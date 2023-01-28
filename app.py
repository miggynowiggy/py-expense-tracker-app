import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem
)
from expense_tracker import Ui_Form

class Window(QMainWindow, Ui_Form):
  expenses = [
    {"description": "Electricity", "amount": 2750.02, "type": "Bill"},
    {"description": "Water", "amount": 501.82, "type": "Bill"},
    {"description": "Internet", "amount": 1500.00, "type": "Bill"},
  ]

  def __init__(self, parent=None):
    super().__init__(parent)
    self.setupUi(self)
    self.addExpense.clicked.connect(self.handleAddExpense)
    self.deleteExpense.clicked.connect(self.handleDeleteExpense)
    self.populateTable()
  
  # Custom Methods for interacting with the expenses table
  def valid(self):
    description = self.expenseDescription.text().strip()
    amount = self.expenseAmount.text().strip()
    expenseType = self.expenseType.currentText()

    if not description:
        QMessageBox.critical(
            self, 'Error', 'Provide a description')
        return False
    elif not amount:
        QMessageBox.critical(self, "Error", "Provide an amount")
        return False
    elif not expenseType:
        QMessageBox.critical(
            self, "Error", "Select an expense type")
        return False

    return True

  def resetFields(self):
    self.expenseDescription.clear()
    self.expenseAmount.clear()
    self.expenseType.setCurrentIndex(0)

  def addExpenseEntry(self, description, amount, expenseType):
    if self.valid == False:
        return

    row = self.expensesTable.rowCount()
    self.expensesTable.insertRow(row)
    self.expensesTable.setItem(
        row, 0, QTableWidgetItem(description))
    self.expensesTable.setItem(
        row, 1, QTableWidgetItem(expenseType))
    self.expensesTable.setItem(
        row, 2, QTableWidgetItem(str(amount)))
    self.resetFields()

  def setTotal(self, amount):
    total = "TOTAL EXPENSE: {:.2f}"
    self.totalExpenses.setText(total.format(float(amount)))

  def getDescription(self):
    description = self.expenseDescription.text().strip()
    return description

  def getAmount(self):
    amount = self.expenseAmount.text()
    return float(amount)

  def getExpenseType(self):
    expType = self.expenseType.currentText()
    return expType

  def populateTable(self):
    for e in self.expenses:
      self.addExpenseEntry(description=e["description"], amount=e["amount"], expenseType=e["type"])
    self.computeTotal()
  
  def computeTotal(self):
    sum = 0.0
    for e in self.expenses:
      sum += float(e["amount"])

    self.setTotal(sum)

  def handleAddExpense(self):
    description = self.getDescription()
    amount = self.getAmount()
    expType = self.getExpenseType()

    self.expenses.append({
      "description": description,
      "amount": amount,
      "type": expType
    })

    self.addExpenseEntry(description=description, amount=amount, expenseType=expType)
    self.computeTotal()

  def handleDeleteExpense(self):
    selectedRow = self.expensesTable.currentRow()
    if selectedRow < 0:
      return QMessageBox.warning(self, "Warning", "Select an expense to delete")
    
    button = QMessageBox.question(
      self,
      "Confirmation",
      "Are you sure you want to delete the expense",
      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )

    if button == QMessageBox.StandardButton.Yes:
      self.expensesTable.removeRow(selectedRow)
      self.expenses.pop(selectedRow)
      self.computeTotal()

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())