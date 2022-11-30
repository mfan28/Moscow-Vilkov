import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.draw)
        
    def draw(self):
        self.canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(self.canvas)
        self.paint = QtGui.QPainter(self.label.pixmap())
        self.pen = QtGui.QPen()
        self.pen.setColor(QtGui.QColor(255,255,0))
        self.paint.setPen(self.pen)
        self.paint.drawEllipse(randint(0, 400), randint(0, 300), randint(0,100), randint(0, 100))
        self.paint.drawEllipse(randint(0, 400), randint(0, 300), randint(0,100), randint(0, 100))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())