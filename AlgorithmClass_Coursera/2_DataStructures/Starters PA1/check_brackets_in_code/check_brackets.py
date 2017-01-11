# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    #text = 'foo(bar[i);'

    opening_brackets_stack = []
    isSuccess = True
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)<1:
                isSuccess=False
                break
            else:
                cb = opening_brackets_stack.pop()

            if not cb.Match(next):
                isSuccess=False
                break

    # Printing answer, write your code here
    if not isSuccess:
        print(i+1)
    elif len(opening_brackets_stack)>0:
        while len(opening_brackets_stack)>0:
            b = opening_brackets_stack.pop()
        print(b.position+1)
    else:
        print("Success")
