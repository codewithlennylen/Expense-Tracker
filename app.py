from PyQt5 import QtWidgets, uic
import sqlite3
import datetime
import json
import sys

app = QtWidgets.QApplication([])
with open('./data/wallet.json','r') as wallet_file:
    wallet = json.load(wallet_file)
db = sqlite3.connect('./data/database.db')
cur = db.cursor()

win_main = uic.loadUi('./ui/main.ui')
win_expense = uic.loadUi('./ui/expense.ui')
win_add = uic.loadUi('./ui/add.ui')


def main_ui_load():
    # Get these variables from the 
    with open('./data/wallet.json','r') as wallet_file:
        wallet = json.load(wallet_file)
    current_cash = wallet["cash"]
    week_cash = wallet["week"]
    peak_cash = wallet["peak"]

    # set relevant labels
    win_main.lbl_current.setText(f"KES. {str(current_cash)}")
    win_main.lbl_topxp.setText(f"KES. {str(peak_cash)}")
    win_main.lbl_weekly.setText(f"KES. {str(week_cash)}")

    # Load data onto the Table Widget
    display_table_data()

def display_table_data():
    """Gets Data from The Database and displays it onto the Table Widget
    """
    rows = cur.execute("SELECT date,usage,amount FROM expenditure").fetchall()
    rows.reverse() # Reverse the order to get the most recent at the top
    print(rows)

    # Clear The Table
    # Failure to clear Data from the tableWidget will lead to duplication of Data
    win_main.table.clearSelection() # Clear any selection to avoid errors
    while(win_main.table.rowCount()>0):
        win_main.table.removeRow(0) # Remove all the rows
        win_main.table.clearSelection()

    # Iterate thru the data and create n new rows based on the number of products,n in the database
    for row, product in enumerate(rows):
        win_main.table.insertRow(row)
        # Iterate through the fields of a product and insert the item into a particular (row,column)
        for column, dataItem in enumerate(product):
            cellData = QtWidgets.QTableWidgetItem(str(dataItem)) # Format the data into a QTableWidgetItem Item!
            win_main.table.setItem(row, column, cellData)


# Functions - Implement Functionality ^_^
def db_add():
    global wallet
    # Get data from the Input Widgets
    date = get_date_day()
    source = win_add.ent_src.text()
    amount = win_add.ent_amt.text()

    # Add To Database
    try:
        # Track the Event into the Database
        cur.execute(f"""INSERT INTO expenditure(date, usage, amount) VALUES(?,?,?) """,(date, source, amount))
        db.commit()
        
        # Add The Cash to your Wallet
        wallet["cash"] = wallet["cash"] + int(amount)
        with open('./data/wallet.json','w') as wallet_file:
            json.dump(wallet, wallet_file)

        print(f"Added to db:  {source} {amount}")
    except Exception as e:
        print(f"Failed : {e}")

def db_expense():
    global wallet
    # Get data from the Input Widgets
    date = get_date_day()
    usage = win_expense.ent_usage.text()
    amount = win_expense.ent_amt.text()

    # Add To Database
    try:
        # Track the Event into the Database
        cur.execute(f"""INSERT INTO expenditure(date, usage, amount) VALUES(?,?,?) """,(date, usage, amount))
        db.commit()

        # Update the Wallet's State
        wallet["cash"] = wallet["cash"] - int(amount)
        wallet["week"] = wallet["week"] + int(amount)
        if int(amount) > wallet["peak"]: wallet["peak"] = amount
        with open('./data/wallet.json','w') as wallet_file:
            json.dump(wallet, wallet_file)

        # Success
        print(f"Added to db:  {usage} {amount}")
    except Exception as e:
        print(f"Failed : {e}")

def func_done():
    print("Back to main UI")

    # Hide all windows, show main window
    main_ui_load()
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

def get_date_day():
    """Returns the Current Date and Day of the Week
    """
    # Get the Date, .split[0] - Drop the Time
    date = str(datetime.datetime.now()).split()[0]
    week_days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    day_index = datetime.datetime.today().weekday() # 0-Mon, 6-Sun
    day = week_days[day_index]

    return f"{day} {date}"

def db_create_table():
    cur.execute("""CREATE TABLE expenditure(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, usage TEXT, amount INTEGER)""")
    
    # Instead of creating a new Table, use JSON!
    # cur.execute("""CREATE TABLE wallet(id INTEGER PRIMARY KEY AUTOINCREMENT, amount INTEGER)""")

# db_create_table() # Ran once, that's it!

# print(str(datetime.datetime.now()).split()[0])
# print(datetime.datetime.today().weekday()) # 
print(get_date_day())
main_ui_load()
event_handler()
win_main.show()
app.exec()