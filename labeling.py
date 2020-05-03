import numpy as np
from PIL import Image


def labeling(filename):
    im = Image.open(filename)
    pix = np.array(im)

    white = 255
    black = 0

    # zmiana na obraz 255 a nie bit
    pix[pix > 0] = white

    num_rows = pix.shape[0]
    num_cols = pix.shape[1]

    # Tworzenie obrazu wyjściowego
    output = [[white for y in range(num_rows)]
              for x in range(num_cols)]
    output = np.array(output, np.uint8)

    # Ilosc mozliwych do rozpoznania obiektow (nalezy podzielic przez 3)
    obj_number = 240

    # labeling
    for row in range(num_rows):
        for cell in range(num_cols):
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
                    output[row][cell] = obj_number
                    obj_number = obj_number - 3
            else:
                output[row][cell] = pixel


    # new_image = Image.fromarray(output)
    # new_image.save('new.png')

    # tworzenie obrazu do scalenia
    output2 = output

    for row in range(num_rows - 1, -1, -1):
        for cell in range(num_cols):
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
    #new_image2.save('new2.png')

    return new_image2
