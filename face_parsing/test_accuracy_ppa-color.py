import cv2
from os import listdir
from os.path import isfile, join
import os
import numpy as np

mypath = './Data_preprocessing/test_label-color'
mypath_2 = './test_color_visualize'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
n_images=len(onlyfiles)
t_acc=0
for n in range(n_images):
    img_color = cv2.imread(join(mypath, str(n) + ".png"))
    img_color_2 = cv2.imread(join(mypath_2, str(n) + ".png"))
    height, width, channel = img_color.shape
    correct=0
    total=0
    for y in range(height):
        for x in range(width):

            total+=1
            b = img_color.item(y, x, 0)
            g = img_color.item(y, x, 1)
            r = img_color.item(y, x, 2)

            b2 = img_color_2.item(y, x, 0)
            g2 = img_color_2.item(y, x, 1)
            r2 = img_color_2.item(y, x, 2)

            if(b==b2 and g==g2 and r==r2):
                correct+=1
    accuracy=correct/total
    print(accuracy*100)
    t_acc+=accuracy

    cv2.waitKey(0)
    cv2.destroyAllWindows()

final_accuracy=t_acc/n_images
print("Average Per Pixel Accuracy =",final_accuracy*100,'%')
