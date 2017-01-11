# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

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

def findPeriod2(m):
	a, b = 0, 1
	for i in range(m*m):
		a,b = b, (a+b)%m
		if (a == 0) & (b==1):
			return i+1
	return 0

def get_fibonacci_huge(n,m):
	return get_fibonacci_huge_naive(n%findPeriod(m),m)


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge(n, m))

