# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def readTree(self,n,data):
    self.n = n
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = data[i]
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrderPrint(self,idx,out):
    if idx==-1:
      return out
    out = self.inOrderPrint(self.left[idx],out)
    out.append(self.key[idx])
    out = self.inOrderPrint(self.right[idx],out)
    return out

  def inOrder(self):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.result = self.inOrderPrint(0,[])
    return self.result

  def preOrderPrint(self,idx,out):
    if idx==-1:
      return out
    out.append(self.key[idx])
    out = self.preOrderPrint(self.left[idx],out)
    out = self.preOrderPrint(self.right[idx],out)
    return out

  def preOrder(self):
    self.result = self.preOrderPrint(0,[])
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.result

  def postOrderPrint(self,idx,out):
    if idx==-1:
      return out
    out = self.postOrderPrint(self.left[idx],out)
    out = self.postOrderPrint(self.right[idx],out)
    out.append(self.key[idx])
    return out

  def postOrder(self):
    self.result = self.postOrderPrint(0,[])
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

##	n=5
##	data=[[4, 1, 2],[2,3,4],[5,-1,-1],[1,-1,-1],[3,-1,-1]]
##	tree = TreeOrders()
##	tree.readTree(n,data)
##	print(" ".join(str(x) for x in tree.inOrder()))
##	print(" ".join(str(x) for x in tree.preOrder()))
##	print(" ".join(str(x) for x in tree.postOrder()))
threading.Thread(target=main).start()
