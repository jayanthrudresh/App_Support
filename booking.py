from time import sleep as wait
import datetime
from rich.console import Console
from rich.table import Table
import sqlite3

class book:
    def __init__(self):
        self.__name=""
        self.__ser=0
        self.__date_time=""

    def booking(self):
        while(True):
            ser_name=["Scanning","X-ray","Testing"]
            self.__name=input("Enter Patient Name: ")
            self.__ser=int(input("Please enter \n0.Scanning\n1.X-ray\n2.Testing\nHere: "))
            self.__date_time=input("Enter date(date-month-year): ")
            try:
                datetime.datetime.strptime(self.__date_time, '%d-%m-%Y')
            except ValueError:
                print("Incorrect date string")
            else:
                if self.__ser>=0 and self.__ser<=len(ser_name):
                    table = Table(title="Booking Confirmed")
                    table.add_column("Token No")
                    table.add_column("Name")
                    table.add_column("Service")
                    table.add_column("Date")
                    console = Console()
                    conn = sqlite3.connect('diagnostics.db')
                    cursor = conn.cursor()

                    # Create a table if it doesn't exist
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS booking_details (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            service TEXT,
                            date TEXT
                        )
                    ''')

                    cursor.execute('''
                    INSERT INTO booking_details (name, service, date)
                    VALUES (?, ?, ?)
                    ''', (self.__name,self.__ser,self.__date_time))


                    # Commit the changes to the database
                    conn.commit()
                   
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
                        table.add_row(str(row[0]),row[1],data,row[3])
                    console.print("\n",table)
                    cursor.close()
                    conn.close()
                    if(self.__ser=='0'):
                        data='Scanning'
                    elif(self.__ser=='1'):
                        data='X-ray'
                    else:
                        data='Testing'
                    print('{0} your {1} is scheduled on {2}'.format(self.__name,data,self.__date_time))
                    print("\n_____Thank You!_____")
                    wait(2)
                    break
                else:
                    print("wrong choice")