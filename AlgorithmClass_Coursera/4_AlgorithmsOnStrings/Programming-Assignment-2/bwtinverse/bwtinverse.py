# python3
import sys

def InverseBWT(bwt):
    nele = len(bwt)
    # create order and first column
    last=[]
    order=dict()
    for ch in bwt:
      order[ch]= order.get(ch,0) +1
      last.append(ch+str(order[ch]).zfill(6)) # pad order string with zeros
    first = dict( zip(sorted(last),range(nele)) )

    # reconstruct
    idx = 0
    res = [min(last)]
    while len(res)<nele:
      res.append(last[idx])
      idx = first[last[idx]]
    res.reverse()
    res= list(map(lambda x:x[0],res ))
    return "".join(res)

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))

# bwt='CCCC$AAAA'
# print(InverseBWT(bwt))
# bwt='AC$A'
# print(InverseBWT(bwt))
# bwt='AGGGAA$'
# print(InverseBWT(bwt))