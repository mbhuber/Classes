# Uses python3
import sys

def get_change(m):
    #write your code here
    coins=[10,5,1]
    ncoins=0

    for c in coins:
    	if (m>=c):
    		ncoins+=m//c
    		m-=(m//c)*c
    	if (m==0):
    		return ncoins
    return -1

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    #print(get_change(12))
