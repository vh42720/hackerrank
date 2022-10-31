# https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
import re
import sys


def split_camel(line):
	ret_val = ''
	operation, op_type, words = line.split(';')

	if operation == 'S':
		ret_val = re.sub(r'([A-Z])', r' \1', words).lower().strip()
		ret_val = ret_val.replace(')', '').replace('(', '')
	elif operation == 'C':
		ret_val = words.title().replace(' ', '').strip()
		if op_type == 'M':
			ret_val = ret_val[0].lower() + ret_val[1:]
			ret_val += '()'
		elif op_type == 'V':
			ret_val = ret_val[0].lower() + ret_val[1:]
	else:
		raise RuntimeError('Operation not found')

	print(ret_val)

inputData = [line.rstrip('\n\r') for line in sys.stdin.readlines()]

for s in inputData:
	split_camel(s)


if __name__ == '__main__':
	split_camel([
		'S;M;plasticCup()',
		'C;V;mobile phone',
		'C;C;coffee machine',
		'S;C;LargeSoftwareBook',
		'C;M;white sheet of paper',
		'S;V;pictureFrame',
	])
