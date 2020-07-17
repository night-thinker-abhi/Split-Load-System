# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ds2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(436, 418)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 31))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(60, 70, 321, 271))
        self.listView.setObjectName("listView")
        self.Refresh = QtWidgets.QPushButton(Form)
        self.Refresh.setGeometry(QtCore.QRect(60, 360, 91, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Refresh.setIcon(icon1)
        self.Refresh.setIconSize(QtCore.QSize(35, 35))
        self.Refresh.setCheckable(False)
        self.Refresh.setFlat(True)
        self.Refresh.setObjectName("pushButton")
        self.Next = QtWidgets.QPushButton(Form)
        self.Next.setGeometry(QtCore.QRect(310, 360, 81, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next.setIcon(icon2)
        self.Next.setIconSize(QtCore.QSize(35, 35))
        self.Next.setFlat(True)
        self.Next.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 81, 31))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Client List"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Master</span></p></body></html>"))
        self.Refresh.setText(_translate("Form", "Refresh"))
        self.Next.setText(_translate("Form", "Next"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Client List</span></p></body></html>"))
