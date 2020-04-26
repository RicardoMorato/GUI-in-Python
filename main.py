from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super(MyWindow, self).__init__()
    self.setGeometry(200, 200, 400, 400)
    self.setWindowTitle("My new window")
    self.initUI()

  def initUI(self):
    self.count = 0
    self.label = QtWidgets.QLabel(self) # Here we set where our label will be shown
    self.label.setText("You clicked zero times!")
    # self.label.setText("parábens Ricardo a pessoa mais bonita que existe no mundo")
    self.label.adjustSize()
    self.label.move(10, 100)

    self.button_1 = QtWidgets.QPushButton(self)
    self.button_1.setText("Click me!")
    self.button_1.clicked.connect(self.clicked)

  def clicked(self):
    self.count += 1
    self.label.setText(f'You clicked {self.count} times!')
    self.update()

  def update(self):
    self.label.adjustSize()

def window():
  app = QApplication(sys.argv)
  win = MyWindow()
  win.show()
  sys.exit(app.exec_())

window()
