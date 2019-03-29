# douglas_lab_adapters
Repository for designing our RAD and UCE adapters. 

All tags and indices taken from: Faircloth and Glenn. 2012. Not All Sequence Tags Are Created Equal: Designing and Validating Sequence Identification Tags Robust to Indels. Plos One. [doi:10.1371/journal.pone.0042543](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0042543)

Credit for the degenerate base modification in the p2 adapter goes to Tin et al (2015). Degenerate adaptor sequences for detecting PCR duplicatesin reduced representation sequencing data improve genotypecalling accuracy. Molecular Ecology Resources. [doi: 10.1111/1755-0998.12314](https://onlinelibrary.wiley.com/doi/epdf/10.1111/1755-0998.12314)

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
````
$ python3 ./make_adapters.py -t uce_template.fasta -b 10nt_ed5_tags.txt 
````

## Outputs
make_adapters.py will output data formatted for the IDT bulk order form:
````
UCE2.0_P1.1_AGTCCGACTG	ACACTCTTTCCCTACACGACGCTCTTCCGATCTagtccgactg*T	100nm	STD
UCE2.0_P1.1_AAGGTGCCTG	ACACTCTTTCCCTACACGACGCTCTTCCGATCTaaggtgcctg*T	100nm	STD
UCE2.0_P1.1_ATATCCGTGG	ACACTCTTTCCCTACACGACGCTCTTCCGATCTatatccgtgg*T	100nm	STD
UCE2.0_P1.1_GGAGCTATGG	ACACTCTTTCCCTACACGACGCTCTTCCGATCTggagctatgg*T	100nm	STD
UCE2.0_P1.1_CCATATGAAC	ACACTCTTTCCCTACACGACGCTCTTCCGATCTccatatgaac*T	100nm	STD
UCE2.0_P1.1_GCAATTACCG	ACACTCTTTCCCTACACGACGCTCTTCCGATCTgcaattaccg*T	100nm	STD
UCE2.0_P1.1_AATGCTGGTT	ACACTCTTTCCCTACACGACGCTCTTCCGATCTaatgctggtt*T	100nm	STD
UCE2.0_P1.1_AACAACAACC	ACACTCTTTCCCTACACGACGCTCTTCCGATCTaacaacaacc*T	100nm	STD
UCE2.0_P1.1_ACCGCCTATT	ACACTCTTTCCCTACACGACGCTCTTCCGATCTaccgcctatt*T	100nm	STD
UCE2.0_P1.1_ACACGTATGA	ACACTCTTTCCCTACACGACGCTCTTCCGATCTacacgtatga*T	100nm	STD
UCE2.0_P1.1_CCGACTAAGC	ACACTCTTTCCCTACACGACGCTCTTCCGATCTccgactaagc*T	100nm	STD
UCE2.0_P1.1_GGCGGATTGA	ACACTCTTTCCCTACACGACGCTCTTCCGATCTggcggattga*T	100nm	STD
UCE2.0_P1.1_TTGGCGGTTC	ACACTCTTTCCCTACACGACGCTCTTCCGATCTttggcggttc*T	100nm	STD
UCE2.0_P1.1_GGCGTTACAT	ACACTCTTTCCCTACACGACGCTCTTCCGATCTggcgttacat*T	100nm	STD
UCE2.0_P1.1_GGTTGTGGCT	ACACTCTTTCCCTACACGACGCTCTTCCGATCTggttgtggct*T	100nm	STD
UCE2.0_P1.1_AAGTCGTTGT	ACACTCTTTCCCTACACGACGCTCTTCCGATCTaagtcgttgt*T	100nm	STD
UCE2.0_P1.1_ATGGAAGGAA	ACACTCTTTCCCTACACGACGCTCTTCCGATCTatggaaggaa*T	100nm	STD
UCE2.0_P1.1_TTGTCTCGAC	ACACTCTTTCCCTACACGACGCTCTTCCGATCTttgtctcgac*T	100nm	STD
UCE2.0_P1.1_AACACGGAAT	ACACTCTTTCCCTACACGACGCTCTTCCGATCTaacacggaat*T	100nm	STD
UCE2.0_P1.1_TCCAATACTC	ACACTCTTTCCCTACACGACGCTCTTCCGATCTtccaatactc*T	100nm	STD
UCE2.0_P1.1_TAGTGATGCA	ACACTCTTTCCCTACACGACGCTCTTCCGATCTtagtgatgca*T	100nm	STD
UCE2.0_P1.1_CGATAGGCTG	ACACTCTTTCCCTACACGACGCTCTTCCGATCTcgataggctg*T	100nm	STD
UCE2.0_P1.1_CGTAGTATAC	ACACTCTTTCCCTACACGACGCTCTTCCGATCTcgtagtatac*T	100nm	STD
UCE2.0_P1.1_ACAGAAGACT	ACACTCTTTCCCTACACGACGCTCTTCCGATCTacagaagact*T	100nm	STD
UCE2.0_P1.2_AGTCCGACTG	/5Phos/cagtcggactAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_AAGGTGCCTG	/5Phos/caggcaccttAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_ATATCCGTGG	/5Phos/ccacggatatAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_GGAGCTATGG	/5Phos/ccatagctccAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_CCATATGAAC	/5Phos/gttcatatggAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_GCAATTACCG	/5Phos/cggtaattgcAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_AATGCTGGTT	/5Phos/aaccagcattAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_AACAACAACC	/5Phos/ggttgttgttAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_ACCGCCTATT	/5Phos/aataggcggtAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_ACACGTATGA	/5Phos/tcatacgtgtAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_CCGACTAAGC	/5Phos/gcttagtcggAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_GGCGGATTGA	/5Phos/tcaatccgccAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_TTGGCGGTTC	/5Phos/gaaccgccaaAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_GGCGTTACAT	/5Phos/atgtaacgccAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_GGTTGTGGCT	/5Phos/agccacaaccAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_AAGTCGTTGT	/5Phos/acaacgacttAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_ATGGAAGGAA	/5Phos/ttccttccatAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_TTGTCTCGAC	/5Phos/gtcgagacaaAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_AACACGGAAT	/5Phos/attccgtgttAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_TCCAATACTC	/5Phos/gagtattggaAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_TAGTGATGCA	/5Phos/tgcatcactaAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_CGATAGGCTG	/5Phos/cagcctatcgAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_CGTAGTATAC	/5Phos/gtatactacgAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P1.2_ACAGAAGACT	/5Phos/agtcttctgtAGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT	100nm	STD
UCE2.0_P2.1	GTGACTGGAGTTCAGACGTGTGCTCTTCCGATC*T	100nm	STD
UCE2.0_P2.2	/5phos/GATCGGAAGAGCGAGAACAA	100nm	STD
````
You can change the desired concentration and purifications using the <-c> and <-p> flags. 

## Our lab's adapters
We typically use the standard desalting for the P1.1, P2.1, P2.2, and PCR oligos, and HPLC for the P1.2. We order everything at 100nm. 

### Generating Douglas Lab 'ddRAD 1.0' adapters:
These are our adapters for legacy projects. They use the Peterson et al 2012 templates, with PstI (p1) and MspI (p2) overhangs, a 5-base barcode in the p1 adapter, and a 6-base TruSeq style index in the p2 adapter

Add in later. 

### Generating Douglas Lab 'ddRAD 2.0' adapters:
These are a modification of the 1.0 adapters, with the 5' barcodes replaced with 8-base long barcodes with a minimum edit distance of 3 (see Faircloth and Glenn 2012), and optional 40base degenerate region after the 6-base p2 index (see Tin

````
#generate the P1 and P2 adapters
python3 ./make_adapters.py -t ddrad_template.fasta -b 8nt_ed4_tags.txt | sed -E 's/(.*P1.2.*)STD(.*)/\1HPLC\2/g' > IDT-bulk_ddRAD2.0_adapters.tsv

#add on the PCR adapters
python3 ./make_adapters.py -t pcr_primer_template.fasta -b 6nt_ed3_indices.txt >> IDT-bulk_ddRAD2.0_adapters.tsv 

#optional: use degenerate bases in the i7 index
python3 ./make_adapters.py -t pcr_primer_template.fasta -b 6nt_ed3_de4_indices.txt >> IDT-bulk_ddRAD2.0_adapters.tsv 
````

### Generating Douglas Lab UCE adapters
These use the same base template as the ddRAD adapters, but with a 10-base, edit-distance 5 barcode, and T-overhangs for ligation following dA tailing. 
````
$ python3 ./make_adapters.py -t uce_template.fasta -b 10nt_ed5_tags.txt -n 24 | sed -E 's/(.*P1.2.*)STD(.*)/\1HPLC\2/g' > IDT-bulk_UCE_adapters.tsv
````




