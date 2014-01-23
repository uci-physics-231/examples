#!/usr/bin/env python

import argparse
import subprocess
import os
import os.path
import sys

def main():
	parser = argparse.ArgumentParser(description='Convert bash script into wiki markup')
	parser.add_argument('-i','--input',default='',help='input script to process')
	parser.add_argument('--tmp-path',default='shtowiki',metavar='NAME',help='run from /tmp/NAME')
	parser.add_argument('--prompt',default='% ',help='command prompt to display')
	args = parser.parse_args()

	if not args.input:
		print 'Missing required input name.'
		sys.exit(-1)
	if not os.path.exists(args.input):
		print 'No such file %r' % args.input
		sys.exit(-2)
	outname,extension = os.path.splitext(args.input)
	outname += '.textile'
	print 'Generating %r' % outname

	# Open files (before we change directories)
	with open(args.input,'r') as input:
		with open(outname,'w') as output:	
			# Go to the requested directory, creating it if necessary.
			where = os.path.join('/tmp',args.tmp_path)
			if not os.path.exists(where):
				os.mkdir(where)
			os.chdir(where)
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
					result = subprocess.check_output(cmd,shell=True)
					if result:
						# Display the output in a separate code block, possibly including blank lines.
						print >>output, '\nbc.. ' + result
						last = 'result'
					else:
						last = 'cmd'

if __name__ == '__main__':
	main()
