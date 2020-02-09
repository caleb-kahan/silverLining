from display import *
from draw import *

def main():
    s = new_screen()
    c = [255,255,255]
    for i in range(YRES):
        for j in range(XRES):
            plot(s,c,j,i)
    editImage(s)
    display(s)
    save_ppm(s, 'binary.ppm')
    save_ppm_ascii(s, 'ascii.ppm')
    save_extension(s, 'img.png')

def editImage(image):
    c=[180,180,180]
    for i in range(0,YRES,YRES//20):
        if(i==YRES/2):
            continue
        c=[180,180,180]
        draw_line(0, i, XRES-1, i, image, c);
        draw_line(i,0,i,YRES-1,image,c)
        c=[0,0,0]
        draw_line(XRES//2-5, i, XRES//2+5, i, image, c);
        draw_line(i,YRES//2-5,i,YRES//2+5,image,c)
    c = [0,0,0]
    for i in range(-2,2):
        draw_line(0, i+YRES//2, XRES-1, i+ YRES//2, image, c);
        draw_line(i+XRES//2, 0, i+XRES//2, YRES-1, image, c);
    c=[255,0,0]
    for i in range(1,XRES):
        actualX = i - XRES//2
        if actualX-1 == 0 or actualX+1==0:
            continue
        draw_line(i-1,(500//(actualX-1))+YRES/2,i+1,(500//(actualX+1))+YRES//2,image,c)


def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
main()
