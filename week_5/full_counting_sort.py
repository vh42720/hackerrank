# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
from itertools import chain


def countSort(arr):
	n = len(arr)
	sort_arr = [[] for i in range(n)]

	for idx, x in enumerate(arr):
		if idx < n / 2:
			char = '-'
		else:
			char = x[1]
		sort_arr[int(x[0])].append(char)

	# return list(chain.from_iterable(sort_arr))
	print(*list(chain.from_iterable(sort_arr)))


if __name__ == '__main__':
	arr = [[0, 'a'], [1, 'b'], [0, 'c'], [1, 'd']]
	print(countSort(arr))
