import sensor, image, time ,screen
import time
import pyb
from pyb import UART

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(200)
sensor.set_auto_whitebal(False)
sensor.set_auto_gain(False)
sensor.set_auto_exposure(False)
sensor.set_brightness(100)

clock = time.clock()
uart = UART(3, 9600)#4口发送，5口接收
def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob=blob
    return max_blob

red_threshold	= [(94, 31, -59, - 9, -16, 31),(0, 61, -51, -9, -11, 7)]
green_threshold  = (88, 100, 0, 11, -8, 3)
y = 0


def Rxcive():
    if uart.any():
        data = uart.read(10)
        m = int (data)
        return m

while(True):

    x = Rxcive()

    y = x
    img = sensor.snapshot().negate().lens_corr(strength = 1.2, zoom = 1.0)
    #img.b_nor(img_drawing_board)

    if y == 1 :

        #img = sensor.snapshot()
        #img = sensor.snapshot().negate()

        blobs = img.find_blobs(red_threshold)
        img.gaussian(1, unsharp=True)
        if blobs:
            max_blob=find_max(blobs)
            print('sum :', len(blobs))
            img.draw_rectangle(max_blob.rect())
            img.draw_rectangle(max_blob[0:4])
            img.draw_cross(max_blob.cx(), max_blob.cy())
            img.mean(1)
            X = '%03d' % max_blob.cx()
            Y = '%03d' % max_blob.cy()
            DATA = 'F' + X + Y + 'E'
            uart.write(DATA)
            print(DATA)
            print(max_blob.cx(),max_blob.cy())
    if y==2 :
        #img = sensor.snapshot()
        #img = sensor.snapshot().negate()
        for r in img.find_rects(threshold = 10000):
            if 120 > r.w() > 80 and 120 >r.h() > 80 :
                # 在屏幕上框出矩形
                img.draw_rectangle(r.rect(), color = (0, 0, 225), scale = 4)
                # 获取矩形角点位置
                corner = r.corners()
                # 在屏幕上圈出矩形角点
                img.draw_circle(corner[0][0], corner[0][1], 2, color = (0, 225, 0), thickness = 2, fill = False)
                img.draw_circle(corner[1][0], corner[1][1], 2, color = (0, 225, 0), thickness = 2, fill = False)
                img.draw_circle(corner[2][0], corner[2][1], 2, color = (0, 225, 0), thickness = 2, fill = False)
                img.draw_circle(corner[3][0], corner[3][1], 2, color = (0, 225, 0), thickness = 2, fill = False)
                corner1_str = corner1 = corner[0][0],corner[0][1]#角点坐标1左下
                corner2_str = corner2 = corner[1][0],corner[1][1]#角点坐标2右下
                corner3_str = corner3 = corner[2][0],corner[2][1]#角点坐标3右上
                corner4_str = corner4 = corner[3][0],corner[3][1]#角点坐标4左上

                X1 = '%03d' % corner[3][0]
                Y1 = '%03d' % corner[3][1]
                X2 = '%03d' % corner[2][0]
                Y2 = '%03d' % corner[2][1]
                X3 = '%03d' % corner[1][0]
                Y3 = '%03d' % corner[1][1]
                X4 = '%03d' % corner[0][0]
                Y4 = '%03d' % corner[0][1]

                DATA =  'A' + X1 + Y1 + X2 + Y2 + X3 + Y3 + X4 + Y4 + 'B'
                print(DATA)

                uart.write(DATA)
#                print(corner4_str + corner3_str + corner2_str + corner1_str)
    if y==3  :
        #img = sensor.snapshot()
        #img = sensor.snapshot().negate()
        for r in img.find_rects(threshold = 10000):
            if 80 > r.w() > 30 and 80 >r.h() > 30 :
                # 在屏幕上框出矩形
                img.draw_rectangle(r.rect(), color = (0, 0, 225), scale = 4)
                # 获取矩形角点位置
                corner = r.corners()
                # 在屏幕上圈出矩形角点
                img.draw_circle(corner[0][0], corner[0][1], 2, color = (0, 225, 0), thickness = 2, fill = False)
                img.draw_circle(corner[1][0], corner[1][1], 2, color = (0, 225, 0), thickness = 2, fill = False)
                img.draw_circle(corner[2][0], corner[2][1], 2, color = (0, 225, 0), thickness = 2, fill = False)
                img.draw_circle(corner[3][0], corner[3][1], 2, color = (0, 225, 0), thickness = 2, fill = False)
                corner1_str = corner1 = corner[0][0],corner[0][1]#角点坐标1左下
                corner2_str = corner2 = corner[1][0],corner[1][1]#角点坐标2右下
                corner3_str = corner3 = corner[2][0],corner[2][1]#角点坐标3右上
                corner4_str = corner4 = corner[3][0],corner[3][1]#角点坐标4左上

                X1 = '%03d' % corner[3][0]
                Y1 = '%03d' % corner[3][1]
                X2 = '%03d' % corner[2][0]
                Y2 = '%03d' % corner[2][1]
                X3 = '%03d' % corner[1][0]
                Y3 = '%03d' % corner[1][1]
                X4 = '%03d' % corner[0][0]
                Y4 = '%03d' % corner[0][1]

                DATA =  'A' + X1 + Y1 + X2 + Y2 + X3 + Y3 + X4 + Y4 + 'B'
                print(DATA)

                uart.write(DATA)
       #将画板画布与感光器图像叠加
