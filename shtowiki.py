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
				for line in input:
					if line.strip() == '':
						last = None
					elif line[0] == '#':
						# Strip the comment sign from explanatory text and format as a paragraph.
						if not last is 'text':
							print >>output, '\np.',
						print >>output, line[1:].strip()
						last = 'text'
					else:
						# Format commands as block code.
						cmd = line.rstrip()
						if not last is 'cmd':
							print >>output, '\npre.',
						print >>output, args.prompt + cmd
						# Try running the command.
						try:
							result = subprocess.check_output(cmd,shell=True)
							if result:
								# Display the output in a separate code block,
								# possibly including blank lines.
								print >>output, '\nbc.. ' + result
								last = 'result'
							else:
								last = 'cmd'
						except subprocess.CalledProcessError,e:
							print 'Command failed: %r' % cmd
							sys.exit(-3)
	finally:
		# recursively delete our workdir and its contents
		shutil.rmtree(workdir)

if __name__ == '__main__':
	main()
