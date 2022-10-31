# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.


def plusMinus(arr):
	pos_cnt = 0
	neg_cnt = 0
	zero_cnt = 0

	for num in arr:
		if num == 0:
			zero_cnt += 1
		elif num < 0:
			neg_cnt += 1
		else:
			pos_cnt += 1

	print(f'{(pos_cnt / len(arr)):.6f}')
	print(f'{(neg_cnt / len(arr)):.6f}')
	print(f'{(zero_cnt / len(arr)):.6f}')


if __name__ == '__main__':
	arr = [1, 1, 0, -1, -1]

	plusMinus(arr)
