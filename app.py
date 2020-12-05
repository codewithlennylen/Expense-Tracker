from PyQt5 import QtWidgets, uic
import sqlite3
import sys

app = QtWidgets.QApplication([])
db = sqlite3.connect('./data/database.db')
cur = db.cursor()

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
def db_add():
    # Get data from the Input Widgets
    source = win_add.ent_src.text()
    amount = win_add.ent_amt.text()
    print(f"Income Recorded: {source} {amount}")

def db_expense():
    # Get data from the Input Widgets
    usage = win_expense.ent_usage.text()
    amount = win_expense.ent_amt.text()
    print(f"Added to db:  {usage} {amount}")

def func_done():
    print("Back to main UI")

    # Hide all windows, show main window
    win_expense.hide()
    win_add.hide()
    win_main.show()

def show_win_expense():
    print("clicked")

    # Hide main window, show expense menu
    win_main.hide()
    win_expense.show()

def show_win_add():
    print("clicked")

    # Hide main window, show expense menu
    win_main.hide()
    win_add.show()

def fun_exit():
    """Exit the Application
    """
    print("See You Next Time!")
    db.close()
    sys.exit()

def fun_report():
    print("Coming Soon")

def event_handler():
    # Main Window - win_main
    win_main.act_expense.triggered.connect(show_win_expense) # Show the Window, Hide current Window
    win_main.act_report.triggered.connect(fun_report)
    win_main.act_add.triggered.connect(show_win_add)
    win_main.act_exit.triggered.connect(fun_exit)

    # Track Expense Window - win_expense
    win_expense.btn_track.clicked.connect(db_expense)
    win_expense.btn_done.clicked.connect(func_done)

    # Add Cash Window - win_add
    win_add.btn_add.clicked.connect(db_add)
    win_add.btn_done.clicked.connect(func_done)

def db_create_table():
    cur.execute("""CREATE TABLE expenditure(date TEXT, usage TEXT, amount INTEGER)""")

# db_create_table() # Ran once, that's it!
main_ui_load()
event_handler()
win_main.show()
app.exec()