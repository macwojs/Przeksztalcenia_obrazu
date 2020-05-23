from PIL import Image

from morfo import dilate
from morfo import erode


def close(filename, len, deg):
    image = Image.open(filename)
    dil_im = dilate(image, len, deg)
    out = erode(dil_im, len, deg)

    return out
