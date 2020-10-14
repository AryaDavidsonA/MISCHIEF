import cv2


def encode(first_image, second_image):
    image1 = cv2.imread(first_image, 1)
    image2 = cv2.imread(second_image, 1)
    width = 300
    height = 300
    area = (width, height)
    im1 = cv2.resize(image1, area, cv2.INTER_AREA)
    im2 = cv2.resize(image2, area, cv2.INTER_AREA)
    for val in range(width):
        for val_1 in range(height):
            for val_2 in range(3):
                pixel1 = format(im1[val][val_1][val_2], '08b')
                pixel2 = format(im2[val][val_1][val_2], '08b')
                pixel = pixel1[0:4] + pixel2[0:4]
                im1[val][val_1][val_2] = int(pixel, 2)
    cv2.imwrite('hidden.png', im1)
    return 1
