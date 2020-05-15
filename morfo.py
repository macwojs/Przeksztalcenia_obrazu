from strel import strel_line
from PIL import Image
import numpy as np


def compare_ero(mask, cut):
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            if mask[row, col] == cut[row, col]:
                continue
            else:
                return False
    return True


# len = 5
# deg = 45
# # def close(image, len, deg):
# strel = strel_line(len, deg)

strel = np.ones((3, 3))
strel_row_around = strel.shape[0] - 1
strel_col_around = strel.shape[1] - 1
strel_row_one_side = int(strel_row_around / 2)
strel_col_one_side = int(strel_col_around / 2)

image = np.ones((13, 15))
image[1, 7] = 0

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
        if compare_ero(strel, image_cut):
            image_out[row-strel_row_one_side, col-strel_col_one_side] = image[row-strel_row_one_side, col-strel_col_one_side]
        else:
            image_out[row-strel_row_one_side, col-strel_col_one_side] = 0

# im = Image.open("logic_image.png")
# pix = np.array(im)
# pix[pix > 0] = 1 # zmiana na obraz binarny

print(strel)
print(strel.shape)
