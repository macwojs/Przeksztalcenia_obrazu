from PIL import Image
from numpy import unique, array

from morfo_logic import dilate_logic
from morfo_logic import erode_logic
from morfo_mono import dilate_mono
from morfo_mono import erode_mono


def close(filename, len, deg):
    image = Image.open(filename)
    pix = array(image)
    uniq = unique(pix)
    if uniq.shape[0] == 2:
        dil_im = dilate_logic(image, len, deg)
        out = erode_logic(dil_im, len, deg)
    else:
        dil_im = dilate_mono(image, len, deg)
        out = erode_mono(dil_im, len, deg)
        print("a")

    return out
