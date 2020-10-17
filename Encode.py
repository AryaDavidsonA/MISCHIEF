import cv2


def encode(first_image, second_image, third_image):
    image1 = cv2.imread(first_image, 1)
    image2 = cv2.imread(second_image, 1)
    image3 = cv2.imread(third_image, 1)
    width = 250
    height = 250
    area = (width, height)
    im1 = cv2.resize(image1, area)
    im2 = cv2.resize(image2, area)
    im3 = cv2.resize(image3, area)
    for val in range(height):
        for val_1 in range(width):
            for val_2 in range(3):
                pixel1 = format(im1[val][val_1][val_2], '08b')
                pixel2 = format(im2[val][val_1][val_2], '08b')
                pixel3 = format(im3[val][val_1][val_2], '08b')
                pix1 = pixel1[0:4] + pixel2[0:4]
                pix2 = pixel2[0:4] + pixel3[0:4]
                im1[val][val_1][val_2] = int(pix1, 2)
                im2[val][val_1][val_2] = int(pix2, 2)
    cv2.imwrite('hidden.png', im1)
    cv2.imwrite('secret.png', im2)
    return 1
