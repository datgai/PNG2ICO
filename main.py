from PIL import Image
import os

"""
This is a simple script that converts .png file into .ico file
change the below variables as according to your needs
"""

#Variables
path = r" INSERT INPUT PATH HERE"
icon_sizes = [(192,192)] # Change output dimension here


def main():
    #makes a new folder
    try:
        os.mkdir("Converted")
    except FileExistsError:
        print("Oops, Folder already exists, might wanna change the folder name.")

    for filename in os.listdir(path):
        if filename[-4:] == ".png":
            img = Image.open(filename)
            img.save(f"{path}/Converted/{filename[:-4]}.ico",sizes = icon_sizes)
            print(f"{filename} Saved as {filename[:-4]}.ico")

if __name__ == '__main__':
    main()