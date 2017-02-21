# python3
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]

#test 1:
#n, m = 3,3
#clauses =[[1, -3],[-1, 2],[-2,-3]]

# test 2:
#n,m =1,2
#clauses = [[1,1],[-1,-1]]

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def isSatisfiable():
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]

        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

def assignVariable(F,result):
    idx = len(result)-1
    newF=[]
    for clause in F:
        if len(clause)==1:
            if abs(clause[0])-1 != idx:
                newF.append(clause)
            else:
                if result[idx]!=(clause[0]<0):
                    newF.append([])
        else:
            if abs(clause[0])-1 == idx:
                if result[idx]!=(clause[0]<0):#result[idx]==0:
                    if abs(clause[1])-1 != idx:
                        newF.append([clause[1]])
                    else:
                        if result[idx]!=(clause[1]<0):
                            newF.append([])
            elif abs(clause[1])-1 == idx:
                if result[idx]!=(clause[1]<0):#result[idx]==0:
                    newF.append([clause[0]])
            else:
                newF.append(clause)
    return newF

def SolveSAT(F,result):
    if len(F)==0:
        return result
    for clause in F:
        if len(clause)==0:
            return None

    newResult = result+[0]
    newResult = SolveSAT(assignVariable(F,newResult),newResult)
    if newResult != None:
        return newResult

    newResult = result+[1]
    newResult = SolveSAT(assignVariable(F,newResult),newResult)
    if newResult != None:
        return newResult

    return None

#result = isSatisfiable()
result = SolveSAT(clauses,[])

if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE");
    print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))

#res = SolveSAT(clauses,[])
#print(res)

##a,b = assignVariable(clauses,[1])
##print a
##
##a,b = assignVariable(a,[1,1])
##print a
##
##a,b = assignVariable(a,[0,0,0])
##print a
