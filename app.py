from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

win_main = uic.loadUi('./ui/main.ui')
win_expense = uic.loadUi('./ui/expense.ui')
win_add = uic.loadUi('./ui/add.ui')

current_cash = 1000
week_cash = 800
peak_cash = 200



win_main.show()
app.exec()