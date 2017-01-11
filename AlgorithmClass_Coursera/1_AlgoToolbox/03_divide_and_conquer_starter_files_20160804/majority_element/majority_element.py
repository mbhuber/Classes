# Uses python3
import sys

def countElement(a,left, right,ele):
	cnt,k= 0,left
	while(k<right):
		if a[k]==ele:
			cnt+=1
		k+=1
	return cnt

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    mid = left + int((right-left)/2)
    leftMajor  = get_majority_element(a, left, mid)
    rightMajor = get_majority_element(a, mid, right)
    # both no majority
    if (leftMajor==-1) & (rightMajor==-1):
    	return -1
    # both majority
    if (leftMajor>-1) & (rightMajor>-1):
    	lcnt = countElement(a,left,right,leftMajor)
    	rcnt = countElement(a,left,right,rightMajor)
    	if lcnt>(right-left)/2:
    		return leftMajor
    	if rcnt>(right-left)/2:
    		return rightMajor
    # only left majority
    if (leftMajor>-1) & (rightMajor==-1):
    	cnt = countElement(a,left,right,leftMajor)
    	if cnt >(right-left)/2:
    		return leftMajor
    # only right majority
    if (rightMajor>-1) & (leftMajor==-1):
    	cnt = countElement(a,left,right,rightMajor)
    	if cnt >(right-left)/2:
    		return rightMajor
    return -1

def moore(a):
	i,k=0,0
	m=a[0]
	while(k<len(a)):
		if i==0:
			m=a[k]
		if m==a[k]:
			i+=1
		else:
			i-=1
		k+=1
	# verify
	k,cnt=0,0
	while(k<len(a)):
		if a[k]==m:
			cnt+=1
		k+=1
	if cnt<=len(a)/2:
		return -1
	else:
	    return m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
#    if moore(a) != -1:
        print(1)
    else:
        print(0)
