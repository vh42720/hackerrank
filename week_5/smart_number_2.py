import math


def is_smart_number(num):
	val = int(math.sqrt(num))
	if num / val == val:
		return True
	return False

print(is_smart_number(169))
