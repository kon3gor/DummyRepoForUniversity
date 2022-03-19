t = int(input())

def f(a, b):
    if (a == b): return a//2
    x = max(a, b)
    y = min(a, b)

    return min((x - y)//2, y)


for i in range(t):
    a, b = map(int, input().split())
    print(f(a, b))