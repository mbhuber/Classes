# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current

    for _ in range(to - from_):
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

def partialSum(m,n):
	if n<=1:
		return n

	p = findPeriod(10)
	return (fibonacci_sum(n%p)-fibonacci_sum((m-1)%p))%10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    #print(fibonacci_partial_sum_naive(from_, to))
    print(partialSum(from_,to))
