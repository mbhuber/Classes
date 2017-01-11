# Uses python3
##def calc_fib(n):
##    if (n <= 1):
##        return n
##
##    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    if (n <= 1):
        return n
    arr = [0] * (n+1)
    arr[1] = 1

    for k in range(2,n+1):
        arr[k] = arr[k-2] + arr[k-1]

    return arr[-1]

n = int(input())
#print(calc_fib(n))
print(calc_fib_fast(n))
