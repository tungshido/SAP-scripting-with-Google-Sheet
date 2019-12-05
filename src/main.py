import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QMessageBox, QDialog
from src.layout.login_window1 import Ui_MainWindow as login_Window
from src.layout.scripting_dialog import Ui_Dialog as scripting_Oe
from src.layout.scripting_dialog_planning import Ui_Dialog as scripting_Planning
from PyQt5 import QtCore, QtGui
from src.createSapConnection import SAP

class Login(QMainWindow, login_Window):
	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)

		self.btn_login.clicked.connect(self.handlelogin)

	def switchDepartment(self, argument):

		self.oeUser = {
			"OE_1": "OE@1234",
			"OE_2": "OE@1234",
			"OE_3": "OE@1234"
		}
		self.planningUser = {
			"SP_SNP_01": "SNP@1234",
			"SP_SNP_02": "SNP@1234",
			"SP_MRP_01": "MRP@1234",
			"SP_MRP_02": "MRP@1234",
			"SP_PP_01": "PP@1234",
			"SP_PP_02": "PP@1234",
			"SP_PP_03": "PP@1234",
			"SP_PP_04": "PP@1234",

		}
		self.warehouseUser = {
			"WHGR": "WHGR@1234",
			"WHGI": "WHGI@1234",
			"WHLG": "WHLG@1234"
		}
		self.eqUser = {
			"EQ_01": "EQ@12345",
			"EQ_02": "EQ@12345",
			"EQ_03": "EQ@12345",
			"EQ_04": "EQ@12345",
			"EQ_05": "EQ@12345",
		}
		switcher = {
			"OE": self.oeUser,
			"Planning": self.planningUser,
			"Warehouse": self.warehouseUser,
			"Equipment": self.eqUser
		}
		return switcher.get(argument)

	def handlelogin(self):
		self.userDict = self.switchDepartment(self.cbx_department.currentText())
		if self.userDict.get(self.txt_username.text()) == self.txt_password.text():
			self.switch_window.emit()
			self.hide()
		else:
			QMessageBox.warning(self, 'Error', 'Sai tên đăng nhập hoặc mật khẩu!!!')


class ScriptingPlanning(QDialog, scripting_Planning, SAP):
	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
		self.btn_RRP.clicked.connect(self.pushbutton_handler_planning)

	def pushbutton_handler_planning(self):
		self.hide()
		self.show()
		self.testSapScripting()


class ScriptingOe(QDialog, scripting_Oe, SAP):
	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
		self.btn_PID.clicked.connect(self.pushbutton_handler_oe)

	def pushbutton_handler_oe(self):
		self.hide()
		self.show()
		self.testSapScripting()


class Controller:

	def __init__(self):
		pass

	def show_login(self):
		self.login = Login()
		self.login.switch_window.connect(self.show_main)
		self.login.show()

	def show_main(self):
		switcher = {
			"OE": ScriptingOe(),
			"Planning": ScriptingPlanning()
		}
		self.dialog = switcher.get(self.login.cbx_department.currentText())
		self.dialog.switch_window.connect(self.show_login)
		self.login.close()
		self.dialog.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	controller = Controller()
	controller.show_login()
	sys.exit(app.exec_())
