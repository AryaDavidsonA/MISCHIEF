# Stegano_Script
Steganography is the method of hiding a secret message within an image.
What I have done here is a process of hiding another image within an image. For that, I used the Least significant bit(LSB) concept.According to the concept of LSB, if we change the last bit value of a pixel, there won't be any changes in the color. In a RGB image each pixel has 8 bits(24). In this script, the use of RGB method is to store data in the first bit of every pixel.
Here in this process ,the widely supported JPEG images are converted to PNG format. Also, check the requirment.txt for needed modules.

## Requirments
    pip3 install cv2
    pip3 install numpy
    pip3 install random
(Install the above libraries for code execution.)

## Usage

I tried to encode 2 images at a time and it worked. Here, the process is  1st image hiding the 2nd image and 2nd image hiding the 3rd image.  If you want to know how it's ,then you can check below.

1.The script should execute as shown below.
    
    python3 stegano_test.py

2.Then you will get the options like below.

    Please choose your option!!! 
    1. Encode    
    2. Decode
    Enter your choice here : 
  
3.If you choose the option 1, again you will get the options like below.

    Enter your first image : 
    Enter your second image : 
    Enter your third image : 
    
4.Here, you can see the image has been encoded and saved as 'hidden.png' and 'secret.png'.

5.if you choose the option 2, again you will get the options like below.

    Enter your image for decode :
    Enter your image for decode :  
  
6.Here, you can see image has been decoded and saved as 'stego.png' and 'stego1.png'.

7.You can check the image files named 'hidden.png','secret.png','stego.png' and 'stego1.png'.


## Try with JPEG images.
