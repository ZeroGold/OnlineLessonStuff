def incriment(a):
    return a+1
def square(a):
    return a * a
def findSequence(initial, goal):
    candidates = [(str(initial), initial)]
    for i in range(1, goal-initial+1):
        newCandidates = []
        for (action, result) in candidates:
            for (a,r) in [(' incriment', incriment), (' square', square)]:
                newCandidates.append((action+a,r(result)))
                print(str(i)+" : "+ str(newCandidates[-1]))
                if newCandidates[-1][1] == goal:
                    return newCandidates[-1]
        candidates = newCandidates





answer = findSequence(1,100)
print()
print("Answer")
print(answer)




### Thinking functionally

## Make a function apply then ask for the answer from apply?


def apply(opList, arg):
    if len(opList) == 0:
        return arg
    else:
        return apply(opList[1:],opList[0](arg))



print(apply([square,square],7))

## We now have a function that can apply our functions to objects within our enviornment
