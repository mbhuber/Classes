# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

import sys

def maxPairProduct(arr):    
    ind1 = 0
    for k in range(len(arr)):
        if (arr[k] > arr[ind1]):
            ind1 = k
    ind2 = -1 
    for k in range(len(arr)):
        if (k != ind1) & ((ind2==-1) | (arr[k] > arr[ind2])):
            ind2 = k
    
    return arr[ind1] * arr[ind2]
	
n = int(sys.stdin.readline())
input = sys.stdin.read()
arr = [int(x) for x in input.split()]

print(maxPairProduct(arr))
