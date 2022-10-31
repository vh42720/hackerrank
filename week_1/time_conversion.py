from datetime import datetime


# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
	return datetime.strptime(s, '%I:%M:%S%p').isoformat(' ')[11:]


if __name__ == '__main__':
	s = '12:01:00AM'
	print(timeConversion(s))
