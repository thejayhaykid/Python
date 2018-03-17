from turtle import *
side = 60
COUNT = 8

def DrawBox(count,colorcount,side):
    # determine color
    if colorcount%2==0:
        if count % 2 == 1:
            fillcolor('black')
        else:
            fillcolor('red')
    else:
        if count % 2 == 1:
            fillcolor('red')
        else:
            fillcolor('black')
    
    # draw box
    begin_fill()
    for i in range(4):
        forward(side)
        left(90)
    end_fill()

######## main program

# draw row of boxes
def checker(sidelen):
    p=2
    goto(sidelen*-4,sidelen*-4)
    for l in range(COUNT):
        tracer(False)
        for i in range(COUNT):
            DrawBox(i,p,sidelen)
            forward(sidelen)
        p+=1
        up()
        goto(sidelen*-4,(((l+1)*sidelen)+(sidelen*-4)))
        down()
        tracer(True)
checker(side)
