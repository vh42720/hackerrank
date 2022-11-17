# Complete the 'lonelyinteger' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
from collections import Counter


def lonelyinteger(a):
	c = Counter(a)
	return [k for k, v in c.items() if v == 1][0]


if __name__ == '__main__':
	a = [1, 2, 3, 4, 3, 2, 1]

	print(lonelyinteger(a))
