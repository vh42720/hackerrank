# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
from functools import reduce
from operator import ixor


def sansaXor(arr):
	if len(arr) % 2 != 0:
		return reduce(ixor, arr[::2])
	else:
		return 0


if __name__ == '__main__':
	arr = [3, 4, 5]
	print(sansaXor(arr))
