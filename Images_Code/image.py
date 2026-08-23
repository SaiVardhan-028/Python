from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("costume.jpg") as img:
        img = img.rotate(360)
        img = img.filter(ImageFilter.BLUR)
        #img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpg")
        
main()