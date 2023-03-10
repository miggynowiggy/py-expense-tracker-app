# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expense_tracker.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(800, 800)
        Form.setMinimumSize(QtCore.QSize(800, 800))
        Form.setWindowOpacity(3.0)
        self.main = QtWidgets.QScrollArea(Form)
        self.main.setGeometry(QtCore.QRect(0, 0, 801, 951))
        self.main.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.main.setWidgetResizable(True)
        self.main.setObjectName("main")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 949))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.windowTitle = QtWidgets.QTextBrowser(self.frame)
        self.windowTitle.setGeometry(QtCore.QRect(0, 0, 801, 71))
        self.windowTitle.setObjectName("windowTitle")
        self.expenseTableScroll = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.expenseTableScroll.setGeometry(QtCore.QRect(0, 100, 801, 381))
        self.expenseTableScroll.setWidgetResizable(True)
        self.expenseTableScroll.setObjectName("expenseTableScroll")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 799, 379))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.expensesTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.expensesTable.setGeometry(QtCore.QRect(0, 0, 801, 381))
        self.expensesTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.expensesTable.setAlternatingRowColors(True)
        self.expensesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.expensesTable.setObjectName("expensesTable")
        self.expensesTable.setColumnCount(3)
        self.expensesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.expensesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.expensesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.expensesTable.setHorizontalHeaderItem(2, item)
        self.expensesTable.horizontalHeader().setCascadingSectionResizes(False)
        self.expensesTable.horizontalHeader().setDefaultSectionSize(265)
        self.expenseTableScroll.setWidget(self.scrollAreaWidgetContents_2)
        self.formLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 550, 781, 100))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.expenseDescription = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.expenseDescription.setClearButtonEnabled(True)
        self.expenseDescription.setObjectName("expenseDescription")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.expenseDescription)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.expenseAmount = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.expenseAmount.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.expenseAmount.setObjectName("expenseAmount")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.expenseAmount)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.expenseType = QtWidgets.QComboBox(self.formLayoutWidget)
        self.expenseType.setObjectName("expenseType")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.expenseType.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.expenseType)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 640, 781, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addExpense = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addExpense.setDefault(True)
        self.addExpense.setFlat(False)
        self.addExpense.setObjectName("addExpense")
        self.horizontalLayout.addWidget(self.addExpense)
        self.totalExpenses = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.totalExpenses.setGeometry(QtCore.QRect(550, 500, 241, 31))
        self.totalExpenses.setObjectName("totalExpenses")
        self.deleteExpense = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.deleteExpense.setGeometry(QtCore.QRect(10, 510, 181, 23))
        self.deleteExpense.setObjectName("deleteExpense")
        self.dateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit.setGeometry(QtCore.QRect(680, 690, 101, 20))
        self.dateEdit.setObjectName("dateEdit")
        self.main.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.expenseDescription, self.expenseAmount)
        Form.setTabOrder(self.expenseAmount, self.expenseType)
        Form.setTabOrder(self.expenseType, self.addExpense)
        Form.setTabOrder(self.addExpense, self.totalExpenses)
        Form.setTabOrder(self.totalExpenses, self.deleteExpense)
        Form.setTabOrder(self.deleteExpense, self.expenseTableScroll)
        Form.setTabOrder(self.expenseTableScroll, self.main)
        Form.setTabOrder(self.main, self.windowTitle)
        Form.setTabOrder(self.windowTitle, self.expensesTable)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "My Expense Tracker"))
        self.main.setToolTip(_translate("Form", "<html><head/><body><p>Enter amount of your expense</p></body></html>"))
        self.windowTitle.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#40a6cb;\">Expense Tracker</span></p></body></html>"))
        self.expensesTable.setSortingEnabled(True)
        item = self.expensesTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Description"))
        item = self.expensesTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type"))
        item = self.expensesTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Amount"))
        self.label.setText(_translate("Form", "Expense Description"))
        self.expenseDescription.setPlaceholderText(_translate("Form", "Enter description of your expense"))
        self.label_2.setText(_translate("Form", "Amount"))
        self.expenseAmount.setPlaceholderText(_translate("Form", "Enter amount of your expense"))
        self.label_3.setText(_translate("Form", "Expense Type"))
        self.expenseType.setPlaceholderText(_translate("Form", "Select  type of your expense"))
        self.expenseType.setItemText(0, _translate("Form", "Bills"))
        self.expenseType.setItemText(1, _translate("Form", "Transportation"))
        self.expenseType.setItemText(2, _translate("Form", "Grocery"))
        self.expenseType.setItemText(3, _translate("Form", "Meal"))
        self.expenseType.setItemText(4, _translate("Form", "Emergency"))
        self.expenseType.setItemText(5, _translate("Form", "Payment"))
        self.expenseType.setItemText(6, _translate("Form", "Rent"))
        self.expenseType.setItemText(7, _translate("Form", "Insurance"))
        self.expenseType.setItemText(8, _translate("Form", "Government Contributions"))
        self.expenseType.setItemText(9, _translate("Form", "Tax"))
        self.addExpense.setText(_translate("Form", "Add Expense"))
        self.totalExpenses.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">TOTAL: 0.00</span></p></body></html>"))
        self.deleteExpense.setText(_translate("Form", "Delete Expense"))
