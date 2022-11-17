# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

import string


def pangrams(s):
	is_pangram = len(set(s.replace(' ', '').lower())) == len(string.ascii_lowercase)

	if is_pangram:
		return 'pangram'
	else:
		return 'not pangram'


if __name__ == '__main__':
	s1 = 'We promptly judged antique ivory buckles for the next prize'
	print(pangrams(s1))

	s2 = 'We promptly judged antique ivory buckles for the prize'
	print(pangrams(s2))
