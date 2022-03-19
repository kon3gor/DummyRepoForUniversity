t = int(input())

def f(b, p):
    pw = [0 for _ in range(len(b))]
    if b[p[0]] != p[0]: return [-1]
    
    def goup(to):
        r = 0
        j = to
        while b[j] != j:
            r += pw[j]
            j = b[j]
        return r

    c = 1
    for i in p[1:]:
        c += goup(i) + 1
        pw[i] = c
    return pw


for _ in range(t):
    n = input()
    b = list(map(lambda x: int(x) - 1, input().split()))
    p = list(map(lambda x: int(x) - 1, input().split()))
    print(*f(b, p))
