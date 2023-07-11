import sqlite3
import maskpass
from view_details import view_details


class admin:
    def __init__(self):
        self.__email=""
        self.__password=""


    def check_login(email, password):
        conn = sqlite3.connect('diagnostics.db')
        cursor = conn.cursor()

        # Execute a SELECT statement to check login details
        cursor.execute('SELECT COUNT(*) FROM admin WHERE email=? AND password=?', (email, password))
        result = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        # Check if a user with the provided login details exists
        if result[0] > 0:
            return True
        else:
            return False

    def admin_login(self):
        self.__email = str(input('Email: '))
        self.__password = str(maskpass.askpass(prompt='Password: ', mask="*"))    
        if admin.check_login(self.__email,self.__password):
            print('-----------------------------------Logged in successfully!---------------------------------\n')
            view_details.choice_view()   
        print("Sorry, you aren't signed up yet.")
        admin().admin_login()