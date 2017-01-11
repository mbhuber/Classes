# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else:
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  else:
    # Zig-zag
    smallRotation(v);
    smallRotation(v);

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v
    last = v
    if v.key == key:
      break
    if v.key < key:
      v = v.right
    else:
      v = v.left
  root = splay(last)
  return (next, root)

def split(root, key):
  (result, root) = find(root, key)
  if result == None:
    return (root, None)
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)


def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right


# Code that uses splay tree to solve the problem

root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)
  root = merge(merge(left, new_vertex), right)

##def erase(x):
##  global root
##  # Implement erase yourself
##  pass

def erase(key):
  global root
  #print('erase', key)
  (left, right) = split(root, key)

  if right is None:
      root= left
  else:
      if right.right is not None:
          right.right.parent = None
      root= merge(left, right.right)

def search(x):
  global root
  #print('search', x)
  # Implement find yourself
  (next,root) = find(root,x)
  if next == None or next.key != x:
    return False
  else:
    return True

def sum(fr, to):
  global root
  #print('range',fr,to)
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  ans = 0
  if middle is not None:
      ans=middle.sum
  root=merge(merge(left,middle),right)
  return ans

def sum2(fr, to):
  global root
  #print('range',fr,to)
  #inOrder()
  (left, middle) = split(root, fr)
  if middle==None:
    ans=0
    root=merge(left,middle)
  else:
    (middle, right) = split(middle, to + 1)
    if middle==None:
      ans=0
    else:
      ans= middle.sum
    root=merge(left,merge(middle,right))
  #printNode(middle)
  #printNode(root)
  #root=merge(left,merge(middle,right))
  #root=splay(root)
  #printNode(root)
  return ans

def printNode(n):
  print('key',n.key,' sum', n.sum,' ',n.left,' ',n.right,' ',n.parent)

def inOrderPrint(node,out):
  if node==None:
    return out
  out = inOrderPrint(node.left,out)
  out.append(node.key)
  out = inOrderPrint(node.right,out)
  return out

def inOrder():
  global root
  result = inOrderPrint(root,[])
  print(result,' ')

MODULO = 1000000001


#lines =['? 1','+ 1','? 1','+ 2','s 1 2','+ 1000000000','? 1000000000','- 1000000000','? 1000000000','s 999999999 1000000000','- 2','? 2','- 0','+ 9','s 0 9']
# lines =['? 1','+ 1','? 1','- 1','? 1','? 2','+ 2','? 2','- 3','+ 4','+ 5','s 2 4','s 3 4','s 1 5']
#lines =['+ 1','+ 2','+ 3','+ 4','+ 5','- 5']
#lines=['+ 491572259','? 491572259','? 899375874','s 310971296 877523306','+ 352411209']
#lines=['s 88127140 859949755','s 407584225 906606553','+ 885530090','+ 234423189','s 30746291 664192454','+ 465752492','s 848498590 481606032','+ 844636782','+ 251529178','+ 182631153']
#lines=['s 40279559 89162572','- 774613289','s 869592654 915517087','- 165280355','- 776346290','-221187096','s 421986248 742826969','s 83228103 852190011','- 640319482','? 528689193','? 75245219','- 617070033','+ 66257759','s 25751289 70170547','s 28248247 617849094','- 954357244','+ 477444954','? 608389416','s 400483980 423330836','- 477444954','? 441393551','s 66257759 66257759','- 822218158','? 806479414','s 548665149 925635534','s 66257759 66257759','? 234121006','+ 663305907','s 314809050 685231317','- 0','s 487458874 602635501','s 66257759 66257759','? 918193520','? 606474691','s 188185089 774086933','- 322445571','s 66257759 66257759','- 814123984','s 0 0','s 0 0','s 689260392 827869844','? 204276815','- 66257759','? 488766408','s 412617563 631410280','- 463415495','+ 601030115','? 776513589','s 257003372 887483600','+ 154047223','? 154047223','? 219327735','+ 978812473','s 978812473 154047223','? 718062555','? 128066784','- 15718305','? 754978417','s 643892549 819127300','? 192401474','? 643892549','+ 638898307','? 973173529','+ 506709268','- 506709268','+ 744166533','- 638898307','+ 95240753','s 997348833 63778002','? 31190791','s 21011834 570648768','+ 217208615','+ 401912531','s 0 723886547','? 251082460','+ 542593404','s 702430665 542593404','? 48285749','s 831077135 671239874','+ 917941607','? 908494561','? 671239874','s 333354822 490605331','+ 261522346','s 170201520 10364259','- 139162050','- 677374727','? 992422786','? 500171144','- 239436034','+ 556867643','? 992422786','+ 720003678','s 220110584 268880636','s 31190791 997548180','s 898610232 383552107','- 682670734','+ 547596765','s 496810115 875859347','? 41728941']
#n=len(lines)


n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  #line = lines[i].split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO