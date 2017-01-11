# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optWeight(W,weights):
	nw = len(weights)
	value=[[0]*(nw+1) for _ in range(W+1)]

	for i in range(1,nw+1):
		for w in range(1,W+1):
			value[w][i]=value[w][i-1]
			if weights[i-1]<=w:
				val = value[w-weights[i-1]][i-1]+weights[i-1]
				if value[w][i]<val:
					value[w][i]=val
	#for line in value:
	#	print(line)
	return value[W][nw]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #print(optimal_weight(W, w))
    print(optWeight(W, w))

##    print(optWeight(10,[1,4,8]))
