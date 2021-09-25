from addStudent_gui import *
import sys

print("here1")
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = AddStudent_gui()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
