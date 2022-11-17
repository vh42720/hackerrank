# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p


def pageCount(n, p):
	if n % 2 == 0:
		n += 1

	return int(min(p / 2, (n - p) / 2))


if __name__ == '__main__':
	n = 6
	p = 5
	print(pageCount(n, p))
