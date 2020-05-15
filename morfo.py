from strel import strel_line
from PIL import Image
import numpy as np

def compare_dil(mask, cut):
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            if mask[row, col] == 1:
                if mask[row, col] == cut[row, col]:
                    return True
    return False

def compare_ero(mask, cut):
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            if mask[row, col] == 1:
                if mask[row, col] == cut[row, col]:
                    continue
                else:
                    return False
    return True

def dilate_logic(im, len, deg):
    strel = strel_line(len, deg)

    # odwracanie elementu strukturalnego
    # strel[strel > 0] = 2
    # strel[strel == 0] = 1
    # strel[strel == 2] = 0

    strel_row_around = strel.shape[0] - 1
    strel_col_around = strel.shape[1] - 1
    strel_row_one_side = int(strel_row_around / 2)
    strel_col_one_side = int(strel_col_around / 2)

    # image = Image.open("logic_image.png")
    image = np.array(im)
    image[image > 0] = 1

    # powiększenie rozszerzenie obrazu o zera
    image_big = np.zeros((image.shape[0] + strel_row_around, image.shape[1] + strel_col_around))
    image_big[strel_row_one_side:image.shape[0] + strel_row_one_side,
    strel_col_one_side:image.shape[1] + strel_col_one_side] = image

    # stworzenie obrazu wyjściowego
    image_out = np.zeros((image.shape[0], image.shape[1]))

    for row in range(strel_row_one_side, image.shape[0] + strel_row_one_side):
        for col in range(strel_col_one_side, image.shape[1] + strel_col_one_side):
            image_cut = image_big[row - strel_row_one_side:row + strel_row_one_side + 1,
                        col - strel_col_one_side:col + strel_col_one_side + 1]
            if compare_dil(strel, image_cut):
#                image_out[row - strel_row_one_side, col - strel_col_one_side] = image[row - strel_row_one_side, col - strel_col_one_side]
                image_out[row - strel_row_one_side, col - strel_col_one_side] = 1
            else:
                image_out[row - strel_row_one_side, col - strel_col_one_side] = 0

    # im = Image.open("logic_image.png")
    # pix = np.array(im)
    # pix[pix > 0] = 1 # zmiana na obraz binarny

    image_out[image_out > 0] = 255
    image_out = np.array(image_out, np.uint8)
    new_image = Image.fromarray(image_out)
    new_image.save('new2.png')
    return new_image

def erode_logic(im, len, deg):
    strel = strel_line(len, deg)

    #strel = np.ones((3, 3))
    strel_row_around = strel.shape[0] - 1
    strel_col_around = strel.shape[1] - 1
    strel_row_one_side = int(strel_row_around / 2)
    strel_col_one_side = int(strel_col_around / 2)
    #
    # # image = np.ones((13, 15))
    # # image[1, 7] = 0
    #image = Image.open(im)
    image = np.array(im)
    image[image > 0] = 1

    # powiększenie rozszerzenie obrazu o zera
    image_big = np.ones((image.shape[0] + strel_row_around, image.shape[1] + strel_col_around))
    image_big[strel_row_one_side:image.shape[0] + strel_row_one_side,
    strel_col_one_side:image.shape[1] + strel_col_one_side] = image

    # stworzenie obrazu wyjściowego
    image_out = np.zeros((image.shape[0], image.shape[1]))

    for row in range(strel_row_one_side, image.shape[0] + strel_row_one_side):
        for col in range(strel_col_one_side, image.shape[1] + strel_col_one_side):
            image_cut = image_big[row - strel_row_one_side:row + strel_row_one_side + 1,
                        col - strel_col_one_side:col + strel_col_one_side + 1]
            if compare_ero(strel, image_cut):
                image_out[row - strel_row_one_side, col - strel_col_one_side] = 1
            else:
                image_out[row - strel_row_one_side, col - strel_col_one_side] = 0

    # im = Image.open("logic_image.png")
    # pix = np.array(im)
    # pix[pix > 0] = 1 # zmiana na obraz binarny

    image_out[image_out > 0] = 255
    image_out = np.array(image_out, np.uint8)
    new_image = Image.fromarray(image_out)
    new_image.save("images/new3.png")
    return new_image

ime = Image.open("images/ship_bin.tif")
image_dil = dilate_logic(ime, 12, 120)
image_dil.save("images/new4.png")
image_ero = erode_logic(ime, 12, 120)
image_ero.save("images/new5.png")