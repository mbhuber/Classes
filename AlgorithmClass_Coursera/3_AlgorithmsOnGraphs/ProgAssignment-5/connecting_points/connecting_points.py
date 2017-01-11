#Uses python3
import sys
import math


def minimum_distance(x, y):
    result = 0.
    #write your code here
    edges = calcSortEdges(x,y) # calculate all edges and sort them
    #print(edges)
    mst = kruskal(edges,len(x))
    #print(mst)
    return sum([math.sqrt(k) for k in mst])

def union(d,u,v):
    newVal= d[u]
    oldVal= d[v]
    for k in d.keys():
      if d[k]==oldVal:
        d[k]=newVal
    return d

def kruskal(edges,n):
    # create dict
    d = dict()
    for k in range(n):
      d[k] = k
    x = list()
    for e in edges:
      (u,v) = e[0]
      if d[u] != d[v]:
        x.append(e[1])
        d=union(d,u,v)
    #print('dict:',d)
    return x

def calcSortEdges(x,y):
    n = len(x)
    dist = []
    for i in range(n):
      for j in range(i+1,n):
        d = (x[i]-x[j])**2 + (y[i]-y[j])**2
        dist.append( [(i,j),d])
    return sorted(dist,key=lambda x: x[1])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

#input = '5 0 0 0 2 1 1 3 0 3 2'
i#nput='4 0 0 0 1 1 0 1 1'