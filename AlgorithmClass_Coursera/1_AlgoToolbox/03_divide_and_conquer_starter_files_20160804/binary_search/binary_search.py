# Uses python3
import sys

def BinarySearch(a,low,high,key):
	if high<low:
		return -1
	mid = low + int((high-low)/2)
	if (key==a[mid]):
		return mid
	elif key<a[mid]:
		return BinarySearch(a,low,mid-1,key)
	else:
		return BinarySearch(a,mid+1,high,key)

def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    return BinarySearch(a,left,right,x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
