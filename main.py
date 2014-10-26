__author__ = 'Christian'
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import class_tech,myButton


# Tutorials I used for this so far:
#   For drag&drop
#       http://zetcode.com/gui/pyqt4/dragdrop/
#   for the dynamical creation of a button
#       http://stackoverflow.com/questions/8651742/dynamically-adding-and-removing-widgets-in-pyqt
#
#


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        addTechAction = QtGui.QAction(QtGui.QIcon('btn_tech.png'), 'add tech', self)
        addTechAction.setShortcut('Ctrl+N')
        addTechAction.setStatusTip('add new technology')
        addTechAction.triggered.connect(self.addWidget)

        # StatusBar
        self.statusBar()

        # MenuBar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exitAction)
        file_menu = menu_bar.addMenu('&Tools')
        file_menu.addAction(addTechAction)
        file_menu = menu_bar.addMenu('&Help')

        # ToolBar
        self.toolbar = self.addToolBar('Tools')
        self.toolbar.addAction(addTechAction)
        self.toolbar.addAction(exitAction)

        # Layout
        self.mainLayout = QtGui.QGridLayout()

        # central widget
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.setGeometry(600, 600, 250, 150)
        self.setWindowTitle('TechTreeWindow')

    # addWidget for a new button - create AddButton class
    def addWidget(self):
        self.mainLayout.addWidget(AddButton(), 0, 2)

class AddButton(QtGui.QWidget):
    def __init__( self, parent=None):
        super(AddButton, self).__init__(parent)

        self.setAcceptDrops(True)

        self.AddAButton = myButton.Button('Button')
        self.AddAButton.setFixedSize(50,25)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.AddAButton)
        self.setLayout(layout)

    def dragEnterEvent(self, e):

        e.accept()

    def dropEvent(self, e):

        position = e.pos()
        self.AddAButton.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()

    def __del__(self):
        self.clicked.connect(self.deleteLater)


def main():
    app = QtGui.QApplication(sys.argv)
    myWidget = MainWindow()
    myWidget.show()

    newTech=class_tech.Tech(5)
    newTech.__setYear__(10)

    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



""" # scroll area widget contents - layout
self.scrollLayout = QtGui.QFormLayout()
# scroll area widget contents
self.scrollWidget = QtGui.QWidget()
self.scrollWidget.setLayout(self.scrollLayout)
# scroll area
self.scrollArea = QtGui.QScrollArea()
self.scrollArea.setWidgetResizable(True)
self.scrollArea.setWidget(self.scrollWidget)

# main layout
self.mainLayout = QtGui.QVBoxLayout()

# add all main to the main vLayout
self.mainLayout.addWidget(self.scrollArea)"""