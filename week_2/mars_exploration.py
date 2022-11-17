# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
	idx_O = list(range(1, len(s), 3))
	change_cnt = 0

	for idx, val in enumerate(s):
		if idx in idx_O and val != 'O':
			change_cnt += 1
		elif idx not in idx_O and val != 'S':
			change_cnt += 1

	return change_cnt


if __name__ == '__main__':
	s = 'SOSTOT'
	print(marsExploration(s))
