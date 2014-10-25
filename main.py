__author__ = 'Christian'
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import class_tech,myButton


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        addTechAction = QtGui.QAction('Add tech', self)
        addTechAction.setShortcut('Ctrl+N')
        addTechAction.setStatusTip('Add new technology')
        addTechAction.triggered.connect(self.addWidget)

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exitAction)
        file_menu = menu_bar.addMenu('&Tools')
        file_menu.addAction(addTechAction)
        file_menu = menu_bar.addMenu('&Help')


        toolbar = self.addToolBar('Tools Exit')
        toolbar.addAction(exitAction)


        # main button
        #self.addButton = QtGui.QPushButton('button to add other widgets')
        #self.addButton.clicked.connect(self.addWidget)

        # scroll area widget contents - layout
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
        self.mainLayout.addWidget(self.scrollArea)

        # central widget
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # set central widget
        self.setCentralWidget(self.centralWidget)



        """
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')"""





        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('TechTreeWindow')
        self.show()

    def addWidget(self):
        self.scrollLayout.addRow(AddButton())

class AddButton(myButton.Button):
    def __init__( self, parent=None):
        super(AddButton, self).__init__(parent)
        self.setText("I am in Test widget")
        self.clicked.connect(self.deleteLater)

    def __del__(self):
        self.clicked.connect(self.deleteLater)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()

    newTech=class_tech.Tech(5)
    newTech.__setYear__(10)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()