from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

win_main = uic.loadUi('./ui/main.ui')
win_expense = uic.loadUi('./ui/expense.ui')
win_add = uic.loadUi('./ui/add.ui')

# Get these variables from the database
current_cash = 1000
week_cash = 800
peak_cash = 250

def main_ui_load():
    # set relevant labels
    win_main.lbl_current.setText(f"KES. {str(current_cash)}")
    win_main.lbl_topxp.setText(f"KES. {str(peak_cash)}")
    win_main.lbl_weekly.setText(f"KES. {str(week_cash)}")

def expense_ui_load():
    # Might Be Irrelevant > We only need to process data not Display!
    pass


# Functions - Implement Functionality ^_^
def fun_add_expense():
    print("clicked")

def fun_add_money():
    print("clicked")

def fun_exit():
    print("clicked")

def fun_report():
    print("Coming Soon")

def event_handler():
    # Main Window - win_main
    win_main.actionAdd_Expense.clicked.connect(fun_add_expense) # Show the Window, Hide current Window
    win_main.actionGenerate_Report.clicked.connect(fun_report)
    win_main.actionAdd_Money.clicked.connect(fun_add_money)
    win_main.actionExit.clicked.connect(fun_exit)


main_ui_load()
win_main.show()
app.exec()