def findZigZagSequence(a, n):
	a.sort()
	mid = int((n + 1) / 2)
	a[mid - 1], a[n - 1] = a[n - 1], a[mid - 1]

	st = mid + 1
	ed = n - 2
	while st <= ed:
		a[st], a[ed] = a[ed], a[st]
		st += 1
		ed -= 1

	for i in range(n):
		if i == n - 1:
			print(a[i])
		else:
			print(a[i], end=' ')
	return


# test_cases = int(input())
# for cs in range (test_cases):
#     n = int(input())
a = [2, 3, 5, 1, 4]
findZigZagSequence(a, len(a))
