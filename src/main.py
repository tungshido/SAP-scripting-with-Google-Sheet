import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QMessageBox, QDialog
from src.layout.login_window import Ui_MainWindow as login_Window
from src.layout.scripting_dialog_oe import Ui_Dialog as scripting_Oe_Gui
from src.layout.scripting_dialog_planning import Ui_Dialog as scripting_Planning_Gui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from src.createSapConnection import OEScript, PlanningScript
from functools import partial


class Login(QMainWindow, login_Window):
	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.btn_login.clicked.connect(self.handlelogin)
		self.btn_credit.clicked.connect(self.showCredit)
		self.oeUser = {
			"OE_1": "OE@1234",
			"OE_2": "OE@1234",
			"OE_3": "OE@1234",
			"admin": "admin"
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
			"admin": "admin"

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

	def showCredit(self):
		creditBox = QMessageBox()
		creditBox.setIcon(QMessageBox.Information)
		creditBox.setWindowTitle("Credit")
		creditBox.setText(
			"<p align='center'><b>This tool is created by Python Pioneers team - My Phuoc plant</b><br><br>""Tung Hoang - "
			"Digital Engineer - tung_hoang@colpal.com<br>Xuan Thanh Nguyen - OE engineer - "
			"xuan_thanh_nguyen@colpal.com<br>Phat Nguyen Huu - Planning Officer - phat_nguyen_huu@colpal.com</p>")

		creditBox.exec()
		return self

	def switchDepartment(self, argument):
		switcher = {
			"OE": self.oeUser,
			"Planning": self.planningUser,
			"Warehouse": self.warehouseUser,
			"Equipment": self.eqUser
		}
		return switcher.get(argument)

	def handlelogin(self):
		userDict = self.switchDepartment(self.cbx_department.currentText())
		if userDict.get(self.txt_username.text()) == self.txt_password.text():
			self.switch_window.emit()
			self.hide()
		else:
			QMessageBox.warning(self, 'Error', 'Sai tên đăng nhập hoặc mật khẩu!!!')
		return self


class MessageBoxConfirmation:
	def __init__(self, script_method, script_name):
		self.scriptingMethod = script_method
		self.scriptingName = script_name

	def showConfirmationAndExecuteScript(self):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setText(f"Bạn có chắc muốn thực hiện script {self.scriptingName}, Hãy đảm bảo SAP đã được bật")
		msgBox.setWindowTitle(f"Xác nhận thực hiện")
		msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

		returnValue = msgBox.exec()
		if returnValue == QMessageBox.Ok:
			self.scriptingMethod()
		else:
			msgBox.hide()


class ScriptingPlanning(QDialog, scripting_Planning_Gui, PlanningScript, MessageBoxConfirmation):
	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
		self.btn_RRP.clicked.connect(partial(self.pushbutton_handler_planning, self.createRRP4_report_planning, "RRP4"))
		MessageBoxConfirmation.__init__(self, script_method=None, script_name=None)

	@pyqtSlot()
	def pushbutton_handler_planning(self, sap_script_method, sap_script_name):
		msgBox = MessageBoxConfirmation(script_method=sap_script_method, script_name=sap_script_name)
		msgBox.showConfirmationAndExecuteScript()
		self.hide()
		self.show()
		return self


class ScriptingOe(QDialog, scripting_Oe_Gui, OEScript, MessageBoxConfirmation):
	switch_window = QtCore.pyqtSignal()

	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
		self.btn_PID.clicked.connect(partial(self.pushbutton_handler_oe, self.testSapScripting, "PID"))
		MessageBoxConfirmation.__init__(self, script_method=None, script_name=None)

	@pyqtSlot()
	def pushbutton_handler_oe(self, sap_script_method, sap_script_name):
		msgBox = MessageBoxConfirmation(script_method=sap_script_method, script_name=sap_script_name)
		msgBox.showConfirmationAndExecuteScript()
		self.hide()
		self.show()
		return self


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
