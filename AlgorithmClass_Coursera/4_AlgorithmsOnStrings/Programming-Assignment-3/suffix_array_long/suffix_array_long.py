# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  # Implement this function yourself
  order = sortCharacters(text)
  classes = ComputeCharClasses(text,order)

  L=1
  while L < len(text):
    order = SortDoubled(text,L,order,classes)
    classes = UpdateClasses(order,classes,L)
    L = 2*L
  return order

def UpdateClasses(newOrder,classes,L):
  n = len(newOrder)
  newClass = [-1]*n
  newClass[newOrder[0]]=0
  for i in range(1,n):
    cur, prev =newOrder[i], newOrder[i-1]
    mid= (cur + L) % n
    midPrev = (prev + L) % n
    if (classes[cur] != classes[prev] or
       classes[mid] != classes[midPrev]):
      newClass[cur] = newClass[prev] + 1
    else:
      newClass[cur] = newClass[prev]
  return newClass

def SortDoubled(S,L,order,classes):
  n = len(S)
  count = [0]*n
  newOrder = [-1]*n
  for i in range(n):
    count[classes[i]] += 1
  for i in range(1,n):
    count[i] += count[i-1]
  for i in range(n-1,-1,-1):
    start = (order[i]-L+n) % n
    cl = classes[start]
    count[cl] -= 1
    newOrder[count[cl]]=start
  return newOrder

def ComputeCharClasses(S,order):
  n = len(S)
  classes = [-1]*n
  classes[order[0]]=0
  for i in range(1,n):
    if S[order[i]]!=S[order[i-1]]:
      classes[order[i]]=classes[order[i-1]]+1
    else:
      classes[order[i]]=classes[order[i-1]]
  return classes

def sortCharacters(S):
  n = len(S)
  nlett = 5
  order = [-1]*n
  count = [0]*nlett # # letters
  letterMap = {'$':0,'A':1,'C':2,'G':3,'T':4} # map from letter to array position
  for i in range(n):
    count[letterMap[S[i]]] += 1
  for i in range(1,nlett):
    count[i] += count[i-1]
  for i in range(n-1,-1,-1):
    c = letterMap[S[i]]
    count[c] -=1
    order[count[c]]=i
  return order



if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))

##  # tests
##  text = 'AAA$'
##  print(text)
##  print(" ".join(map(str, build_suffix_array(text))))
##
##  # tests
##  text = 'GAC$'
##  print(text)
##  print(" ".join(map(str, build_suffix_array(text))))
##
##  # tests
##  text = 'GAGAGAGA$'
##  print(text)
##  print(" ".join(map(str, build_suffix_array(text))))
##
##    # tests
##  text = 'AACGATAGCGGTAGA$'
##  print(text)
##  print(" ".join(map(str, build_suffix_array(text))))