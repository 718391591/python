from decimal import Decimal as D
from time import clock
from decimal import getcontext

getcontext().prec = 1000
a = [D(1.0)] * 1000
pi = [D(1.0)] * 1000
a[1] = D(0.5)
for i in range(1,999):
    a[i+1] = a[i].sqrt() / 2 + D(0.5)
pi[0] = D(0.0)
for i in range(1,1000):
    pi[i] = (1-a[i]).sqrt() * (2 ** (i+1))
    if pi[i] < pi[i-1]:
        break
    print(i, pi[i])

print(clock())
