# Pairwise-Comparison-Genotypes
QC measures to make sure that samples are plated correctly 

This program was written for python 2.7 and requires pandas 0.23.3. Will work with pandas 0.20.3.
This program was modified for python 3 on 5/11/2021 
If pandas is not installed, please use the following command to install pandas.

********** Download Pandas **********
pip install pandas

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


********** USAGE EXAMPLE **********
python compute.py <input_file_path>

********** TASK ******************
QC measures to make sure that samples are plated correctly and that everyone is who we think they are. In order to do this, we will be running a small SNP panel (~25 variants) on all samples that we receive at once, and then we want to compare the samples to determine if there are any that are the same. In an ideal world, the only samples that will be the same will be replicates, but that’s not necessarily a guarantee.
 
The idea would be to take a set of PLINK files (i.e. sample and genotype information) and then perform a pairwise comparison between samples, generating a distance score for each pair.
 
Assuming that we can code the genotypes as 0 (homozygous reference), 1 (heterozygote), and 2 (homozygote alternate), the distance score would be the sum of absolute differences in genotype across all variants. The machine we’re using to do this small panel will also output a missing call if it is not able to make a genotype determination (indicated by a ‘.’ here); if either person is missing a genotype for a particular variant, that variant should not contribute to the score.
 
Example: Using 10 genotypes for illustration
 
PersonA  1 1 1 2 0 1 0 . 2 1
PersonB  0 1 1 2 1 0 0 1 . 2
 
In this example, the genotypes for variants 8 and 9 will not be counted for the score since there is a missing call. The total score for this pair should be 1 + 1 + 1 + 1 = 4 (for 1 difference in the scores for variants 1, 5, 6, and 10). 
 
 
If the score for a pair is 0 or 1, we want to output that pair along with their score. 
Any pairs meeting this criterion will be sequenced on a larger panel (~40-50 variants), and we will want to re-compute the distance scores using the new panel results.
