#Uses python3

import sys
import queue

def distance(adj, cost, s, t):
    #write your code here
    prev = dikjstra(adj,cost,s)
    path = getPath(s,t,prev)
    return getCost([s]+path,adj,cost)

def dikjstra(adj,cost,s):
    n = len(adj)
    dist=[1e12]*n
    prev=[None for _ in range(n)]
    dist[s]=0

    h=queue.PriorityQueue()
    h.put((dist[s],s))

    while not h.empty():
      d,u = h.get()
      if d<=dist[u]:
        for idx in range(len(adj[u])):
          v = adj[u][idx]
          if dist[v]>dist[u]+cost[u][idx]:
              dist[v]=dist[u]+cost[u][idx]
              prev[v]=u
              h.put((dist[v],v))
    return prev

def getPath(s,u,prev):
    res = []
    while u != s and u!=None:
      res.append(u)
      u=prev[u]
    if u==s:
      res.reverse()
    else:
      res=[]
    return res

def getCost(path,adj,cost):
    if len(path)<2:
      return -1

    c = 0
    while len(path)>1:
      s,t = path[0],path[1]
      idx = adj[s].index(t)
      c+=cost[s][idx]
      path=path[1:]
    return c

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

#input='4 4 1 2 1 4 1 2 2 3 2 1 3 5 1 3' #3
#input='5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 1 5' #6
#input='3 3 1 2 7 1 3 5 2 3 2 3 2' #-1
