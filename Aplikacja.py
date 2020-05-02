import numpy as np
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
print(filename)

im = Image.open(filename)
pix = np.array(im)

white = 255
black = 0

numRows = pix.shape[0]
numCols = pix.shape[1]

# Tworzenie obrazu wyjściowego
output = [[white for y in range(numRows)]
          for x in range(numCols)]
output = np.array(output, np.uint8)

# Ilosc mozliwych do rozpoznania obiektow (nalezy podzielic przez 3)
objNumber = 240

# labeling
for row in range(numRows):
    for cell in range(numCols):
        pixel = pix[row][cell]
        if pixel != white:
            above = white
            left = white
            try:  # sprawdzamy pixel powyzej
                above = pix[row - 1][cell]
            except:
                print("Brak pixela powyzej")

            try:  # pobieramy pixel po lewej
                left = pix[row][cell - 1]
            except:
                print("Brak pixela z lewej")

            if left != white:
                output[row][cell] = output[row][cell - 1]
            elif above != white:
                output[row][cell] = output[row - 1][cell]
            else:
                output[row][cell] = objNumber
                objNumber = objNumber - 3
        else:
            output[row][cell] = pixel

new_image = Image.fromarray(output)
new_image.save('new.png')

# tworzenie obrazu do
output2 = output

for row in range(numRows - 1, -1, -1):
    for cell in range(numCols):
        pixel = output[row][cell]
        if pixel != white:
            above = white
            right = white
            try:
                above = output[row - 1][cell]
            except:
                print("Nie ma juz linii nad")
            try:
                right = output[row][cell + 1]
            except:
                print("Nie ma juz linii na prawo")
            if above != white:
                output2[output2 == above] = pixel
            if right != white:
                output2[output2 == right] = pixel

new_image2 = Image.fromarray(output2)
new_image2.save('new2.png')
