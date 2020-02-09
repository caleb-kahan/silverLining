from display import *
from draw import *

def main():
    s = new_screen()
    c = [255,255,255]
    for i in range(YRES):
        for j in range(XRES):
            plot(screen,c,j,i)
    editImage(image)
    display(s)
    save_ppm(s, 'binary.ppm')
    save_ppm_ascii(s, 'ascii.ppm')
    save_extension(s, 'img.png')

def editImage(image):
    c = [0,0,0]
    draw_line(0, YRES//2, XRES-1, YRES//2, image, c);
    draw_line(XRES//2, 0, XRES//2, YRES-1, image, c);

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
main()
