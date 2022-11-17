# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B

def twoArrays(k, A, B):
	# A_compliment = [k - i for i in A]
	# min_threhold = min(A_compliment)

	# if min(B) < min_threhold:
	# 	return 'NO'
	# elif (min(B) == min_threhold) and (A_compliment.count(min_threhold) < B.count(min(B))):
	# # elif A_compliment.count(min_threhold) < B.count(min(B)):
	# 	return 'NO'
	# elif min(B) > min_threhold:
	# 	return 'YES'
	# else:
	# 	return 'YES'

	# sort
	A.sort()
	A.reverse()
	B.sort()

	for a, b in zip(A, B):
		if a + b < k:
			return 'NO'

	return 'YES'

if __name__ == '__main__':
	# n = 3
	# k = 10
	# A = [2, 1, 3]
	# B = [7, 8, 9]

	n = 4
	k = 5
	A = [1,2,2,1]
	B = [3,3,3,4]

	print(twoArrays(k, A, B))
