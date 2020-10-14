import cv2
import numpy as num
import random


def decode():
    img = cv2.imread("hidden.png", 1)
    width = img.shape[0]
    height = img.shape[1]
    saved2img = num.zeros((width, height, 3), num.uint8)
    for val in range(width):
        for val_1 in range(height):
            for val_2 in range(3):
                bin_data = format(img[val][val_1][val_2], '08b')
                converted_bin = bin_data[-4:] + chr(random.randint(0, 1) + 48) * 4
                saved2img[val][val_1][val_2] = int(converted_bin, 2)
    cv2.imwrite('saved.png', saved2img)

