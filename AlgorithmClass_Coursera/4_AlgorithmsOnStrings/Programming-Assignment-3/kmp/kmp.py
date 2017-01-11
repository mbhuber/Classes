# python3
import sys

def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  # Implement this function yourself
  plen = len(pattern)
  newStr = pattern+'$'+text
  pf = ComputePrefixFunction(newStr)

  result = []
  for k in range(plen+1,len(newStr)):
    if pf[k]==plen:
      result.append(k-2*plen)
  return result

def ComputePrefixFunction(p):
  n = len(p)
  s = [0]*n
  border = 0
  for i in range(1,n):
    while (border>0) and (p[i]!=p[border]):
      border=s[border-1]
    if p[i]==p[border]:
      border+=1
    else:
      border=0
    s[i]=border
  return s

if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

# pattern = 'TACG'
# text = 'GT'
# result = find_pattern(pattern, text)
# print(" ".join(map(str, result)))

# pattern = 'ATA'
# text = 'ATATA'
# result = find_pattern(pattern, text)
# print(" ".join(map(str, result)))

# pattern = 'ATAT'
# text = 'GATATATGCATATACTT'
# result = find_pattern(pattern, text)
# print(" ".join(map(str, result)))