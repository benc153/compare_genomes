#!/usr/bin/env python3
from argparse import *
from compare_genomes import load, search
from pdb import set_trace as brk


def main():
	ap = ArgumentParser()
	ap.add_argument("haystacks", nargs="+")
	ap.add_argument("-t", "--needle", type=str)

	args = ap.parse_args()

	term = args.needle.lower()

	for h in args.haystacks:
		genome = load(h)
		n = search(genome, term)
		print("{}: {}".format(h, n))


if __name__ == "__main__":
	main()
