import turtle

turtle.shape("turtle")

def koch(dl,gl):
    if gl==0:
        turtle.forward(dl)
    else:
        koch(dl/3,gl-1)
        turtle.left(60)
        koch(dl/3,gl-1)
        turtle.right(120)
        koch(dl / 3, gl - 1)
        turtle.left(60)
        koch(dl / 3, gl - 1)



def snezxhinka(d,g):
    for i in range(3):
        koch(d,g)
        turtle.right(120)



#koch(300,3)
snezxhinka(300,1)
turtle.done()

