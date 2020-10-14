# Stegano_Script
Steganography is the method of hiding a secret message within an image.
What I have done here is a process of hiding another image within an image. For that, I used the Least significant bit(LSB) concept.According to the concept of LSB, if we change the last bit value of a pixel, there won't be any changes in the color. In a RGB image each pixel has 8 bits(24). In this script, the use of RGB method is to store data in the first bit of every pixel.
Here in this process , the widely supported JPEG images are converted to PNG format. Also, check the requirment.txt for needed modules.
