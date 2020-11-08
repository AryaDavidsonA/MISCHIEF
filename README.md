# LOKI_SECRET
I developed a tool with a steganographic technique for hiding secret data. And I’m naming this tool ‘LOKI_SECRET’. Also, I can tell you that you can use this tool for CTF purposes. Because here I borrow the concept of the fictional character ‘Loki’: the false god and the skilled liar.

Loki is a fictional character who appears in American comic books published by Marvel Comics. Based on the Norse goddess, the character is the Asgardian "God of Mischief", Odd's adopted child, the brother of superhero Thor and later Angela. Loki is portrayed as a supervillain and antihero. This character is often portrayed strictly as a man, but in some cases shows gender.

In my tool, Loki is trying to manipulate the user in the sense of helping the user to hide their secret image within another image. With the help of Steganography, Loki uses the LSB concept for encoding and decoding the image. According to the concept of LSB, Loki tried to change the first bit of every pixel to hiding the secret image.

## Requirments
    pip3 install opencv-python
    pip3 install pyfiglet
    pip3 install time
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
