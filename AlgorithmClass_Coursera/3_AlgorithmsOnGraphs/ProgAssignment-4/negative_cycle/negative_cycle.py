#Uses python3

import sys

def negative_cycle(adj, cost):
    #write your code here
    return 1 if hasCycle(adj,cost) else 0

def hasCycle(adj,cost): # using bellman-ford
    n = len(adj)
    dist=[1e12]*n
    prev=[None for _ in range(n)]
    dist[0]=0
    lastUpdate=[]

    for iter in range(n): # #vertices interations
      for u in range(n):  # loop over all edges
        for idx in range(len(adj[u])):
          v = adj[u][idx]
          if dist[v]>dist[u]+cost[u][idx]:
            dist[v]=dist[u]+cost[u][idx]
            prev[v]=u
            if iter == (n-1): # last iteration
              #print('last',v)
              return True
    return False

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
    print(negative_cycle(adj, cost))

#input='4 4 1 2 -5 4 1 2 2 3 2 3 1 1' # 1
#input='4 4 1 2 1 4 1 2 2 3 2 1 3 5'  # 0