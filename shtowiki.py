#!/usr/bin/env python

import argparse
import tempfile
import shutil
import subprocess
import os
import os.path
import sys

def main():
	parser = argparse.ArgumentParser(description='Convert bash script into wiki markup')
	parser.add_argument('-i','--input',default='',help='input script to process')
	parser.add_argument('--prompt',default='% ',help='command prompt to display')
	args = parser.parse_args()

	# Check input arg and prepare output name
	if not args.input:
		print 'Missing required input name.'
		sys.exit(-1)
	if not os.path.exists(args.input):
		print 'No such file %r' % args.input
		sys.exit(-2)
	outname,extension = os.path.splitext(args.input)
	outname += '.textile'
	print 'Generating %r' % outname

	# Prepare the temporary working directory we will use
	workdir = tempfile.mkdtemp()
	print 'Working in %r' % workdir

	# Wrap everything with a try/finally block to make sure we delete the workdir
	try:
		# Open files (before we change directories)
		with open(args.input,'r') as input:
			with open(outname,'w') as output:	
				# Go to the working dir
				os.chdir(workdir)
				# Loop over lines in the input file.
				last = None
				textBuffer = ''
				for line in input:
					if line[0] == '#':
						# Strip off the comment symbol and add to our text buffer
						textBuffer += line[1:].strip() + ' '
						last = 'text'
					else:
						# Output anything in the text buffer as a paragraph.
						if textBuffer:
							print >>output, '\np.',textBuffer
						textBuffer = ''
						if line.strip() == '':
							# Skip blank lines
							last = 'blank'
						else:
							# Otherwise, this is a command
							cmd = line.rstrip()
							# We suppress the output from commands in parentheses
							if cmd[0] == '(' and cmd[-1] == ')':
								quiet = True
								cmd = cmd[1:-1]
							else:
								quiet = False
							# Keep consecutive commands with no output in the same code block
							if not last is 'cmd':
								print >>output, '\npre.',
							print >>output, args.prompt + cmd
							last = 'cmd'
							# Try running the command.
							try:
								result = subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
								if result and not quiet:
									# Display the output in a separate code block,
									# possibly including blank lines.
									print >>output, '\nbc.. ' + result
									last = 'result'
							except subprocess.CalledProcessError,e:
								print 'Command failed: %r' % cmd
								sys.exit(-3)
	finally:
		# recursively delete our workdir and its contents
		shutil.rmtree(workdir)

if __name__ == '__main__':
	main()
