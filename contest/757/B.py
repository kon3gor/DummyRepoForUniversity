t = int(input())

def solve(a, n):
    def maxInd():
        mI = 0
        m = a[0]
        for i in range(1, len(a)):
            if m < a[i]:
                m = a[i]
                mI = i
        return mI+1

    r = [0]*(n+1)
    m = n//2
    r[0] = m
    ind = m
    l1 = ind
    r1 = ind
    t  = 0 
    nextLeft = True
    for _ in range(n):
        l1 -= 1 
        r1 += 1
        if (nextLeft): 
            ind = l1
            nextLeft = False
        else:
            ind = r1
            nextLeft = True
        mI = maxInd()
        t += a[mI-1]*2*abs(r[0] - ind)
        a[mI - 1] = -1
        r[mI] = ind
    return (t, r)


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    r = solve(a, n)
    print("s", r)