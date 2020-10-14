# Stegano_Script
Steganography is the method of hiding a secret message within an image.
What I have done here is a process of hiding another image within an image. For that, I used the Least significant bit(LSB) concept.According to the concept of LSB, if we change the last bit value of a pixel, there won't be any changes in the color. In a RGB image each pixel has 8 bits(24). In this script, the use of RGB method is to store data in the first bit of every pixel.
Here in this process ,the widely supported JPEG images are converted to PNG format. Also, check the requirment.txt for needed modules.

## Requirment
pip3 install cv2
pip3 install numpy
pip3 install random
(Install the above libraries for code execution.)

## Usage
1.python3 stegano_test.py

2.Then you will get options like below.
  (Please choose your option!!! 
   1. Encode 
   2. Decode 
  Enter your choice here : )
  
3.If you choose the option 1, again you will get options like below.
  Enter your choice here : 1
  Enter the first image name : 1st_image.jpeg
  Enter the image name for hide : 2nd_image.jpeg
  Given image encoded successfully and the image saved as hidden.png!!!
  
4.Here, you can see the image has been encoded and saved as 'hidden.png'.

5.if you choose the option 2, again you will get the options like below.
  Enter your choice here : 2
  Enter the image for decode : hidden.png
  Your image decoded successfully, the image encrypted from  hidden.png  and saved as saved.png!!!
  
6.Here, you can see image has been decoded and saved as 'saved.png'.

7. You can check the files named 'hidden.png' and 'saved.png'.


## Try with JPEG images.
