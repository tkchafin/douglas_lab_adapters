# douglas_lab_adapters
Repository for designing our RAD and UCE adapters. 

All tags and indices taken from: Faircloth and Glenn. 2012. Not All Sequence Tags Are Created Equal: Designing and Validating Sequence Identification Tags Robust to Indels. Plos One. [doi:10.1371/journal.pone.0042543](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0042543)

## Usage
````
$ python3 ./make_adapters.py -h

 Exiting because help menu was called.

make_adapters.py

Contact:Tyler K. Chafin, University of Arkansas,tkchafin@uark.edu

Usage:  ./make_adapters.py -t <template> -b <barcodes>


Probably will add more functions later...

	Arguments:
		INPUT FILES
		-t	: Template file
		-b	: Barcodes

		PARAMETERS
		-n	: Number of barcodes from <-b> to use
		-c	: Concentration [default=100nm]
		-p	: Purification, e.g. de-salting (STD) or HPLC (HPLC) [default=STD]

````

The required inputs are a <template> file, where [f] is a placeholder for the FORWARD sequence of each tag, and [r] for the REVERSE sequence:
	
````
>ddRAD2.0_PstI_P1.1
ACACTCTTTCCCTACACGACGCTCTTCCGATCT[f]TGC*A

>ddRAD2.0_PstI_P1.2
/5Phos/[r]AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT

>ddRAD2.0_MspI_P2.1
GTGACTGGAGTTCAGACGTGTGCTCTTCCGATC*T

>ddRAD2.0_MspI_P2.2
/5phos/GATCGGAAGAGCGAGAACAA
````
Sequences without an [f] or [r] tag will be output as-is. Tag sequences will be output for each input barcode, with the barcode ID or name appended to the header. 

The <tags> file can be provided one of two ways. Either with one tag on each line:
````
AGTCCGACTG
AAGGTGCCTG
ATATCCGTGG
GGAGCTATGG
CCATATGAAC
GCAATTACCG
AATGCTGGTT
AACAACAACC
ACCGCCTATT
ACACGTATGA
CCGACTAAGC
...
...
...
````
In which case the whole tag sequence will be treated as the tag ID and appended to the full oligo name, or you can provide the desired idenfier as a first column in a tab-delimited file:
````
IDX13	CGATGT
IDX14	TGACCA
IDX15	ACAGTG
IDX16	GCCAAT
IDX17	CAGATC
IDX18	GATCAG
IDX19	CTTGTA
...
...
````

To run the program, provide the desired tag and template files to make_adapters.py:
```
$ python3 ./make_adapters.py -t uce_template.fasta -b 10nt_ed5_tags.txt 
```




