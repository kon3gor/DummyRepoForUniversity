t = int(input())

def g(p):
    a = []
    i = 0 
    j = len(p) - 1
    while i <= j:
        l = p[i]
        r = p[j]
        if l < r:
            a.insert(0, l)
            p = p[i+1:]
        else:
            a.append(r)
            p = p[:j]
        j-=1
    return a

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    m = max(p)
    if p[0] != m and p[-1] != m: print(-1)
    else: print(*p[::-1])
