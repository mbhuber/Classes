# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10
        sum += current

    return sum%10

def findPeriod(m):
	prev, current = 0, 1
	n=1
	while (True):
		prev, current = current, (prev+current)%m
		if (prev == 0) & (current==1):
			return n
		else:
			n+=1
	return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #print(fibonacci_sum_naive(n))
    print(fibonacci_sum_naive(n%findPeriod(10)))
