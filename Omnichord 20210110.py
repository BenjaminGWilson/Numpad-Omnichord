import winsound
import Panel_class

"""
Press buttons, make noises

"""

# standard modules
import tkinter as tk
from functools import partial


# local modules
from Panel_class import Panel

# c scale
scale = (261, 293,329, 349, 392, 440, 493, 523)


def launch_gui():
    root = tk.Tk()

    panel = Panel()
    panel.title = "Numpad Omnichord"
    panel.legend =" Press 1 - 7 on numpad to change chord"
    panel.overtake_window(root)

    root.bind("<Key>", make_beep)
    root.mainloop()



def make_beep(event):
       if not event.char.isdigit():
              return
       else:
              degree = int(event.char) - 1
              winsound.Beep (scale[degree], 200)

launch_gui()