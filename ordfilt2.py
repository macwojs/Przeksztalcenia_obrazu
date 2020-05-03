import numpy as np
from PIL import Image


def ordfilt2(filename, m_x, m_y, n):
    im = Image.open(filename)

    while n > (m_x * m_y) or n < 1:
        print('Podaj poprawny numer elementu')
        n = input()

    if im.mode == 'RGB':
        image = ordfilt2rgb(im, m_x, m_y, n)
    elif im.mode == 'L':
        image = ordfilt2mono(im, m_x, m_y, n)
    else:
        print("Zły rodzaj obrazu!")
        return

    return image


def ordfilt2rgb(im, x, y, n):
    r, g, b = im.split()
    r_ord = ordfilt2mono(r, x, y, n)
    g_ord = ordfilt2mono(g, x, y, n)
    b_ord = ordfilt2mono(b, x, y, n)
    img = Image.merge('RGB', (r_ord, g_ord, b_ord))
    return img


def ordfilt2mono(im, x, y, n):
    pix = np.array(im)

    nr = n

    mask_size_row = x
    mask_size_col = y

    num_rows = pix.shape[0]
    num_cols = pix.shape[1]

    # powiekszamy obraz żeby nie miec errorow
    pix_an = np.zeros((num_rows + mask_size_row, num_cols + mask_size_col))
    pix_an[:num_rows, :num_cols] = pix

    output = [[0 for y in range(num_cols)]
              for x in range(num_rows)]
    output = np.array(output, np.uint8)

    for row in range(num_rows):
        for col in range(num_cols):
            mask = pix_an[row:row + mask_size_row, col:col + mask_size_col]
            mask_sorted = np.sort(mask, axis=None)
            output[row][col] = mask_sorted[nr - 1]

    # output = output.transpose()
    new_image = Image.fromarray(output)
    # new_image.show()
    return new_image
