import sys
from PIL import Image, ImageOps
import os

'''
In a file called shirt.py, implement a program that:

    Expects the user to provide two command-line arguments, looks like:
        python shirt.py before.jpg after.jpg
        in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
        in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

    In the swap_imgs function, the program should then
        overlay shirt.png (which already has a transparent background) on top of the input img
        after resizing and cropping the input img to be the same size as shirt.png
        saving the result as its output.

program should instead exit via sys.exit with an error message
    if the user does not specify exactly two command-line arguments
    if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if the input’s name does not have the same extension as the output’s name
    if the specified input file does not exist

Open the input with Image.open,
    per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit, using default values for method, bleed, and centering,
    per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
overlay the shirt with Image.paste
    per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
save the result with Image.save,
    per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

first must done:
pip install Pillow
# download shirt.png: wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
# download muppet photos: wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip
# unzip  muppet photos:  unzip muppets.zip

'''

def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif (sys.argv[1][-4:].lower() not in ['.jpg', '.jpeg, ', '.png']):
         sys.exit('Invalid input')
    elif (sys.argv[2][-4:].lower() not in ['.jpg', '.jpeg, ', '.png']):
        sys.exit('Invalid output')
    elif sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
        sys.exit('Input and output have different extensions')
    else:
        im_in = sys.argv[1]
        im_out = sys.argv[2]
        print(f'{im_in} and {im_out}')
        overlay_imgs(im_in, im_out)


def overlay_imgs(im_in, im_out):
    try:
        file, ext = os.path.splitext(im_in)
        # print(f'{file} and {ext}')
        shirt = Image.open('shirt.png')
        size =  shirt.size

        with Image.open(im_in) as im:
            im_sized = ImageOps.fit(im, size)
            im_sized.paste(shirt, mask=shirt)
            # print(type(im_sized))
            im_sized.save(im_out)

    except FileNotFoundError:
        sys.exit('Input does not exist')


if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/shirt
# submit50 cs50/problems/2022/python/shirt

