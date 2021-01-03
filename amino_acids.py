from argparse import *
from compare_genomes import convert_to_aa, load
from pdb import set_trace as brk


def main():
	ap = ArgumentParser()
	ap.add_argument('-n', "--newlines", action="store_true")
	ap.add_argument("genome", nargs=1)
	args = ap.parse_args()

	genome = load(args.genome[0])
	aa = convert_to_aa(genome)

	if args.newlines:
		for a in aa:
			print(a)
	else:
		print(convert_to_aa(genome))


if __name__ == "__main__":
	main()
