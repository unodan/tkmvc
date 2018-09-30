########################################################################################################################
#    File: controller.py
#  Author: Dan Huckson, https://github.com/unodan
#    Date: 2018-09-19
########################################################################################################################

from tkinter import Tk


class Controller(Tk):
    def __init__(self, *args, **kwargs):
        self.app_title = kwargs.pop('title', None)
        super().__init__(*args, **kwargs)
        self.withdraw()
