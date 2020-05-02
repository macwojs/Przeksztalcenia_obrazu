from tkinter import Tk
from tkinter.filedialog import askopenfilename

import labeling as l

Tk().withdraw()
filename = askopenfilename()

l.labeling(filename)
