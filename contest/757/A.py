t = int(input())

# n - кол-во плиток
# l - мин цена норм шоколадки
# r - макс цена норм шоколадки
# k - макс цена за шоколадку
# a - цены шоколадок
def solve(l, r, k, a):
    s = sorted(filter(lambda x: x in range(l, r+1), a))
    c = 0
    while c < len(s) and  k - s[c] >= 0:
        k -= s[c]
        c += 1


    return c


for _ in range(t):
    n, l, r, k = map(int, input().split())
    a = list(map(int, input().split()))

    r = solve(l, r, k, a)
    print(r)