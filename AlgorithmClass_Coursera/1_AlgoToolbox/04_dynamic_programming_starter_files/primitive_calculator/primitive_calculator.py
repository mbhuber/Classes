# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def opfunc(x,op):
	if op==1:
		return x-1
	if op==2:
		return x/2
	if op==3:
		return x/3

def opfunc2(x,op):
	if op==1:
		return x+1
	if op==2:
		return x*2
	if op==3:
		return x*3

def reconstruct(arr):
	n = len(arr)
	res = [n-1]
	k=n-1
	while(k>1):
		k=int(opfunc(k,arr[k]))
		res.append(k)
	res.reverse()
	return res

def func(n):
	minNumOp = [1e15]*(n+1)
	minNumOp[:2] = [0,0]
	res = [0,1]
	for k in range(2,n+1):
		for op in range(1,4):
			if (opfunc(k,op)>=1) and (opfunc(k,op)%1==0):
				numOp = minNumOp[int(opfunc(k,op))]+1
				if numOp<minNumOp[k]:
					minNumOp[k]=numOp
					minOp = op

		res.append(minOp)
	return minNumOp[n], res

def optSeq(n):
	op,res = func(n)
	return reconstruct(res)

input = sys.stdin.read()
n = int(input)
#sequence = list(optimal_sequence(n))
sequence = list(optSeq(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

#print(sequence)

# seq = optSeq(1)
# print(len(seq)-1)
# print(seq,end=' ')

# print()
# seq = optSeq(6)
# print(len(seq)-1)
# print(seq,end=' ')

# print()
# op, res = func(96234)
# seq = optSeq(96234)
# print(len(seq)-1)
# print(seq,end=' ')

# print()
# seq = optSeq(100000)
# print(len(seq)-1)
# print(seq,end=' ')