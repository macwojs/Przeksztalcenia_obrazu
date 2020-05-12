import numpy as np
from PIL import Image


def regionprops_cent(image):
    pix = np.array(image)

    unique = np.unique(pix)
    unique = unique[unique != 0] # dla czarnego nie liczymy


    # tworzenie macierzy na wyniki
    output = np.zeros((unique.size, 3))
    output[:, 0] = unique

    i = 0
    for un in unique:
        where = np.argwhere(pix == unique[i])
        length = where.size / 2
        for wh in where:
            output[i, 1] = output[i, 1] + wh[1]
            output[i, 2] = output[i, 2] + wh[0]
        output[i, 1] = output[i, 1] / length + 1
        output[i, 2] = output[i, 2] / length + 1
        i = i + 1

    print(unique)
