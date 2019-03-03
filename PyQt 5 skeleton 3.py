#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtQuick import *
from PyQt5.uic import *
from PyQt5.QtQml import *

#-------------------------------------------------
    
__author__ = '__Bill__'


class _Window_(QWidget):
    """
    -------------------(_Example_)------------------
    """
    def __init__(self):
        super().__init__()
        print(_Window_.__doc__)

        self.initGUI()


    def initGUI(self):

        self.setGeometry(700,500, 400,150)
        self.setWindowTitle('My Window')
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    _Win_ = _Window_()
    app.exec_()
    
