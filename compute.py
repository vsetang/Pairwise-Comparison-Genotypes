import pandas as pd
import sys
import datetime as dt
import time
import argparse

help_info="""\n

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
		
"""

def combinations(iterable, r):
	"""
	Documentation: https://docs.python.org/2/library/itertools.html

	Combinations function return 'r' length item of elements from iterable
	
	Combinations are emitted in lexicographic sort order. 
	So, if the input iterable is sorted, the combination tuples will be produced 
	in sorted order.

	Elements are treated as unique based on their position, not on their value. 
	So if the input elements are unique, there will be no repeat values in each 
	combination
	
	SAMPLE USAGE: combinations(range(0,3),2)
	SAMPLE OUTPUT:
						(0, 1)
						(0, 2)
						(1, 2)

	SAMPLE USAGE: combinations('ATCG', 2)
	SAMPLE OUTPUT: ('A', 'T')
						('A', 'C')
						('A', 'G')
						('T', 'C')
						('T', 'G')
						('C', 'G')
	"""
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i + n - r:
				break
		else:
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
		yield tuple(pool[i] for i in indices)


#create arg parser information
usage = help_info
parser = argparse.ArgumentParser(prog='compuete.py', usage=usage, add_help=True)

#loop through each argument from command line
for a in sys.argv:
	if a in ['-h','--help']:
		parser.print_help()
		sys.exit()
	else:
		continue

#get todays date
TODAY = dt.datetime.today()
TODAY_STR = TODAY.strftime('%d%b%Y')

#Start time for script
strt = time.time()

#get path of inputfile and read in input samples and genotypes
input_path = sys.argv[1] 
data = pd.read_csv(input_path, engine='python', sep=None, skiprows=0, header=None)

#get total # of genotype columns
num_geno_cols = len(data.columns)-1

print(data, "\n")

#create empty data frame for outputs
file_out = pd.DataFrame()
full_out = pd.DataFrame()

#get # combinations of pairs from inputfile based on their index
comb = combinations(range(0,len(data)),2)

for pair in comb:
	#initialize calculation row and list for the final and raw output
	calc_row = []
	final_set = []
	full_set = []
	for g_col in data:
		#add sample name to calculation row
		if g_col == 0:
			name = str(str(data.iloc[pair[0],0]) + '_' + str(data.iloc[pair[1],0]))
			calc_row.append(str(name))
		#loop through genotype columns
		elif ((g_col != 0)):
			#check if '.' exists between pairs. if it does, we append '.' to our calc list and skip
			if ((data.iloc[pair[0], g_col] == '.') | (data.iloc[pair[1], g_col] == '.')):
				calc_row.append('.')
			else:
			#calculate absolute value of the difference in scores
				val = abs(int(data.iloc[pair[0],g_col]) - int(data.iloc[pair[1],g_col]))
				calc_row.append(int(val))
			#if itteration reached last column
			if (g_col == num_geno_cols):
				#calculate total score 
				total_score = sum(filter(lambda x: isinstance(x,int), calc_row))

				#if total score equals 0 or 1 add both pairs and score to final list
				if ((total_score == 0 ) | (total_score == 1)):
					final_set.append(str(data.iloc[pair[0],0]))
					final_set.append(str(data.iloc[pair[1],0]))
					final_set.append(total_score)
					file_out = file_out.append([final_set]).reset_index(drop=True)	

				#get full listing of samples and scores and append to list
				if total_score >= 0:
					full_set.append(str(data.iloc[pair[0],0]))
					full_set.append(str(data.iloc[pair[1],0]))
					full_set.append(total_score)
					full_out = full_out.append([full_set]).reset_index(drop=True)

#check if anything was added to the output frame
if file_out.shape[0] == 0:
	print("No Match of distance scores of 0 or 1")
	file_out = file_out.append(['No Match'])
	file_out.to_csv(TODAY_STR + '_output.txt', sep='\t', index=False)
	sys.exit()
else:
	#Update names of data frame
	file_out.columns = ['Samp1', 'Samp2', 'Score']
	#create text file of the results
	file_out.to_csv(TODAY_STR + '_output.txt', sep='\t', index=False)
	print("0/1 Score file: " + TODAY_STR + '_output.txt')

	#Create columns for full listing
	full_out.columns = ['Samp1', 'Samp2', 'Score']
	#create text file of the results of full listing
	full_out.to_csv(TODAY_STR + '_RAW_output.txt', sep='\t', index=False)
	print("Full Score file: " + TODAY_STR + '_output.txt')
	

end = time.time()
print('Total Running Time: %.2f' %(end-strt))
