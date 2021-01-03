#!/usr/bin/env python3
import re
from argparse import *
from pdb import set_trace as brk


CODON_TABLE = {
		"ttt": 'F',	# Phenylalanine
		"ttc": 'F',

		"tta": 'L',	# Leucine
		"ttg": 'L',
		"ctt": 'L',
		"ctc": 'L',
		"cta": 'L',
		"ctg": 'L',

		"att": 'I',	# Isoleucine
		"atc": 'I',
		"ata": 'I',

		"atg": 'M',	# Methionine

		"gtt": 'V',	# Valine
		"gtc": 'V',
		"gta": 'V',
		"gtg": 'V',

		"tct": 'S',	# Serine
		"tcc": 'S',
		"tca": 'S',
		"tcg": 'S',

		"cct": 'P',	# Proline
		"ccc": 'P',
		"cca": 'P',
		"ccg": 'P',

		"act": 'T',	# Threonine
		"acc": 'T',
		"aca": 'T',
		"acg": 'T',

		"gct": 'A',	# Alanine
		"gcc": 'A',
		"gca": 'A',
		"gcg": 'A',

		"tat": 'Y',	# Tyrosine
		"tac": 'Y',

		"taa": 'X',	# Stop
		"tag": 'X',

		"cat": 'H',	# Histidine
		"cac": 'H',

		"caa": 'Q',	# Glutadine
		"cag": 'Q',

		"aat": 'N',	# Asparagine
		"aac": 'N',

		"aaa": 'K',	# Lysine
		"aag": 'K',

		"gat": 'D',	# Aspartic acid
		"gac": 'D',

		"gaa": 'E',	# Glutamic acid
		"gag": 'E',

		"tgt": 'C',	# Cysteine
		"tgc": 'C',

		"tga": 'X',	# Stop
		"tgg": 'W',	# Tryptophan

		"cgt": 'R',	# Arginine
		"cgc": 'R',
		"cga": 'R',
		"cgg": 'R',

		"agt": 'S',	# Serine
		"agc": 'S',

		"aga": 'R',	# Arginine (again)
		"agg": 'R',

		"ggt": 'G',	# Glycine
		"ggc": 'G',
		"gga": 'G',
		"ggg": 'G',
	}


def load(fname):
	lines = []
	with open(fname) as fp:
		for line in fp:
			line = re.sub(r'\s*\d* ', '', line).strip()
			lines.append(line)
	return "".join(lines)


def subsequences(genome, n_codons):
	n = len(genome)
	ss_len = n_codons * 3

	for i in range(0, n, 3):
		result = genome[i:i+ss_len]
		if len(result) == ss_len:
			yield result


def search(genome, sequence):
	"""Returns the number of matches"""
	n = len(sequence)
	ret = 0

	while True:
		pos = genome.find(sequence)
		if pos == -1: break

		ret += 1
		genome = genome[pos+n:]

	return ret


def convert_to_aa(genome):
	"""Convert a genome to an amino acid sequence"""
	ret = []
	for i in range(0, len(genome), 3):
		codon = genome[i:i+3]

		if len(codon) == 3:
			ret.append(CODON_TABLE[codon])

	return "".join(ret)


def compare(a, b):
	for n_codons in range(4, 50):
		count = 0
		for ss in subsequences(a, n_codons):
			n_matches = search(b, ss)
			count += n_matches
		print(n_codons, count)
		if count == 0: break


def compare_aa(a, b):
	"""Compare amino acids rather than bases"""
	b = convert_to_aa(b)
	for n_codons in range(4, 50):
		count = 0
		for ss in subsequences(a, n_codons):
			n_matches = search(b, convert_to_aa(ss))
			count += n_matches
		print(n_codons, count)
		if count == 0: break


def main():
	ap = ArgumentParser()
	ap.add_argument("genome", nargs=2)
	ap.add_argument('-a', "--amino-acids", action="store_true",
			help="Compare by amino acids")
	args = ap.parse_args()

	print("{} vs {}".format(*args.genome))
	print("length in codons    number of matches")
	a, b = [load(f) for f in args.genome]

	if args.amino_acids:
		compare_aa(a, b)
	else:
		compare(a, b)


if __name__ == "__main__":
	main()
