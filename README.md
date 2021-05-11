# Pairwise-Comparison-Genotypes
QC measures to make sure that samples are plated correctly 

This program was written for python 2.7 and requires pandas 0.23.3. Will work with pandas 0.20.3.
This program was modified for python3 on 5/11/2021 
If pandas is not installed, please use the following command to install pandas.

********** Download Pandas **********
pip install pandas
\n

DESCRIPTION:
compute.py will calculate the pairwise distance scores between pairs of samples
and output a text file with the paired sample with their total distance score of
0 or 1. Total distance scores > 1 will be omitted in one file. The program will also
produce a second file with the full combination of samples and their scores

INPUTS:	Space or tab delimited text file that contains sample name on first column, and
	sample's genotype for the rest of the columns

GENOTYPES:		0 - Homozygous reference
			1 - Heterozygote
			2 - Homozygote Alternate
			. - Missing 

OUTPUT:	Tab delimated text file with the the paired sample and their score of
	either 0 or 1 in one file and a full listing in a second file. 

			Samp1	Samp2	Score
\n

********** USAGE EXAMPLE **********
python compute.py <input_file_path>
