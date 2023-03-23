import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from Solution import solution
from Plot import show

class Application(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Heat Transport")
        self.setGeometry(50, 50, 600, 300)
        self.setFixedSize(600, 300)
        self.setStyleSheet("background-color: lightgray;")
        self.label = QtWidgets.QLabel("Heat Transport", self)
        self.label.setFont(QtGui.QFont("Arial", 25))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(0, 40, 600, 40)
        self.input_label = QtWidgets.QLabel("Input number of elements", self)
        self.input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.input_label.setGeometry(0, 120, 600, 40)
        self.entry = QtWidgets.QLineEdit(self)
        self.entry.setFixedWidth(180)
        self.entry.setFixedHeight(40)
        self.entry.setAlignment(QtCore.Qt.AlignCenter)
        self.entry.move(210, 170)
        self.button = QtWidgets.QPushButton("Confirm", self)
        self.button.clicked.connect(self.solution)
        self.button.setFixedWidth(100)
        self.button.setFixedHeight(40)
        self.button.setStyleSheet("background-color: green; color: white;")
        self.button.setGeometry(250, 260, 100, 40)
        self.entry.returnPressed.connect(self.button.click)
        self.show()

    def solution(self):
        try:
            nof = int(self.entry.text())
            if nof < 2: raise Exception("number of elements must be greater than 2")
            x = [(2 / nof) * i for i in range(nof+1)]
            y = solution(nof)
            show(x, y)
        except:
            QtWidgets.QMessageBox.warning(self, "Error", "Incorrect input data")

app = QtWidgets.QApplication(sys.argv)
application = Application()
sys.exit(app.exec_())