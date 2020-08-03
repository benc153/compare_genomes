#!/usr/bin/env python3
import re
from compare_genomes import load
from argparse import *
from textwrap import fill
from pdb import set_trace as brk


def main():
	ap = ArgumentParser()
	ap.add_argument("genome", nargs=1)
	ap.add_argument("range", help="For example 24750..24983", nargs="+")

	args = ap.parse_args()

	genome = load(args.genome[0])
	for r in args.range:
		start, end = [int(x) for x in re.split(r'[^\d+]', r) if x]
		print(r)
		print(fill(genome[start:end], 80))


if __name__ == "__main__":
	main()
