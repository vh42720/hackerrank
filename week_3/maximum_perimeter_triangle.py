# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.

from itertools import combinations


def maximumPerimeterTriangle(sticks):
	candidates = []
	max_peri = 0
	max_side = 0
	min_side = 0

	for sides in combinations(sticks, 3):
		# print(sides, max(sides), sum(sides) - max(sides))
		peri = sum(sides)
		max_side_temp = max(sides)
		min_side_temp = min(sides)

		# check triangle
		if (peri - max_side_temp) <= max_side_temp:
			continue

		# check max peri
		if peri >= max_peri:
			max_peri = peri
			if max_side_temp >= max_side:
				max_side = max_side_temp
				if min_side_temp >= min_side:
					min_side = min_side_temp

					candidate = list(sides)
					candidate.sort()
					candidates.append(candidate)

	if candidates:
		return candidates[-1]
	else:
		return [-1]


if __name__ == '__main__':
	sticks = [1, 2, 3, 4, 5, 10]
	print(maximumPerimeterTriangle(sticks))
