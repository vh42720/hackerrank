# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password

import re


def minimumNumber(n, password):
	# numbers = "0123456789"
	# lower_case = "abcdefghijklmnopqrstuvwxyz"
	# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# special_characters = "!@#$%^&*()-+"

	digit_error = re.search(r"\d", password) is None
	uppercase_error = re.search(r"[A-Z]", password) is None
	lowercase_error = re.search(r"[a-z]", password) is None
	symbol_error = re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

	total_error = int(digit_error + uppercase_error + lowercase_error + symbol_error)
	total_len = len(password) + total_error
	if total_len < 6:
		total_error += (6 - total_len)

	return total_error


if __name__ == '__main__':
	n = 5
	# password = '2bbbb'
	password = 'Ab1'
	print(minimumNumber(n, password))
