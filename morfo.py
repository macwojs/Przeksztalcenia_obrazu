import numpy as np
from PIL import Image

from strel import strel_line


def find(mask, cut):
    list = []
    output = np.array(list)
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            if mask[row, col] == 1:
                output = np.append(output, [cut[row, col]])
    return output


def erode(im, len, deg):
    strel = strel_line(len, deg)

    strel_row_around = strel.shape[0] - 1
    strel_col_around = strel.shape[1] - 1
    strel_row_one_side = int(strel_row_around / 2)
    strel_col_one_side = int(strel_col_around / 2)

    image = np.array(im)

    # powiększenie rozszerzenie obrazu o jedynki
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
            values = find(strel, image_cut)
            image_out[row - strel_row_one_side, col - strel_col_one_side] = np.amin(values)

    if np.unique(image_out).shape[0] == 2:
        image_out[image_out > 0] = 255
    image_out = np.array(image_out, np.uint8)
    new_image = Image.fromarray(image_out)
    new_image.save("images/new2.png")
    return new_image


def dilate(im, len, deg):
    strel = strel_line(len, deg)

    strel_row_around = strel.shape[0] - 1
    strel_col_around = strel.shape[1] - 1
    strel_row_one_side = int(strel_row_around / 2)
    strel_col_one_side = int(strel_col_around / 2)

    image = np.array(im)

    # powiększenie rozszerzenie obrazu o zera
    image_big = np.zeros((image.shape[0] + strel_row_around, image.shape[1] + strel_col_around))
    # image_big[image_big > 0] = 0
    image_big[strel_row_one_side:image.shape[0] + strel_row_one_side,
    strel_col_one_side:image.shape[1] + strel_col_one_side] = image

    # stworzenie obrazu wyjściowego
    image_out = np.zeros((image.shape[0], image.shape[1]))

    for row in range(strel_row_one_side, image.shape[0] + strel_row_one_side):
        for col in range(strel_col_one_side, image.shape[1] + strel_col_one_side):
            image_cut = image_big[row - strel_row_one_side:row + strel_row_one_side + 1,
                        col - strel_col_one_side:col + strel_col_one_side + 1]
            values = find(strel, image_cut)
            image_out[row - strel_row_one_side, col - strel_col_one_side] = np.amax(values)

    if np.unique(image_out).shape[0] == 2:
        image_out[image_out > 0] = 255
    image_out = np.array(image_out, np.uint8)
    new_image = Image.fromarray(image_out)
    new_image.save("images/new3.png")
    return new_image
