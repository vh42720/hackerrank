# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.

def flippingBits(n):
	bit_32 = f'{n:032b}'.replace('0', '2').replace('1', '0').replace('2', '1')
	return int(bit_32, 2)


if __name__ == '__main__':
	bits = [2147483647, 1, 0]
	for bit in bits:
		print(flippingBits(bit))
