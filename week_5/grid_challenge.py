# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.


def gridChallenge(grid):
	sort_grid = []
	col_grid = [''] * len(grid[0])

	for x in grid:
		letters = [l for l in x]
		letters.sort()
		sort_grid.append(''.join(letters))
		for idx, col in enumerate(letters):
			col_grid[idx] += col

	for y in col_grid:
		if y != ''.join(sorted(y)):
			return 'NO'

	return 'YES'


if __name__ == '__main__':
	grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
	print(gridChallenge(grid))
