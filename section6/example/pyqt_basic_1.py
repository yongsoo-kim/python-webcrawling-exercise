import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
#print(sys.argv)  # current path

label = QLabel("PyQT First Test")
label.show()


print("Before Loop")
app.exec_()
print("After Loop")
