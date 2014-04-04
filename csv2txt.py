## csv2txt
## Originally developed by Jorge Meneses (jorgejhms[at]gmail[dot]com).
## Released under a GNU General Public Licence v. 3.0.
## Version 0.2

import argparse, sys, csv

###Arguments definition###
parser = argparse.ArgumentParser(prog="csv2txt", description="Converts a comma-separeted-value file into a diferent txt files for each case.")
parser.add_argument("infile", type=argparse.FileType('r'), help="CSV file to open", default=sys.stdin)
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.2')
args = parser.parse_args()

t = csv.reader(args.infile)
rownumber=1
for row in t:
	print(row) 
	f=open('outfile{0}.txt' .format(rownumber), 'w')
	for item in row:
		f.write("{0}\n \n" .format(item))
	rownumber += 1
	f.close

