# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr

def rotateLeft(d, arr):
	# rotate
	return arr[d:] + arr[:d]

if __name__ == '__main__':
	d = 4
	arr = [1, 2, 3, 4, 5]
	print(rotateLeft(d, arr))
