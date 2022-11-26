def divide(x, nums):
	for num in nums:
		if x % num != 0:
			return False
	return True


def divide_by(y, nums):
	for num in nums:
		if num % y != 0:
			return False
	return True


def getTotalX(a, b):
	res = []
	for i in range(max(a), min(b) + 1, 1):
		if not divide(i, a) or not divide_by(i, b):
			continue
		res.append(i)
	return len(set(res))


if __name__ == '__main__':
	arr = [2, 4]
	brr = [16, 32, 96]
	print(getTotalX(arr, brr))
