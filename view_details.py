from sys import exit
from rich.console import Console
from rich.table import Table
import sqlite3
console = Console()


class view_details:
    @classmethod
    def __init__(self):
       self.__book_file=None
       self.__login_file=None

    def choice_view():
        while True:
            view=int(input("Please Enter to View \n1.Login Details\n2.Booking Details\n3.Exit\nHere: "))
            if view==1:
                view_details().login_details()
            elif view==2:
                view_details().booking_details()
            elif view==3:
                exit(0)
            else:
                print("Invalid Choice")     


    def booking_details(self):
        self.__book_file = open('booking.csv', 'r')
        table = Table(title="Booking Details")
        table.add_column("Token")
        table.add_column("Name")
        table.add_column("Service")
        table.add_column("Date")
        
        conn = sqlite3.connect('diagnostics.db')

        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM booking_details')
        rows = cursor.fetchall()
        data=''
        for row in rows:
            if(row[2]=='0'):
                data='Scanning'
            elif(row[2]=='1'):
                data='X-ray'
            else:
                data='Testing'
            table.add_row(str(row[0]),row[1],data,row[3],style='bright_green')
        console.print("\n",table)

    def login_details(self):
        self.__login_file = open('accounts.csv', 'r')
        table = Table(title="Login Details")
        table.add_column("ID")
        table.add_column("Email")
        table.add_column("Password")
        conn = sqlite3.connect('diagnostics.db')

        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            table.add_row(str(row[0]),row[1],row[2],style='bright_green')
        console = Console()
        console.print("\n",table)