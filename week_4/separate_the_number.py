# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.

def separateNumbers(s):
	is_beautiful = False
	first_nums = []

	for i in range(1, int(len(s) / 2) + 1):
		first_num = int(s[:i])
		first_str = s[:i]

		while len(first_str) < len(s):
			first_num += 1
			first_str += str(first_num)

		if first_str == s:
			# print(f'YES {s[0:i]}')
			is_beautiful = True
			first_nums.append(s[0:i])

	if is_beautiful:
		print(f'YES {min(first_nums)}')
	else:
		print('NO')


if __name__ == '__main__':
	s = '91011'
	print(separateNumbers(s))
