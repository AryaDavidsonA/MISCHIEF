# LOKI_SECRET
I developed a tool with a steganographic technique for hiding secret data. And I’m naming this tool ‘LOKI_SECRET’. Also, I can tell you that you can use this tool for CTF purposes. Because here I borrow the concept of the fictional character ‘Loki’: The god of mischief and the skilled liar.

Loki is a fictional character who appears in American comic books published by Marvel Comics. Based on the Norse goddess, the character is the Asgardian "God of Mischief", Odd's adopted child, the brother of superhero Thor and later Angela. Loki is portrayed as a supervillain and antihero. This character is often portrayed strictly as a man, but in some cases shows gender.

In my tool, Loki is trying to manipulate the user in the sense of helping the user to hide their secret image within another image. With the help of Steganography, Loki uses the LSB concept for encoding and decoding the image. According to the concept of LSB, Loki tried to change the first bit of every pixel to hiding the secret image.

## Requirments
    pip3 install opencv-python
    pip3 install random
    pip3 install nmupy
    pip3 install pyfiglet
    pip3 install time
(Install the above libraries for code execution.)

# How to use it
First unload and allow permisions.

    git clone https://github.com/AryaDavidsonA/LOKI_SECRET.git
    cd LOKI_SECRET
    chmod +x loki_secret.py

If it does not work, try to install all the libraries that are located in the file requirements.txt

    pip3 install -r requirements.txt

Run

    ./loki_secret.py
    OR
    python3 loki_secret.py
# License
AryaDavidsonA/LOKI_SECRET is licensed under the MIT License

