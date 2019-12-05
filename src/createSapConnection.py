from win32com.client import GetObject, CDispatch
import pandas as pd
import numpy as np


class SAP:

	def createSapConnection(self):

		sapGuiObject = GetObject("SAPGUI")
		if not type(sapGuiObject) == CDispatch:
			return

		sApplication = sapGuiObject.GetScriptingEngine
		if not type(sApplication) == CDispatch:
			sapGuiObject = None
			return

		connection = sApplication.Children(0)
		if not type(connection) == CDispatch:
			sApplication = None
			sapGuiObject = None
			return

		session = connection.Children(0)

		if not type(session) == CDispatch:
			connection = None
			sApplication = None
			sapGuiObject = None
			return
		if self:
			return session


class OEScript(SAP):
	def __init__(self):
		super(OEScript, self).__init__()

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


class PlanningScript(SAP):
	def __init__(self):
		super(PlanningScript, self).__init__()

	def createRRP4_report_planning(self):
		session = self.createSapConnection()
		session.findById("wnd[0]").iconify()
		session.findById("wnd[0]/tbar[0]/okcd").text = "/n/sapapo/rrp4"
		session.findById("wnd[0]/tbar[0]/btn[0]").press()
		session.findById("wnd[0]/tbar[1]/btn[17]").press()
		session.findById("wnd[1]/usr/txtV-LOW").text = "VN_SNP"
		session.findById("wnd[1]/tbar[0]/btn[8]").press()
		session.findById("wnd[0]/tbar[1]/btn[8]").press()


class EQScript(SAP):
	pass


class WHScript(SAP):
	pass
