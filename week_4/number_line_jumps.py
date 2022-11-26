# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2

def kangaroo(x1, v1, x2, v2):
	if x1 == x2 and v1 != v2:
		return 'NO'
	elif x1 != x2 and v1 == v2:
		return 'NO'
	elif (x1 - x2) / (v2 - v1) <= 0:
		return 'NO'
	elif not ((x1 - x2) / (v2 - v1)).is_integer():
		return 'NO'
	else:
		return 'YES'


if __name__ == '__main__':
	x1 = 43
	v1 = 2
	x2 = 70
	v2 = 2

	print(kangaroo(x1, v1, x2, v2))
