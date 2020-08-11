#!/usr/bin/env python3
from argparse import *
from pdb import set_trace as brk
from compare_genomes import load
from random import shuffle


def to_codons(genome):
	ret = []
	for i in range(0, len(genome), 3):
		ret.append(genome[i:i+3])
	return ret


def from_codons(codons):
	return "".join(codons)


def main():
	ap = ArgumentParser()
	ap.add_argument("genome", nargs=1)
	args = ap.parse_args()

	genome = load(args.genome[0])
	codons = to_codons(genome)
	shuffle(codons)
	print(from_codons(codons))


if __name__ == "__main__":
	main()
