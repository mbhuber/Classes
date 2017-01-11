#Uses python3
import sys
import math

def clustering(x, y, k):
    result = 0.
    #write your code here
    edges = calcSortEdges(x,y) # calculate all edges and sort them
    #print(edges)
    d = kruskal(edges,len(x),k)
    return math.sqrt(d)

def union(d,u,v):
    newVal= d[u]
    oldVal= d[v]
    for k in d.keys():
      if d[k]==oldVal:
        d[k]=newVal
    return d

def kruskal(edges,n,nclust):
    # create dict
    d = dict()
    for k in range(n):
      d[k] = k
    x = list()
    for idx in range(len(edges)):
      e = edges[idx]
      (u,v) = e[0]
      if d[u] != d[v]:
        x.append(e[1])
        d=union(d,u,v)
        if len(set(d.values()))<nclust:
          #print(set(d.values()))
          break
    #print(edges[idx:idx+5])
    return edges[idx][1]

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
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

#input='12 7 6 4 3 5 1 1 7 2 7 5 7 3 3 7 8 2 8 4 4 6 7 2 6 3'
#input='8 3 1 1 2 4 6 9 8 9 9 8 9 3 11 4 12 4'