import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore


# QtWidgets -> Default
# QMainWindow -> Default with menu bar and control bar


class TestForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(800, 400, 500, 500)  # X axis, Y axis, width, height

        label_1 = QLabel("Input test", self)
        label_2 = QLabel("Output test", self)

        label_1.move(20, 20)
        label_2.move(20, 60)

        self.lineEdit = QLineEdit("", self)  # Default is ""
        self.plainEdit = QtWidgets.QPlainTextEdit(self)
        self.plainEdit.setReadOnly(True)

        self.lineEdit.move(90, 20)
        self.plainEdit.setGeometry(QtCore.QRect(20, 90, 361, 231))

        self.lineEdit.textChanged.connect(self.lineEditChanged)
        self.lineEdit.returnPressed.connect(self.lineEditEnter)

        # Status bar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

    def lineEditEnter(self):
        self.plainEdit.appendPlainText(self.lineEdit.text()) #insertPlainText -> This can be used too, but it won't add line breaks(\n)
        self.lineEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
