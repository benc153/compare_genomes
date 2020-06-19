#!/usr/bin/env python3
import re
from argparse import *
from pdb import set_trace as brk


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


def compare(a, b):
	for n_codons in range(4, 50):
		count = 0
		for ss in subsequences(a, n_codons):
			n_matches = search(b, ss)
			count += n_matches
		print(n_codons, count)
		if count == 0: break


def main():
	ap = ArgumentParser()
	ap.add_argument("genome", nargs=2)
	args = ap.parse_args()

	print("{} vs {}".format(*args.genome))
	print("length in codons    number of matches")
	a, b = [load(f) for f in args.genome]
	compare(a, b)


if __name__ == "__main__":
	main()
