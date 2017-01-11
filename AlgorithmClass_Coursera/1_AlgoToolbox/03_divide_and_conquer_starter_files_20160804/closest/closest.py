#Uses python3
import sys
import math

##import numpy as np
##import time


def naive(x,y):
	dist = 1e15
	for k in range(len(x)):
		for l in range(k+1,len(x)):
			dx = x[k]-x[l]
			dy = y[k]-y[l]
			d = dx*dx + dy*dy
			if d<dist:
				dist=d
	return math.sqrt(dist)

def distFunc(p1,p2):
	dx,dy=p1[0]-p2[0],p1[1]-p2[1]
	return math.sqrt(dx*dx+dy*dy)

def crossDist(points,mdist,left,mid,right):
	#consider only points within mdist distance
	# for l in range(left,mid+1):
	# 	if ((points[mid][0]-points[l][0])<mdist):
	# 		for r in range(mid+1,right+1):
	# 			if (points[r][0]-points[mid][0])<mdist:
	# 				d = distFunc(points[l],points[r])
	# 				if d<mdist:
	# 					mdist=d

	l=mid
	while( (l>=left) and ((points[mid][0]-points[l][0])<mdist)):
		r = mid+1
		while((r<=right) and ((points[r][0]-points[mid][0])<mdist)):
			#d = distFunc(points[l],points[r])
			dx,dy=points[l][0]-points[r][0],points[l][1]-points[r][1]
			d=math.sqrt(dx*dx+dy*dy)
			if d<mdist:
				mdist=d
			r+=1
		l-=1
	return mdist


def minDist(points,left,right):
	if left>=right: # 0 or 1 point
		return 1e15;
	if left+1==right: # 2 points
		#dx,dy=points[left][0]-points[right][0],points[left][1]-points[right][1]
		#return math.sqrt(dx*dx+dy*dy)
		return distFunc(points[left],points[right])
	mid = left+int((right-left)/2)
	ld = minDist(points,left,mid)
	rd = minDist(points,mid+1,right)

	return crossDist(points,min(ld,rd),left,mid,right)

def calcVar(arr):
	mean = sum(arr)/len(arr)
	return sum([(x-mean)**2 for x in arr])

def minimum_distance(x, y):
	if len(x)==1:
		return 0
	#points = sorted([t for t in zip(x,y)])
	if calcVar(x)>calcVar(y):
		points = sorted([t for t in zip(x,y)])
	else:
		points = sorted([t for t in zip(y,x)])
	return minDist(points,0,len(points)-1)

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	x = data[1::2]
	y = data[2::2]
	print("{0:.9f}".format(minimum_distance(x, y)))

    # test
##    np.random.seed(1234)
##    n=10000
##    rg = int(1e5)
##    x = np.random.choice(range(-rg,rg), n)
##    y = np.random.choice(range(-rg,rg), n)
##    st = time.time()
##    print("{0:.9f}".format(minimum_distance(x, y)))
##    print("time:",time.time()-st)
##    x = [5,3,2,6]
##    y = [0,4,0,0]
##    print("{0:.9f}".format(minimum_distance(x, y)))

# x = [5,3,2,6]
# y = [0,4,0,0]
# print("{0:.9f}".format(minimum_distance(x, y)))
# print("{0:.9f}".format(naive(x, y)))


# x = [4,-2,-3,-1,2,-4,1,-1, 3,-4,-2]
# y = [4,-2,-4, 3,3, 0,1,-1,-1, 2, 4]
# print("{0:.9f}".format(minimum_distance(x, y)))
# print("{0:.9f}".format(naive(x, y)))

# print()
# x=[-83,-21,-61,76]
# y=[-76,-31,38,-43]
# print("{0:.9f}".format(minimum_distance(x, y)))
# print("{0:.9f}".format(naive(x, y)))

# print()
# x=[-69,-69,26]
# y=[-22,83,11]
# print("{0:.9f}".format(minimum_distance(x, y)))
# print("{0:.9f}".format(naive(x, y)))


print()
# np.random.seed(1234)
# random.seed(123)
# cnt=1
# while(cnt<100000):
# 	n=random.randint(2,10)
# 	rg = int(1e2)
# 	x = np.random.choice(range(-rg,rg), n)
# 	y = np.random.choice(range(-rg,rg), n)
# 	if (minimum_distance(x, y)!=naive(x, y)):
# 		print("Failed:",cnt)
# 		print(x)
# 		print(y)
# 	if (cnt%10000==0):
# 		print("step:",cnt)
# 	cnt+=1
#np.random.seed(1234)
#n=100000
#rg = int(1e5)
#x = np.random.choice(range(-rg,rg), n)
#y = np.random.choice(range(-rg,rg), n)
#st = time.time()
#print("{0:.9f}".format(minimum_distance(x, y)))
#print("time:",time.time()-st)

# st = time.time()
# print("{0:.9f}".format(naive(x, y)))
# print("time:",time.time()-st)