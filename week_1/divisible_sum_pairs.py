# Complete the 'divisibleSumPairs' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar


def divisibleSumPairs(n, k, ar):
	ar.sort()
	pair_cnt = 0
	for idx, val in enumerate(ar):
		while idx + 1 < n:
			if (val + ar[idx + 1]) % k == 0:
				pair_cnt += 1
			idx += 1

	return pair_cnt


if __name__ == '__main__':
	k = 3
	n = 6
	ar = [1, 3, 2, 6, 1, 2]

	print(divisibleSumPairs(n, k, ar))
