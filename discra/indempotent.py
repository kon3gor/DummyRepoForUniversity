from typing import List, Tuple
from collections import Counter
from math import gcd

class NumberFactorizator:

    def factorize(self, n: int) -> List[int]:
        i = 2
        primfac = []
        while i * i <= n:
            while n % i == 0:
                primfac.append(i)
                n = n // i
            i = i + 1
        if n > 1:
            primfac.append(n)
        return primfac

class ModuloRing:

    def __init__(self, size):
        self.size = size
        self.factorization = Counter(NumberFactorizator().factorize(size))

    def countNilpotents(self) -> int:
        x = 1
        for i in self.factorization.keys(): x*=i
        return self.size // x - 1

    def findIndempotents(self) -> List[int]:
        factorization = self._flattenFactorization()
        base = []
        for factor in factorization:
            Ai = self.size // factor
            iRing = ModuloRing(factor)
            rev = iRing.findReversedByMultiply(Ai)
            base.append(Ai * rev)

        powerSet = self._powerSet(base)
        
        return list(sorted(map(lambda x : x % self.size, powerSet)))
        
    def _powerSet(self, set):
        setSize = len(set)
        powerSetSize = 2**setSize
        
        result = [0]*powerSetSize
        for counter in range(powerSetSize):
            for j in range(setSize):
                if((counter & (1 << j)) > 0): result[counter] += set[j]

        result.sort()
        return result
    
    def _flattenFactorization(self) -> List[int]:
        return [k**v for k, v in self.factorization.items()]

    def findReversedByMultiply(self, n: int) -> int:
        g, x, _ = self._gcdex(n, self.size)
        if (g != 1): return -1
        return (x % self.size + self.size) % self.size

    def _gcdex(self, a: int, b: int) -> Tuple[int]: # расширенный алгоритм евклида, решающий диафантово уравнение
        if (a == 0): return (b, 0, 1)
        g, x, y = self._gcdex(b%a, a)
        return (g, y - (b//a)*x, x)

    def phi(self, n):
        amount = 0        
        for k in range(1, n + 1):
            if gcd(n, k) == 1:
                amount += 1
        return amount

    def getMultiplicativeGroupSizes(self) -> List[int]:
        return [ self.phi(i) for i in self._flattenFactorization() ]

    def getFactorization(self) -> List[int]:
        return self.factorization


def from32To10Converter(n: str) -> int:
    r = 0
    for i, l in enumerate(reversed(n)):
        num = ord(l) - ord("А")
        r += num * ( 32**i )

    return r

m = from32To10Converter("САР")
n = from32To10Converter("ИВА")
ring = ModuloRing(n**2)

print(n, m)

t = ring.findReversedByMultiply(m)
print("обратный:", t)

ind = ring.findIndempotents()
print("индемпотенты:", ind)

nilp = ring.countNilpotents()
print("нильпотенты:", nilp)

fac = ring.getFactorization()
print(fac)

mgs = ring.getMultiplicativeGroupSizes()
print(mgs)

a = mgs[0]
b = mgs[1]
c = mgs[2]

lcmAB = (a*b)//gcd(a, b)
lcmAll = (lcmAB*c)//gcd(lcmAB, c)
print(lcmAll)   