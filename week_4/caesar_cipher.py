# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k

def caesarCipher(s, k):
	original = 'abcdefghijklmnopqrstuvwxyz'
	new_string = ''

	for i in s:
		if i.lower() not in original:
			new_string += i
		else:
			if i.isupper():
				new_string += original[(original.index(i.lower()) + k) % 26].upper()
			else:
				new_string += original[(original.index(i) + k) % 26]
	return new_string


if __name__ == '__main__':
	s = 'middle-Outz'
	k = 2
	print(caesarCipher(s, k))
