# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scripting_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.setEnabled(True)
		Dialog.resize(300, 300)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
		Dialog.setSizePolicy(sizePolicy)
		Dialog.setMaximumSize(QtCore.QSize(300, 300))
		Dialog.setSizeGripEnabled(False)
		self.gridLayout = QtWidgets.QGridLayout(Dialog)
		self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.gridLayout.setContentsMargins(12, -1, 12, -1)
		self.gridLayout.setObjectName("gridLayout")
		self.btn_PID = QtWidgets.QPushButton(Dialog)
		self.btn_PID.setDefault(False)
		self.btn_PID.setFlat(False)
		self.btn_PID.setObjectName("btn_PID")
		self.gridLayout.addWidget(self.btn_PID, 0, 0, 1, 1)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "SAP scripting"))
		self.btn_PID.setText(_translate("Dialog", "PID scripting"))
