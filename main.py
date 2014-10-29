__author__ = 'Christian Gold'
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import class_tech,myButton


# Tutorials I used for this so far:
#   for drag&drop
#       http://zetcode.com/gui/pyqt4/dragdrop/
#   for the dynamical creation of a button
#       http://stackoverflow.com/questions/8651742/dynamically-adding-and-removing-widgets-in-pyqt
#       http://thecodeinn.blogspot.de/2013/09/dynamically-adding-objects-in-pyqt.html
#

count=1

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True)

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
        self.toolbar.setIconSize(QtCore.QSize(64,64))
        self.toolbar.addAction(addTechAction)
        self.toolbar.addAction(exitAction)

        # Layout
        self.mainLayout = QtGui.QGridLayout()

        # central widget
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.setFixedSize(640, 480)
        self.setWindowTitle('TechTreeWindow')

    # addWidget for a new button - create AddButton class
    def addWidget(self):
        global count

        self.b = myButton.Button(str(count),self)
        self.b.clicked.connect(self.Button)
        self.b.setFixedSize(40,40)

        self.mainLayout.addWidget(self.b,count,0)

        count += 1


    def dragEnterEvent(self, e):

        e.accept()

    def dropEvent(self, e):

        position = e.pos()
        self.b.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()

    def Button(self):

        sender = self.sender()

        print(sender.text())

def main():
    app = QtGui.QApplication(sys.argv)
    myWidget = MainWindow()
    myWidget.show()

    #Techclass
    #newTech=class_tech.Tech(5)
    #newTech.__setYear__(10)

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