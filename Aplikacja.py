from tkinter import Tk
from tkinter.filedialog import askopenfilename

from labeling import labeling
from ordfilt2 import ordfilt2
from regionprops import regionprops_cent
from regionprops import regionprops_equiv_diam
from PIL import Image
import numpy as np
import os
from close import close

################LABELING
Tk().withdraw()
filename1 = askopenfilename()

im_labeled = labeling(filename1)
file_name = 'images/%s_labeled.png' % (os.path.basename(filename1).split(".")[0])
im_labeled.save(file_name)

###############ORDFILT
Tk().withdraw()
filename2 = askopenfilename()

print('Podaj rozmiar maski')
m_x = int(input())
print('x')
m_y = int(input())
print('Podaj numer elementu')
n = int(input())

im_ordfilt = ordfilt2(filename2, m_x, m_y, n)
file_name = 'images/%s_ordfil.png' % (os.path.basename(filename2).split(".")[0])
im_ordfilt.save(file_name)

#################REGIONPROPS
im = Image.open("images/logic_image_labeled.png")

im_prop_cent = regionprops_cent(im)
file_name = 'images/%s_prop_centroid.txt' % (os.path.basename(filename1).split(".")[0])
np.savetxt(file_name, im_prop_cent, fmt='%1.6g')

im_prop_equiv_diam = regionprops_equiv_diam(im)
file_name = 'images/%s_prop_equiv_diam.txt' % (os.path.basename(filename1).split(".")[0])
np.savetxt(file_name, im_prop_equiv_diam, fmt='%1.6g')

#################CLOSE
im_close_logic = close("images/ship_bin.tif", 3, 45)
im_close_mono = close("images/cameraman.tif", 3, 45)
file_name = 'images/%s_close.tif' % (os.path.basename("images/ship_bin.tif").split(".")[0])
im_close_logic.save(file_name)
file_name = 'images/%s_close.tif' % (os.path.basename("images/cameraman.tif").split(".")[0])
im_close_mono.save(file_name)

