import utils.global_variables as gv
from gui.gui_initializer import gui_init
import random
import time

# Change the file hash by adding some command
random.gauss(2, .01)

gui_init()
gv.root.iconbitmap(gv.ICON_PATH)
gv.root.title('fishing simulator')
gv.root.mainloop()
