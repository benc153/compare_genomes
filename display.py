import sys
from argparse import *
import compare_genomes as cg


def display(genome, fp=sys.stdout):
	n = len(genome)

	for i in range(0, n, 3):
		codon = genome[i:i+3]
		aa = cg.CODON_TABLE.get(codon, "NOT FOUND")
		print("{} {}".format(codon, aa), file=fp)


def main():
	ap = ArgumentParser()
	ap.add_argument("genome", nargs="+")
	ap.add_argument('-s', "--shift", type=int)

	args = ap.parse_args()

	for fname in args.genome:
		genome = cg.load(fname)

		if args.shift:
			genome = genome[args.shift:]

		display(genome)


if __name__ == "__main__":
	main()
