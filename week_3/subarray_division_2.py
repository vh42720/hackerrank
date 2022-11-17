# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m

def birthday(s, d, m):
	cnt = 0

	for idx, val in enumerate(s):
		# exit
		if idx + m - 1 > len(s):
			break

		# check
		if sum(s[idx:(idx + m)]) == d:
			cnt += 1

	return cnt


if __name__ == '__main__':
	s = [2, 2, 1, 3, 2]
	d = 4
	m = 2

	print(birthday(s, d, m))
