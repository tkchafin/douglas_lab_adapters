#!/usr/bin/python

import os
import sys
import getopt
import collections as c
import re

def main():
	params=parseArgs()

	temps = c.OrderedDict()
	for t in read_fasta(params.template):
		temps[t[0]] = t[1]

	tags = c.OrderedDict()
	num=0
	for b in read_barcodes(params.tags):
		if params.num and num >= params.num:
			break
		tags[b[0]]=b[1]
		num+=1

	outs = list()
	f_re = re.compile(r'\[f\]')
	r_re = re.compile(r'\[r\]')
	for t in temps.keys():
		if f_re.search(temps[t]):
			for tag in tags.keys():
				oline = t + "_" + tag + "\t"
				oline = oline + re.sub(f_re, tags[tag].lower(), temps[t]) + "\t"
				oline = oline + params.product + "\t" + params.pur
				print(oline)
		elif r_re.search(temps[t]):
			for tag in tags.keys():
				oline = t + "_" + tag + "\t"
				oline = oline + re.sub(r_re, reverseComplement(tags[tag]).lower(), temps[t]) + "\t"
				oline = oline + params.product + "\t" + params.pur
				print(oline)
		else:
			oline = t + "\t"
			oline = oline + temps[t] + "\t"
			oline = oline + params.product + "\t" + params.pur
			print(oline)

#Function to return reverse complement of a nucleotide, while preserving case
def get_revComp_caseless(char):
	lower = False
	if char.islower():
		lower = True
		char = char.upper()
	d = {
		"A"	: "T",
		"G"	: "C",
		"C"	: "G",
		"T"	: "A",
		"N"	: "N",
		"-"	: "-",
		"R"	: "Y",
		"Y"	: "R",
		"S"	: "S",
		"W"	: "W",
		"K"	: "M",
		"M"	: "K",
		"B"	: "V",
		"D"	: "H",
		"H"	: "D",
		"V"	: "B"
	}
	ret = d[char]
	if lower:
		ret = ret.lower()
	return ret


#Function to reverse complement a sequence, with case preserved
def reverseComplement(seq):
	comp = []
	for i in (get_revComp_caseless(j) for j in seq):
		comp.append(i)
	return("".join(comp[::-1]))

#write fasta from dict
def write_fasta(name, d):
	with open(name, 'w') as fh:
		try:
			for sample in d.keys():
				to_write = ">" + str(sample) + "\n" + d[sample] + "\n"
				fh.write(to_write)
		except IOError as e:
			print("Could not read file:",e)
			sys.exit(1)
		except Exception as e:
			print("Unexpected error:",e)
			sys.exit(1)
		finally:
			fh.close()

def read_barcodes(fas):
	if os.path.exists(fas):
		with open(fas, 'r') as fh:
			try:
				contig = ""
				seq = ""
				for line in fh:
					line = line.strip()
					if not line:
						continue
					stuff = line.split("\t")
					if len(stuff) == 2:
						yield([stuff[0],stuff[1]])
					elif len(stuff) ==1:
						yield([stuff[0],stuff[0]])
					else:
						print("Wrong number of elements:",line)

			except IOError:
				print("Could not read file ",fas)
				sys.exit(1)
			finally:
				fh.close()
	else:
		raise FileNotFoundError("File %s not found!"%fas)

#Read samples as FASTA. Generator function
def read_fasta(fas):
	if os.path.exists(fas):
		with open(fas, 'r') as fh:
			try:
				contig = ""
				seq = ""
				for line in fh:
					line = line.strip()
					if not line:
						continue
					#print(line)
					if line[0] == ">": #Found a header line
						#If we already loaded a contig, yield that contig and
						#start loading a new one
						if contig:
							yield([contig,seq]) #yield
							contig = "" #reset contig and seq
							seq = ""
						split_line = line.split()
						contig = (split_line[0].replace(">",""))
					else:
						seq += line
				#Iyield last sequence, if it has both a header and sequence
				if contig and seq:
					yield([contig,seq])
			except IOError:
				print("Could not read file ",fas)
				sys.exit(1)
			finally:
				fh.close()
	else:
		raise FileNotFoundError("File %s not found!"%fas)

#Object to parse command-line arguments
class parseArgs():
	def __init__(self):
		#Define options
		try:
			options, remainder = getopt.getopt(sys.argv[1:], 't:b:o:n:hp:c:', \
			["help"])
		except getopt.GetoptError as err:
			print(err)
			self.display_help("\nExiting because getopt returned non-zero exit status.")
		#Default values for params
		#Input params
		self.template=None
		self.tags=None
		self.out="adapters"
		self.num=None
		self.product="100nm"
		self.pur="STD"


		#First pass to see if help menu was called
		for o, a in options:
			if o in ("-h", "-help", "--help"):
				self.display_help("Exiting because help menu was called.")

		#Second pass to set all args.
		for opt, arg_raw in options:
			arg = arg_raw.replace(" ","")
			arg = arg.strip()
			opt = opt.replace("-","")
			#print(opt,arg)
			if opt == "t":
				self.template = arg
			elif opt == "b":
				self.tags = arg
			elif opt == "o":
				self.out = arg
			elif opt == "n":
				self.num = int(arg)
			elif opt == "p":
				self.pur = arg
			elif opt == "c":
				self.product=arg
			elif opt in ('h', 'help'):
				pass
			else:
				assert False, "Unhandled option %r"%opt

		#Check manditory options are set
		if not self.template:
			self.display_help("No template provided")
		if not self.tags:
			self.display_help("No tags provided")

	def display_help(self, message=None):
		if message is not None:
			print ("\n",message)
		print ("\nmake_adapters.py\n")
		print ("Contact:Tyler K. Chafin, University of Arkansas,tkchafin@uark.edu")
		print ("\nUsage: ", sys.argv[0], "-t <template> -b <barcodes>\n")

		print("\nProbably will add more functions later...")

		print("""
	Arguments:
		INPUT FILES
		-t	: Template file
		-b	: Barcodes

		PARAMETERS
		-n	: Number of barcodes from <-b> to use
		-c	: Concentration [default=100nm]
		-p	: Purification, e.g. de-salting (STD) or HPLC (HPLC) [default=STD]

""")
		sys.exit()


#Call main function
if __name__ == '__main__':
    main()
