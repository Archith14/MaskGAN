import cv2
from os import listdir
from os.path import isfile, join
import os
import numpy as np

mypath = './Data_preprocessing/test_label'
mypath_2 = './test_results'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
img_color = np.empty(len(onlyfiles), dtype=object)

accuracy_background_list = []
accuracy_skin_list = []
accuracy_brow_list = []
accuracy_eye_list = []
accuracy_nose_list = []
accuracy_mouth_list = []
accuracy_u_lip_list = []
accuracy_l_lip_list = []
accuracy_neck_list = []
accuracy_cloth_list = []
accuracy_hair_list = []

for n in range(0, 20):

    img_color=cv2.imread(join(mypath, str(n + 1) + ".png"))
    img_color_2=cv2.imread(join(mypath_2, str(n + 1) + ".png"))

    height, width, channel = img_color.shape

    ########################################################################################################################

    ########################################################################################################################

    gt_background = 0
    gt_skin = 0
    gt_brow = 0
    gt_eye = 0
    gt_nose = 0
    gt_mouth = 0
    gt_u_lip = 0
    gt_l_lip = 0
    gt_neck = 0
    gt_cloth = 0
    gt_hair = 0

    overlap_area_background = 0
    overlap_area_skin = 0
    overlap_area_brow = 0
    overlap_area_eye = 0
    overlap_area_nose = 0
    overlap_area_mouth = 0
    overlap_area_u_lip = 0
    overlap_area_l_lip = 0
    overlap_area_neck = 0
    overlap_area_cloth = 0
    overlap_area_hair = 0

    ########################################################################################################################

    background_b = 0
    background_g = 0
    background_r = 0

    skin_b = 0
    skin_g = 0
    skin_r = 204

    brow_b = 255
    brow_g = 255
    brow_r = 0

    eye_b = 255
    eye_g = 51
    eye_r = 51

    nose_b = 0
    nose_g = 153
    nose_r = 76

    mouth_b = 0
    mouth_g = 204
    mouth_r = 102

    u_lip_b = 0
    u_lip_g = 255
    u_lip_r = 255

    l_lip_b = 153
    l_lip_g = 0
    l_lip_r = 0

    neck_b = 51
    neck_g = 153
    neck_r = 255

    cloth_b = 0
    cloth_g = 204
    cloth_r = 0

    hair_b = 204
    hair_g = 0
    hair_r = 0

    ########################################################################################################################
    print("\n")
    print("\n")
    print("\n")
    print("start")

    for y in range(0, height):
        for x in range(0, width):

            b = img_color.item(y, x, 0)
            g = img_color.item(y, x, 1)
            r = img_color.item(y, x, 2)

            # print(b, g, r)

            if b == background_b and g == background_g and r == background_r:
                gt_background = gt_background + 1

            if b == skin_b and g == skin_g and r == skin_r:
                gt_skin = gt_skin + 1

            if b == brow_b and g == brow_g and r == brow_r:
                gt_brow = gt_brow + 1

            if b == eye_b and g == eye_g and r == eye_r:
                gt_eye = gt_eye + 1

            if b == nose_b and g == nose_g and r == nose_r:
                gt_nose = gt_nose + 1

            if b == mouth_b and g == mouth_g and r == mouth_r:
                gt_mouth = gt_mouth + 1

            if b == u_lip_b and g == u_lip_g and r == u_lip_r:
                gt_u_lip = gt_u_lip + 1

            if b == l_lip_b and g == l_lip_g and r == l_lip_r:
                gt_l_lip = gt_l_lip + 1

            if b == neck_b and g == neck_g and r == neck_r:
                gt_neck = gt_neck + 1

            if b == cloth_b and g == cloth_g and r == cloth_r:
                gt_cloth = gt_cloth + 1

            if b == hair_b and g == hair_g and r == hair_r:
                gt_hair = gt_hair + 1

            ################################################################################################################

            b2 = img_color_2.item(y, x, 0)
            g2 = img_color_2.item(y, x, 1)
            r2 = img_color_2.item(y, x, 2)

            # print(b2, g2, r2)

            if b2 == background_b and g2 == background_g and r2 == background_r:
                overlap_area_background = overlap_area_background + 1

            if b2 == skin_b and g2 == skin_g and r2 == skin_r:
                overlap_area_skin = overlap_area_skin + 1

            if b2 == brow_b and g2 == brow_g and r2 == brow_r:
                overlap_area_brow = overlap_area_brow + 1

            if b2 == eye_b and g2 == eye_g and r2 == eye_r:
                overlap_area_eye = overlap_area_eye + 1

            if b2 == nose_b and g2 == nose_g and r2 == nose_r:
                overlap_area_nose = overlap_area_nose + 1

            if b2 == mouth_b and g2 == mouth_g and r2 == mouth_r:
                overlap_area_mouth = overlap_area_mouth + 1

            if b2 == u_lip_b and g2 == u_lip_g and r2 == u_lip_r:
                overlap_area_u_lip = overlap_area_u_lip + 1

            if b2 == l_lip_b and g2 == l_lip_g and r2 == l_lip_r:
                overlap_area_l_lip = overlap_area_l_lip + 1

            if b2 == neck_b and g2 == neck_g and r2 == neck_r:
                overlap_area_neck = overlap_area_neck + 1

            if b2 == cloth_b and g2 == cloth_g and r2 == cloth_r:
                overlap_area_cloth = overlap_area_cloth + 1

            if b2 == hair_b and g2 == hair_g and r2 == hair_r:
                overlap_area_hair = overlap_area_hair + 1

            ################################################################################################################

    try:
        accuracy_background = overlap_area_background / gt_background

        if accuracy_background > 1:
            accuracy_background = 1 - (accuracy_background - 1)

        # print("gt area background")
        # print(gt_background)
        # print("overlap area background")
        # print(overlap_area_background)
        print("accuracy background")
        print(accuracy_background)

        accuracy_background_list.append(accuracy_background)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_skin = overlap_area_skin / gt_skin

        if accuracy_skin > 1:
            accuracy_skin = 1 - (accuracy_skin - 1)

        # print("gt area skin")
        # print(gt_skin)
        # print("overlap area skin")
        # print(overlap_area_skin)
        print("accuracy skin")
        print(accuracy_skin)

        accuracy_skin_list.append(accuracy_skin)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_brow = overlap_area_brow / gt_brow

        if accuracy_brow > 1:
            accuracy_brow = 1 - (accuracy_brow - 1)

        # print("gt area brow")
        # print(gt_brow)
        # print("overlap area brow")
        # print(overlap_area_brow)
        print("accuracy brow")
        print(accuracy_brow)

        accuracy_brow_list.append(accuracy_brow)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_eye = overlap_area_eye / gt_eye

        if accuracy_eye > 1:
            accuracy_eye = 1 - (accuracy_eye - 1)

        # print("gt area eye")
        # print(gt_eye)
        # print("overlap area eye")
        # print(overlap_area_eye)
        print("accuracy eye")
        print(accuracy_eye)

        accuracy_eye_list.append(accuracy_eye)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_nose = overlap_area_nose / gt_nose

        if accuracy_nose > 1:
            accuracy_nose = 1 - (accuracy_nose - 1)

        # print("gt area nose")
        # print(gt_nose)
        # print("overlap area nose")
        # print(overlap_area_nose)
        print("accuracy nose")
        print(accuracy_nose)

        accuracy_nose_list.append(accuracy_nose)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_mouth = overlap_area_mouth / gt_mouth

        if accuracy_mouth > 1:
            accuracy_mouth = 1 - (accuracy_mouth - 1)

        # print("gt area mouth")
        # print(gt_mouth)
        # print("overlap area mouth")
        # print(overlap_area_mouth)
        print("accuracy mouth")
        print(accuracy_mouth)

        accuracy_mouth_list.append(accuracy_mouth)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_u_lip = overlap_area_u_lip / gt_u_lip

        if accuracy_u_lip > 1:
            accuracy_u_lip = 1 - (accuracy_u_lip - 1)

        # print("gt area u lip")
        # print(gt_u_lip)
        # print("overlap area u lip")
        # print(overlap_area_u_lip)
        print("accuracy u lip")
        print(accuracy_u_lip)

        accuracy_u_lip_list.append(accuracy_u_lip)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_l_lip = overlap_area_l_lip / gt_l_lip

        if accuracy_l_lip > 1:
            accuracy_l_lip = 1 - (accuracy_l_lip - 1)

        # print("gt area l lip")
        # print(gt_l_lip)
        # print("overlap area l lip")
        # print(overlap_area_l_lip)
        print("accuracy l lip")
        print(accuracy_l_lip)

        accuracy_l_lip_list.append(accuracy_l_lip)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_neck = overlap_area_neck / gt_neck

        if accuracy_neck > 1:
            accuracy_neck = 1 - (accuracy_neck - 1)

        # print("gt area neck")
        # print(gt_neck)
        # print("overlap area neck")
        # print(overlap_area_neck)
        print("accuracy neck")
        print(accuracy_neck)

        accuracy_neck_list.append(accuracy_neck)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_cloth = overlap_area_cloth / gt_cloth

        if accuracy_cloth > 1:
            accuracy_cloth = 1 - (accuracy_cloth - 1)

        # print("gt area cloth")
        # print(gt_cloth)
        # print("overlap area cloth")
        # print(overlap_area_cloth)
        print("accuracy cloth")
        print(accuracy_cloth)

        accuracy_cloth_list.append(accuracy_neck)

    except:
        pass

    ########################################################################################################################

    try:
        accuracy_hair = overlap_area_hair / gt_hair

        if accuracy_hair > 1:
            accuracy_hair = 1 - (accuracy_hair - 1)

        # print("gt area hair")
        # print(gt_hair)
        # print("overlap area hair")
        # print(overlap_area_hair)
        print("accuracy hair")
        print(accuracy_hair)

        accuracy_hair_list.append(accuracy_hair)

    except:
        pass

    ########################################################################################################################
    ########################################################################################################################
    ########################################################################################################################
    ########################################################################################################################

    cv2.waitKey(0)

    cv2.destroyAllWindows()
########################################################################################################################

print(accuracy_background_list)
print(sum(accuracy_background_list))
print(len(accuracy_background_list))
print("background average accuracy")
print(sum(accuracy_background_list) / len(accuracy_background_list))

print(accuracy_skin_list)
print(sum(accuracy_skin_list))
print(len(accuracy_skin_list))
print("skin average accuracy")
print(sum(accuracy_skin_list) / len(accuracy_skin_list))

print("brow average accuracy")
print(sum(accuracy_brow_list) / len(accuracy_brow_list))

print("eye average accuracy")
print(sum(accuracy_eye_list) / len(accuracy_eye_list))

print("nose average accuracy")
print(sum(accuracy_nose_list) / len(accuracy_nose_list))

print("mouth average accuracy")
print(sum(accuracy_mouth_list) / len(accuracy_mouth_list))

print("u lip average accuracy")
print(sum(accuracy_u_lip_list) / len(accuracy_u_lip_list))

print("l lip average accuracy")
print(sum(accuracy_l_lip_list) / len(accuracy_l_lip_list))

print("neck average accuracy")
print(sum(accuracy_neck_list) / len(accuracy_neck_list))

print("cloth average accuracy")
print(sum(accuracy_cloth_list) / len(accuracy_cloth_list))

print("hair average accuracy")
print(sum(accuracy_hair_list) / len(accuracy_hair_list))
