 # python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

        def calcDepth(self,depth,k):
        	if self.parent[k]==-1:
        		return 1
        	elif depth[self.parent[k]]>0:
        		return depth[self.parent[k]]+1
        	else:
        		return self.calcDepth(depth,self.parent[k])+1

        def calcHeight(self):
        	depth = [0]*self.n
        	for k in range(self.n):
        		depth[k]=self.calcDepth(depth,k);
        	return max(depth)

def main():
  tree = TreeHeight()
  tree.read()
  #print(tree.compute_height())
  print(tree.calcHeight())

threading.Thread(target=main).start()


##def calcDepth(tree,depth,k):
##	if tree[k]==-1:
##		return 1
##	elif depth[tree[k]]>0:
##		return depth[tree[k]]+1
##	else:
##		return calcDepth(tree,depth,tree[k])+1
##
##def calcHeight(tree):
##	n = len(tree)
##	depth = [0]*n
##	for k in range(n):
##		depth[k]=calcDepth(tree,depth,k);
##
##	#print(depth)
##	return max(depth)