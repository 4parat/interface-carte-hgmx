from PIL import Image
import os
import sys


k = float(sys.argv[1])
print(os.getcwd())

for i in os.listdir():
    img = Image.open(i)
    img = img.resize((int(img.width*k), int(img.height*k)))
    img.save("../"+i)