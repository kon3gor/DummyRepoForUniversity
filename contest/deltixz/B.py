n, q = map(int, input().split())

s = input()

def rabinKarp(s, n):
    print("processing", s)
    def hash(s):
        p = 3
        r = 0
        for i in range(len(s)):
            r += p**i * ord(s[i])
        return r

    ans = []
    m = 3
    p = 3 
    hashS = hash(s[0:m])
    hashW = hash("abc")

    for i in range(n-m):
        if hashS == hashW: ans.append(i)

        hashS = (p * hashS - 27* hash(s[i]) + hash(s[i+m]) )

    return ans

for _ in range(q):
    ind, ch = input().split()
    newS = list(s)
    newS[int(ind)-1] = ch
    r = rabinKarp(newS, n)
    print("answer", r)

