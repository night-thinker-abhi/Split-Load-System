# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ds4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 20, 121, 16))
        self.label.setObjectName("label")
        self.downloadLink = QtWidgets.QTextEdit(Form)
        self.downloadLink.setGeometry(QtCore.QRect(30, 50, 341, 41))
        self.downloadLink.setObjectName("textEdit")
        self.Download = QtWidgets.QPushButton(Form)
        self.Download.setGeometry(QtCore.QRect(150, 110, 100, 28))
        self.Download.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Enter URL"))
        self.label.setText(_translate("Form", "Enter Download Link"))
        self.Download.setText(_translate("Form", "Download"))
