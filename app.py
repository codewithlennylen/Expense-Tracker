from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

win_main = uic.loadUi('./ui/main.ui')
win_expense = uic.loadUi('./ui/expense.ui')
win_add = uic.loadUi('./ui/add.ui')

win_add.show()
app.exec()