# python3
import sys

def BWT(text):
    n= len(text)
    mat = [text] # bwt matrix
    for k in range(1,n):
      text = text[1:]+text[0]
      mat.append(text)
    lastCol = list(map(lambda x:x[-1],sorted(mat))) # sort and last element in each row
    return ''.join(lastCol)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))


# text='AA$'
# print(BWT(text))
# text='ACACACAC$'
# print(BWT(text))
# text='AGACATA$'
# print(BWT(text))