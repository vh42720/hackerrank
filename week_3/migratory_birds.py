# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


from collections import Counter


def migratoryBirds(arr):
	bird_counter = Counter(arr)

	max_cnt = max(bird_counter.values())
	max_cnt_dict = [k for k, v in bird_counter.items() if v == max_cnt]

	return min(max_cnt_dict)


if __name__ == '__main__':
	arr = [1, 1, 2, 2, 3]
	print(migratoryBirds(arr))
