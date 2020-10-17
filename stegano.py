import Decode
import Encode


def stegano():
    Choice = int(input("Please choose your option!!! \n 1. Encode \n 2. Decode \n Enter your choice here : "))
    if Choice == 1:
        first = input("Enter your first image : ")
        second = input("Enter your second image : ")
        third = input("Enter your third image : ")
        Encode.encode(first, second, third)
        print("Given image encrypted successfully!!!")
        print("Image saved as hidden.png and secret.png!!!")

    elif Choice == 2:

        dec = input("Enter your image for decode : ")
        dec_1 = input("Enter your image for decode : ")
        Decode.decode()
        print("Your image decrypted successfully!!!")
        print("Image decrypted from ", dec, "and", dec_1, "!!!")
        print("Both image saved as stego.png and stego1.png!!!")
    else:
        raise Exception("Choose the correct option!!!")


stegano()
