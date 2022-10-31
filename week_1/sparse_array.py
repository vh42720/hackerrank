#!/bin/python3


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
	ret_val = []

	for query in queries:
		cnt = 0
		for string in strings:
			if query == string:
				cnt += 1
		ret_val.append(cnt)

	return ret_val


if __name__ == '__main__':
	strings = ['ab', 'ab', 'abc']
	queries = ['ab', 'abc', 'bc']

	print(matchingStrings(strings, queries))
