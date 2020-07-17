# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ds1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(311, 255)
        Form.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.Master = QtWidgets.QPushButton(Form)
        self.Master.setGeometry(QtCore.QRect(30, 180, 111, 31))
        self.Master.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Master.setToolTipDuration(2)
        self.Master.setAutoFillBackground(False)
        self.Master.setAutoDefault(True)
        self.Master.setFlat(False)
        self.Master.setObjectName("Master")
        self.Client = QtWidgets.QPushButton(Form)
        self.Client.setGeometry(QtCore.QRect(170, 180, 111, 31))
        self.Client.setObjectName("Client")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 140, 311, 20))
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 311, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 50, 55, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons/download.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SplitLoad"))
        self.Master.setToolTip(_translate("Form", "Start a new Download by providing Link"))
        self.Master.setText(_translate("Form", "Start Download"))
        self.Client.setText(_translate("Form", "Serve Download"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Use this System to:</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SplitLoad</span></p></body></html>"))
