# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr

def maxMin(k, arr):
	# arr = list(set(arr))
	arr.sort()
	diffs = []
	for idx, val in enumerate(arr[:len(arr) - k + 1]):
		diffs.append(arr[idx + k - 1] - val)

	# return diffs
	return min(diffs)


# return diffs

if __name__ == '__main__':
	k = 4
	arr = [10, 4, 1, 2, 3, 4, 10, 20, 30, 40, 100, 200]

	print(maxMin(k, arr))
