"""
https://adventofcode.com/2022/day/1
"""

import sys

INPUT_FILE_PATH = "./input.txt"

def main():
	try:
		with open(INPUT_FILE_PATH) as input_raw:
      part_1(input_raw)
			part_2(input_raw)

	except IOError as ioe:
		print("{}\nError opening {}. Terminating process.".format(ioe, INPUT_FILE_PATH), file=sys.stderr)
		sys.exit(1)

def part_1(input_raw):
	total_cals_per_elf = [0]
	lines = [i for i in input_raw.read().strip().split("\n")]
	for l in lines:
		if len(l) > 0:
			total_cals_per_elf[-1] += int(l)
		else:
			total_cals_per_elf.append(0)
	total_cals_per_elf.sort()
	print(total_cals_per_elf[-1])
		

def part_2(input_raw):
	total_cals_per_elf = [0]
	lines = [i for i in input_raw.read().strip().split("\n")]
	for l in lines:
		if len(l) > 0:
			total_cals_per_elf[-1] += int(l)
		else:
			total_cals_per_elf.append(0)
	total_cals_per_elf.sort()
	print(
		total_cals_per_elf[-1] +
		total_cals_per_elf[-2] +
		total_cals_per_elf[-3] 
	)


if __name__ == '__main__':
	main()
