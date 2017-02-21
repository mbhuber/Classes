# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column] or \
          abs(a[pivot_element.row][pivot_element.column])<EPS:
        pivot_element.column += 1
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    nrow = len(a)
    ncol = len(a[pivot_element.row])
    pivot = a[pivot_element.row][pivot_element.column]

    # rescale pivot to 1
    for col in range(ncol):
        a[pivot_element.row][col]/= 1.*pivot
    b[pivot_element.row]/=1.*pivot

    #PrintEquation(a,b)

    # substract pivot row from others to make other entries zero
    for row in range(nrow):
        if row!=pivot_element.row and abs(a[row][pivot_element.column])>EPS:
            factor = 1.*a[row][pivot_element.column]/a[pivot_element.row][pivot_element.column]

            for col in range(ncol):
                a[row][col]-= factor * a[pivot_element.row][col]
            b[row] -= factor * b[pivot_element.row]


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        #print('step: '+str(step))
        pivot_element = SelectPivotElement(a, used_rows, used_columns)

        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)


        #PrintEquation(a,b)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def PrintColumn(column):
    size = len(column)
    res = ''
    for row in range(size):
        #print("%.6lf" % column[row])
        res+="%.6lf " % column[row]
    print(res)

def PrintEquation(a,b):
    size = len(b)
    for row in range(size):
        print(a[row],b[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)

##    equation = Equation([[1,0,0,0],[0,0,0,1],[0,1,0,0],[0,0,1,0]],[1,3,5,8])
##    solution = SolveEquation(equation)
##    PrintColumn(solution)
##
##    equation = Equation([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],[1,5,4,3])
##    solution = SolveEquation(equation)
##    PrintColumn(solution)
##
##    equation = Equation([[1,1],[2,3]],[3,7])
##    solution = SolveEquation(equation)
##    PrintColumn(solution)
##
##    equation = Equation([[5,-5],[-1,-2]],[-1,-1])
##    #PrintEquation(equation.a,equation.b)
##    solution = SolveEquation(equation)
##    PrintColumn(solution)

    exit(0)
