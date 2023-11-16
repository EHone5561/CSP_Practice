from simpleai.search import CspProblem, backtrack

variables = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

domains = {
    'S' : [i for i in range(10)],
    'E' : [i for i in range(10)],
    'N' : [i for i in range(10)],
    'D' : [i for i in range(10)],
    'M' : [0, 1],
    'O' : [i for i in range(0,10)],
    'R' : [i for i in range(10)],
    'Y' : [i for i in range(10)]
}

def constraints1(variables, values):
    if values[0] + values[1] < 10:
        return (values[0] + values[1] == values[2])
    else:
        return (values[0] + values[1] - 10 == values[2])

def constraints2(variables, values):
    if values[0] + values[1] < 10:
        if values[2] + values[3] < 10:
            return (values[2] + values[3] == values[0])
        elif values[2] + values[3] >= 10:
            return (values[2] + values[3] - 10 == values[0])
    else:
        if (values[2] + values[3] >= 9):
            return (values[2] + values[3] - 9 == values[0])
        elif (values[2] + values[3] < 9):
            return (values[2] + values[3] + 1 == values[0])
        
def constraints3(variables, values):
    if values[0] + values[1] < 10:
        return (values[0] + values[1] == values[2]) and (values[1] == 0)
    elif values[0] + values[1] >= 10:
        return (values[0] + values[1] - 10 == values[2]) and (values[1] == 1)
    
def constraints4(variables, values):
    for i in range(8):
        for j in range(1+i, 8):
            if values[i] == values[j]:
                return False
            else:
                pass
    return True

constraints = [
    (('D', 'E', 'Y'), constraints1),
    (('S', 'M', 'O'), constraints3),
    (('E', 'D', 'N', 'R'), constraints2),
    (('N', 'R', 'E', 'O'), constraints2),
    (('O', 'E', 'S', 'M'), constraints2),
    (('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'), constraints4)
]

problem = CspProblem(variables, domains, constraints)

print('\nSolutions:\n\nNormal:', backtrack(problem))