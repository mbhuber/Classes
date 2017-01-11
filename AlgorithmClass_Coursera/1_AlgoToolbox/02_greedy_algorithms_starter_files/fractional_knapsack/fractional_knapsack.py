# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.

    wv = [x[0]/x[1] for x in zip(values,weights)]

    isPicked = [0]*len(values)
    while(capacity>0) & (min(isPicked)==0):

    	max_wv= 0
    	midx =-1

    	for k in range(len(wv)):
    		if (wv[k] > max_wv) & (not isPicked[k]):
    			max_wv = wv[k]
    			midx = k
    	isPicked[midx]=1

    	if capacity>=weights[midx]:
    		capacity-=weights[midx]
    		value+=values[midx]
    	else:
    		frac=capacity/weights[midx]
    		value+=frac*values[midx]
    		capacity-=frac*weights[midx]

##    	w = min(weights[midx],capacity)
##    	value+= w*values[midx]/weights[midx]
##    	capacity-=w
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

	#c=1000000
	#w=range(1,1001)
	#v=range(1,1001)
	#print(get_optimal_value(c, w, v))
