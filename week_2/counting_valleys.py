# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

def countingValleys(steps, path):
	# stack
	at_sea = True
	step_stack = []
	valley_cnt = 0

	for step in path:
		# up or down
		if not step_stack:
			step_stack.append(step)
			if step == 'D':
				valley_cnt += 1
			at_sea = False
			continue

		if not at_sea and step != step_stack[-1]:
			step_stack.pop()
		else:
			step_stack.append(step)

		if not step_stack:
			at_sea = True

	return valley_cnt


if __name__ == '__main__':
	steps = 8
	path = 'UDDDUDUU'

	print(countingValleys(steps, path))
