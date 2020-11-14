import cv2
from os import listdir
from os.path import isfile, join
import os
import numpy as np

mypath = './Data_preprocessing/test_label'
mypath_2 = './test_results'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
n_images=len(onlyfiles)
t_acc=0
for n in range(n_images):
    target = cv2.imread(join(mypath, str(n) + ".png"))
    prediction = cv2.imread(join(mypath_2, str(n) + ".png"))
    intersection = np.logical_and(target, prediction)
    union = np.logical_or(target, prediction)
    iou_score = np.sum(intersection) / np.sum(union)
    print(iou_score*100)
    t_acc+=iou_score

    cv2.waitKey(0)
    cv2.destroyAllWindows()

final_accuracy=t_acc/n_images
print("Average IOU score =",final_accuracy*100,"%")
