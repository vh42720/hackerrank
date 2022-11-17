# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

from collections import Counter


def sockMerchant(n, ar):
	sock_counter = Counter(ar)
	pair_cnt = 0

	for k, v in sock_counter.items():
		pair_cnt += v // 2

	return pair_cnt


if __name__ == '__main__':
	n = 7
	ar = [1, 2, 1, 2, 1, 3, 2]
	print(sockMerchant(n, ar))
