from PyQt5 import QtWidgets, uic
import sys

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
    """Exit the Application
    """
    print("See You Next Time!")
    sys.exit()

def fun_report():
    print("Coming Soon")

def event_handler():
    # Main Window - win_main
    win_main.act_expense.triggered.connect(fun_add_expense) # Show the Window, Hide current Window
    win_main.act_report.triggered.connect(fun_report)
    win_main.act_add.triggered.connect(fun_add_money)
    win_main.act_exit.triggered.connect(fun_exit)


main_ui_load()
event_handler()
win_main.show()
app.exec()



# toolbar = QToolBar("My main toolbar")
# self.addToolBar(toolbar)

# button_action = QAction("Your button", self)
# button_action.setStatusTip("This is your button")
# button_action.triggered.connect(self.onMyToolBarButtonClick)
# toolbar.addAction(button_action)
