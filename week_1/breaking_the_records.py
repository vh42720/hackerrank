# Complete the 'breakingRecords' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.

def breakingRecords(scores):
	min = scores[0]
	max = scores[0]

	min_cnt = 0
	max_cnt = 0

	for score in scores:
		if score > max:
			max_cnt += 1
			max = score
		elif score < min:
			min_cnt += 1
			min = score

	return [max_cnt, min_cnt]


if __name__ == '__main__':
	scores = [12, 24, 10, 24]
	print(breakingRecords(scores))
