#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    return bfsCheck(adj)

def bfsCheck(adj):
    n=len(adj)
    dist=[-1]*n
    dist[0]=0
    q = queue.Queue()
    q.put(0)

    while not q.empty():
      u = q.get()
      for v in adj[u]:
        if dist[v]==-1:
          q.put(v)
          dist[v]=(1 if dist[u]==0 else 0)
        elif dist[v]==dist[u]:
          return 0
    return 1

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
    print(bipartite(adj))

#input='4 4 1 2 4 1 2 3 3 1'
#input='5 4 5 2 4 2 3 4 1 4'