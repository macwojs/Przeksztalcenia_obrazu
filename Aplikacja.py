import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import numpy as np
from PIL import Image

from close import close
from labeling import labeling
from ordfilt2 import ordfilt2
from regionprops import regionprops_cent
from regionprops import regionprops_equiv_diam

# #################REGIONPROPS
# Tk().withdraw()
# file_name_regionprops = askopenfilename()
#
# im = Image.open(file_name_regionprops)
#
# im_prop_cent = regionprops_cent(im)
# file_name = 'result/%s_prop_centroid.txt' % (os.path.basename(file_name_regionprops).split(".")[0])
# np.savetxt(file_name, im_prop_cent, fmt='%1.6g')
#
# im_prop_equiv_diam = regionprops_equiv_diam(im)
# file_name = 'result/%s_prop_equiv_diam.txt' % (os.path.basename(file_name_regionprops).split(".")[0])
# np.savetxt(file_name, im_prop_equiv_diam, fmt='%1.6g')
#
# ###############ORDFILT
# Tk().withdraw()
# file_name_ordfilt = askopenfilename()
#
# print('Podaj rozmiar maski')
# m_x = int(input())
# print('x')
# m_y = int(input())
# print('Podaj numer elementu')
# n = int(input())
#
# im_ordfilt = ordfilt2(file_name_ordfilt, m_x, m_y, n)
# file_name = 'result/%s_ordfil.png' % (os.path.basename(file_name_ordfilt).split(".")[0])
# im_ordfilt.save(file_name)

#################CLOSE
Tk().withdraw()
file_name_close = askopenfilename()
print('Podaj dlugosc linii')
len = int(input())
print('Podaj kat')
deg = int(input())

im_close = close(file_name_close, len, deg)
file_name = 'result/%s_close.tif' % (os.path.basename(file_name_close).split(".")[0])
im_close.save(file_name)


################LABELING
# Tk().withdraw()
# file_name_labeling = askopenfilename()
#
# im_labeled = labeling(file_name_labeling)
# file_name = 'result/%s_labeled.png' % (os.path.basename(file_name_labeling).split(".")[0])
# im_labeled.save(file_name)
