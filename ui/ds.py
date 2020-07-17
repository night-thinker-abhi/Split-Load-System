import ds1,ds1,ds3
from PyQt5 import QtCore, QtGui, QtWidgets
ui1 = "abc"
ui2="abc"
ui3="abc"
def abc():
	ui1.label.setText("abc")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui1 = ds1.Ui_Form()
    ui1.setupUi(Form)
    ui1.Master.clicked.connect(abc)
    ui1.Client.clicked.connect(abc)
    Form.show()
    sys.exit(app.exec_())