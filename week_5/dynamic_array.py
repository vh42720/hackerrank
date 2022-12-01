# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries

def dynamicArray(n, queries):
	arr = []
	for i in range(n):
		arr.append([])
	last_answer = 0
	answers = []

	for query in queries:
		if query[0] == 1:
			idx = (query[1] ^ last_answer) % n
			arr[idx].append(query[2])
		elif query[0] == 2:
			idx = (query[1] ^ last_answer) % n
			last_answer = arr[idx][query[2] % len(arr[idx])]
			answers.append(last_answer)
		else:
			raise RuntimeError(f'Query not recognized: {query}')

	return answers


if __name__ == '__main__':
	n = 2
	queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
	print(dynamicArray(n, queries))
