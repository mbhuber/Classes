#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    prev = bfs(adj,s)
    path = getPath(s,t,prev)
    return (len(path) if len(path)>0 else -1)

def bfs(adj,s):
    n=len(adj)
    inf = 1e10
    dist=[inf]*n
    prev=[None for _ in range(n)]

    dist[s]=0
    q = queue.Queue()
    q.put(s)

    while not q.empty():
      u = q.get()
      for v in adj[u]:
        if dist[v]==inf:
          q.put(v)
          dist[v]=dist[u]+1
          prev[v]=u
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

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

#input='4 4 1 2 4 1 2 3 3 1 2 4'
#input='5 4 5 2 1 3 3 4 1 4 3 5'