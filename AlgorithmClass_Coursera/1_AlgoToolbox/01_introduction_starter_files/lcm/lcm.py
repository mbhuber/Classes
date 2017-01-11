# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_alter(a,b):
    res,k = 1,1
    while (a>1) | (b>1):
        k +=1
        e = 1
        while(a%k==0) | (b%k==0):
            if (a%k==0):
                a/=k
            if (b%k==0):
                b/=k
            e+=1
        res *= k**(e-1)
    return res

def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    if (a==1) | (b==1):
        return a*b
    else:
        return int(a/gcd(a,b))*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    print(lcm(a, b))

