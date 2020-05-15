from strel import strel_line
from PIL import Image
import numpy as np


def find_ero(mask, cut):
    output = np.array([255])
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            if mask[row, col] == 1:
                output = np.append(output, [cut[row, col]])
    return output

def erode_mono(im, len, deg):
    strel = strel_line(len, deg)

    # strel = np.ones((3, 3))
    strel_row_around = strel.shape[0] - 1
    strel_col_around = strel.shape[1] - 1
    strel_row_one_side = int(strel_row_around / 2)
    strel_col_one_side = int(strel_col_around / 2)

    # # image = np.ones((13, 15))
    # # image[1, 7] = 0
    # image = Image.open(im)
    image = np.array(im)
    # image[image > 0] = 1

    # powiększenie rozszerzenie obrazu o zera
    image_big = np.ones((image.shape[0] + strel_row_around, image.shape[1] + strel_col_around))
    image_big[image_big > 0] = 255
    image_big[strel_row_one_side:image.shape[0] + strel_row_one_side,
    strel_col_one_side:image.shape[1] + strel_col_one_side] = image

    # stworzenie obrazu wyjściowego
    image_out = np.zeros((image.shape[0], image.shape[1]))

    for row in range(strel_row_one_side, image.shape[0] + strel_row_one_side):
        for col in range(strel_col_one_side, image.shape[1] + strel_col_one_side):
            image_cut = image_big[row - strel_row_one_side:row + strel_row_one_side + 1,
                        col - strel_col_one_side:col + strel_col_one_side + 1]
            values = find_ero(strel, image_cut)
            image_out[row - strel_row_one_side, col - strel_col_one_side] = np.amin(values)

    # im = Image.open("logic_image.png")
    # pix = np.array(im)
    # pix[pix > 0] = 1 # zmiana na obraz binarny

    # image_out[image_out > 0] = 255
    image_out = np.array(image_out, np.uint8)
    new_image = Image.fromarray(image_out)
    new_image.save("images/new3.png")
    return new_image


ime = Image.open("images/cameraman.tif")
image_dil = erode_mono(ime, 12, 120)
