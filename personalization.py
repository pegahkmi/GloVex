"""compute surprise value with user familiarity and conditional probability of each category"""

import csv
import argparse


def filter(word):
	return word[:-1] if word[-1] == "." else word 

def read_data(inputfile):

	with open(inputfile,'U') as csvfile:
		 reader = csv.reader(csvfile)
		 words = [row[5].split() for row in reader]#select abstract as a list of words
		 words = [[filter(word) for word in abstract] for abstract in words]
	print (words)	 








if __name__ == "__main__":


	parser = argparse.ArgumentParser(description='read list of words from abstract')
	parser.add_argument('csv_file', type=str, help='ACMDL_1000')

	args = parser.parse_args()
	read_data(args.csv_file)



