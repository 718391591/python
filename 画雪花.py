import turtle
def a(size,n):

    if n==0:
        turtle.fd(size)
    else:
        for b in [60,-120,60,0]:
            a(size/2,n-1)
            turtle.left(b)
for i in range(3):
    turtle.right(120)            
    a(100,3)
turtle.speed(0)
