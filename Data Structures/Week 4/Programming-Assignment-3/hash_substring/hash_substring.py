# python3
next_prime = 1000000007 
x_temp = 263
def read_input():
	return (input().rstrip(), input().rstrip())

def print_occurrences(output):
	print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
	result = []
	l = len(pattern)
	hashedValues = sum([ord(pattern[i]) for i in range(len(pattern))])
	currentHashedVal = sum([ord(text[:l][i]) for i in range(len(text[:l]))])
	if text[:l] == pattern:
		result.append(0)
	for i in range(1,len(text)-l+1):
		currentHashedVal = currentHashedVal - ord(text[i-1]) + ord(text[i+l-1])
		if currentHashedVal == hashedValues:
			if text[i:i+l] == pattern: result.append(i)
	return result



	

if __name__ == '__main__':
	print_occurrences(get_occurrences(*read_input()))