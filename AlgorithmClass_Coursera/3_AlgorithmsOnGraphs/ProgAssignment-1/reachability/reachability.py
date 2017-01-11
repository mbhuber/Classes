#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    cc=DFS(adj)
    return 1 if cc[x]==cc[y] else 0

def DFS(adj):
    visited = [0]*len(adj)
    cc = [-1] * len(adj)
    cnt = 1
    for v in range(len(adj)):
      if not visited[v]:
        visited=explore(v,adj,visited)
        for w in range(len(visited)):
          if visited[w]==1 and cc[w]<1:
             cc[w]=cnt
        #print(cc)
        cnt+=1
    return cc

def explore(v,adj,visited):
    visited[v]=1
    for w in adj[v]:
      if not visited[w]:
        visited=explore(w,adj,visited)
    return visited

if __name__ == '__main__':
    input = sys.stdin.read()
    #input='4 4 1 2 3 2 4 3 1 4 1 4'
    #input='4 2 1 2 3 2 1 4'
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
