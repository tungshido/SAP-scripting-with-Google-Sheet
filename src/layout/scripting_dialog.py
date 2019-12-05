# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scripting_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from win32com.client import GetObject, CDispatch
from src.createSapConnection import SAP
import pandas as pd
import numpy as np


class Ui_Dialog(object):
	def __init__(self):
		super(Ui_Dialog, self).__init__()

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

	'''
	def createSapConnection(self):
		SapGuiAuto = GetObject("SAPGUI")
		if not type(SapGuiAuto) == CDispatch:
			return
		sApplication = SapGuiAuto.GetScriptingEngine
		if not type(sApplication) == CDispatch:
			SapGuiAuto = None
			return
		connection = sApplication.Children(0)
		if not type(connection) == CDispatch:
			sApplication = None
			SapGuiAuto = None
			return
		session = connection.Children(0)
		return session

	def pid_scripting(self):
		session = self.createSapConnection()
		pd.option_context('display.max_rows', None, 'display.max_columns', None)
		df = pd.read_excel("O:\\Shared drives\\VETMP_OE\\TEST_Script post PID.xlsx").replace(np.nan, '', regex=True)
		# print(df)

		mainRow = df.iat[2, 16]  # Cell contain number of Row in LI1N screen
		# storageLocation = df.iat[1,16] # Cell contain Storage Location Value
		PIDnumber = df.iat[0, 16]
		lastIndex = df.index[-1]  # Last Row value
		# print(LastIndex)
		page = lastIndex // mainRow  # Define number of pages that need to be used
		rest = lastIndex - (page * mainRow)

		# Open SAP T-code LI11N with warehouse "VMR" & PID number.

		session.findById("wnd[0]").maximize()
		session.findById("wnd[0]/tbar[0]/okcd").text = "/nLI11N"
		session.findById("wnd[0]").sendVKey(0)
		session.findById("wnd[0]/usr/ctxtLINV-LGNUM").text = "VMR"
		session.findById("wnd[0]/usr/txtLINV-IVNUM").text = PIDnumber
		session.findById("wnd[0]/usr/txtLINV-IVNUM").setFocus()
		session.findById("wnd[0]/usr/txtLINV-IVNUM").caretPosition = 5
		session.findById("wnd[0]/tbar[0]/btn[0]").press()
		# Input value from column "Actual Quantity" in xlsx file to column "Counted Quantity" in t-code LI11N
		for j in range(1, page + 2):
			if j > page:
				FirstRow = 0 + (page * mainRow)
				LastRow = lastIndex
			else:
				FirstRow = (mainRow * (j - 1))
				LastRow = mainRow - 1 + (mainRow * (j - 1))
			for i in range(FirstRow, LastRow + 1):
				if df.iloc[i]['Actual Quantity'] == 0:
					session.findById(
						"wnd[0]/usr/tblSAPML04ID2051/chkRL04I-KZNUL[8," + str(i - mainRow * (j - 1)) + "]").selected = True
				else:
					session.findById(
						"wnd[0]/usr/tblSAPML04ID2051/txtLINV-MENGA[6," + str(i - mainRow * (j - 1)) + "]").text = str(
						df.iloc[i]['Actual Quantity'])
			if j > page:
				session.findById("wnd[0]").sendVKey(0)
			else:
				session.findById("wnd[0]").sendVKey(82)
			for i in range(FirstRow, LastRow + 1):
				session.findById("wnd[0]").sendVKey(0)
		session.findById("wnd[0]/tbar[0]/btn[11]").press()

	def testSapScripting(self):
		session = self.createSapConnection()
		session.findById("wnd[0]").maximize()
		session.findById("wnd[0]/tbar[0]/okcd").text = "/nse16"
		session.findById("wnd[0]").sendVKey(0)
		session.findById("wnd[0]/usr/ctxtDATABROWSE-TABLENAME").text = "MARC"
		session.findById("wnd[0]").sendVKey(0)
		session.findById("wnd[0]/usr/ctxtI2-LOW").text = "VN11"
		session.findById("wnd[0]/usr/ctxtI2-LOW").setFocus()
		session.findById("wnd[0]/usr/ctxtI2-LOW").caretPosition = 4
		session.findById("wnd[0]/tbar[1]/btn[8]").press()
		session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").setCurrentCell(2, "WERKS")
		session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").contextMenu()
		session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectContextMenuItem("&XXL")
		session.findById("wnd[1]/tbar[0]/btn[0]").press()
		session.findById("wnd[1]/usr/ctxtDY_PATH").text = "C:\\Users\\Tung Hoang\\Documents"
		session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "test1.XLSX"
		session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
		session.findById("wnd[1]/tbar[0]/btn[0]").press()


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())
'''