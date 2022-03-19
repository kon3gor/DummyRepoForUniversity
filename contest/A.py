t = int(input())

def f(n):
    intN = int(n)
    if (intN%2 == 0): return 0
    for i, s in enumerate(n):
        intS = int(s)
        if intS%2 == 0 and i == 0: return 1
        elif intS%2 == 0: return 2
    return -1


for i in range(t):
    n = input()
    print(f(n))