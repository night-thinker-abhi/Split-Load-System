# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ds5.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 70, 381, 51))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(163, 140, 100, 91))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap("icons/giphy.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 381, 61))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(14, 149, 371, 51))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setWordWrap(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Download"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Downloading</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>File Name : </p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>File Downloaded at : </p></body></html>"))
        self.label_2.setText(_translate("Downloading", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        movie = QtGui.QMovie("icons/loading.gif")
        self.label_2.setMovie(movie)
        movie.start()
        self.label_2.setLayout(QtWidgets.QHBoxLayout())

    def changeText(self, text:str, color:str='black'):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:{color}; font-weight:600;\">{text}</span></p></body></html>"))

    def changeTextFilename(self, text:str):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Form", f"<html><head/><body>{text}</body></html>"))

    def changeTextDownloadedAt(self, text:str):
        _translate = QtCore.QCoreApplication.translate
        self.label_4.setText(_translate("Form", f"<html><head/><body>{text}</body></html>"))