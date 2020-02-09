from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #Always draw left from right
    if x1-x0<0:
        x0,y0,x1,y1=x1,y1,x0,y0
    x0,y0,x1,y1=round(x0),round(y0),round(x1),round(y1)
    A = y1-y0
    B = -(x1-x0)
    x = x0
    y = y0
    if(B==0):
        QuadVersionY(x,y,y1,A,B,screen,color)
        return;
    if abs(A/B)<1:
        #QUAD
        QuadVersionX(x,y,x1,A,B,screen,color)
    else:
        QuadVersionY(x,y,y1,A,B,screen,color)

    pass
def QuadVersionX(x,y,x1,A,B,screen,color):
    D = 2*A+B*sign(A)
    while x<=x1:
        plot(screen,color,x,y)
        if(sign(A)*D>0):
            y+=sign(A);
            D+=2*B*sign(A);
        x+=1
        D+=2*A
    plot(screen,color,x,y)

def QuadVersionY(x,y,y1,A,B,screen,color):
    #print(str(x)+","+str(y))
    D = A+B*2*sign(A)
    while sign(A)*y<=sign(A)*y1:
        plot(screen,color,x,y)
        if(sign(A)*D<0):
            x+=1
            D+=2*A
        y+=sign(A);
        D+=2*B*sign(A)
    plot(screen,color,x,y)

def sign(num):
    if num>0:
        return 1
    if num == 0:
        return 0
    return -1
