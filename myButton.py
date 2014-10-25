__author__ = 'Christian'

import sys
from PySide import QtCore, QtGui

class Button(QtGui.QPushButton):

    def __init__(self, title):
        super(Button, self).__init__(title)

    def mouseMoveEvent(self, e):

        if e.buttons() != QtCore.Qt.RightButton:
            return

        mimeData = QtCore.QMimeData()

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.start(QtCore.Qt.MoveAction)

    def mousePressEvent(self, e):

        super(Button, self).mousePressEvent(e)

        if e.button() == QtCore.Qt.LeftButton:
            print('press')