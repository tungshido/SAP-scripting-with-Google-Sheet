# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scripting_dialog_planning.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
    Dialog.setMinimumSize(QtCore.QSize(300, 300))
    Dialog.setMaximumSize(QtCore.QSize(300, 300))
    Dialog.setSizeGripEnabled(False)
    self.gridLayout = QtWidgets.QGridLayout(Dialog)
    self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
    self.gridLayout.setContentsMargins(12, -1, 12, -1)
    self.gridLayout.setObjectName("gridLayout")
    self.btn_RRP = QtWidgets.QPushButton(Dialog)
    self.btn_RRP.setDefault(False)
    self.btn_RRP.setFlat(False)
    self.btn_RRP.setObjectName("btn_PID")
    self.gridLayout.addWidget(self.btn_RRP, 0, 0, 1, 1)
    self.btn_Adjust = QtWidgets.QPushButton(Dialog)
    self.btn_Adjust.setDefault(False)
    self.btn_Adjust.setFlat(False)
    self.btn_Adjust.setObjectName("btn_PID_2")
    self.gridLayout.addWidget(self.btn_Adjust, 1, 0, 1, 1)

    self.retranslateUi(Dialog)
    QtCore.QMetaObject.connectSlotsByName(Dialog)

  def retranslateUi(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    Dialog.setWindowTitle(_translate("Dialog", "SAP scripting"))
    self.btn_RRP.setText(_translate("Dialog", "Create RRP4"))
    self.btn_Adjust.setText(_translate("Dialog", "Adjust Loading Date"))
