import random
from time import clock
total=1000000
NumberOfcircle=0
clock()
for i in range(total):
    x=random.random()
    y=random.random()
    distance=x*x+y*y
    if distance<=1:
        NumberOfcircle=NumberOfcircle+1
pi=NumberOfcircle/total*4
print(clock())
print(pi)
