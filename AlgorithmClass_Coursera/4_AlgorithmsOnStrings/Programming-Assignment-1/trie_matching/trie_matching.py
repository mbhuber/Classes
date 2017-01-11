# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def build_trie(patterns):
    tree = dict()
    # write your code here
    tree[0]=dict()
    nodeCnt = 0
    for pattern in patterns:
      currentNode = 0
      for ch in pattern:
        if ch in tree[currentNode]:
          currentNode=tree[currentNode][ch]
        else:
          nodeCnt+=1 # new node
          tree[nodeCnt]=dict()
          tree[currentNode][ch]=nodeCnt
          currentNode=nodeCnt
    return tree

def prefixTrieMatching(text,trie):
  l = len(text)
  ch, idx = text[0], 0
  node = trie[0]
  while True:
    if ch in node and len(trie[node[ch]])==0: # leaf
      return True
    elif ch in node:
      node = trie[node[ch]]
      idx +=1
      if idx>l-1:
        return False
      else:
        ch = text[idx]
    else:
      return False

def trieMatching(text,trie):
  res =[]
  for pos in range(len(text)):
    if prefixTrieMatching(text[pos:],trie):
      res.append(pos)
  return res

def solve (text, n, patterns):
  result = []
  # write your code here
  trie = build_trie(patterns)
  return trieMatching(text,trie)


text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')

# text = 'AATCGGGTTCAATCGGGGT'
# n=2
# patterns = ['ATCG','GGGT']

# text = 'AA'
# n=1
# patterns = ['T']

# text = 'AAA'
# n=1
# patterns = ['AA']

