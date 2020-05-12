from tkinter import Tk
from tkinter.filedialog import askopenfilename

from labeling import labeling
from ordfilt2 import ordfilt2
from regionprops_cent import regionprops_cent
from regionprops_cent import regionprops_equiv_diam
from PIL import Image
import os
################LABELING
Tk().withdraw()
filename1 = askopenfilename()

im_labeled = labeling(filename1)
file_name = '%s_labeled.png' % (os.path.basename(filename1).split(".")[0])
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
file_name = '%s_ordfil.png' % (os.path.basename(filename2).split(".")[0])
im_ordfilt.save(file_name)


#################REGIONPROPS
im = Image.open("logic_image_labeled.png")
im_prop_cent = regionprops_cent(im)
im_prop_cent = regionprops_equiv_diam(im)
#regionprops_cent(im_labeled)


