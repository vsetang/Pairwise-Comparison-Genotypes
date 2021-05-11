# Pairwise-Comparison-Genotypes
## Author
Vincent Setang
## Description
QC measures to make sure that samples are plated correctly. Assuming that samples are coded with the genotypes listed below, the distance score would be the sum of absolute differences in genotype across all variants.

***compute.py*** will calculate the pairwise distance scores between pairs of samples
and output two text file with the paired sample with their total distance score of
0 or 1 and another file with the raw scores of all combinations of samples.

***INPUTS***:	Space or tab delimited text file that contains sample name on first column, and
	sample's genotype for the rest of the columns

**GENOTYPES**:		
- "**0**"	:	Homozygous reference
- "**1**"	:	Heterozygote
- "**2**"	:	Homozygote Alternate
- "**.**"	:	Missing 

***OUTPUT***:	Two tab delimated text file with the the paired sample and their score of
	either 0 or 1 in one file and a full listing in a second file. 
Samp1 | Samp2 | Score
------------ | ------------- | -------------


## Useage Example
python compute.py <input_file_path>

## Requirements
This script was originally written for Python 2.7 but was updated for Python 3.6. The following packages are needed
- pandas	
- sys		
- datetime	
- time	
- argparse	
