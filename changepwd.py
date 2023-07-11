import re
import pandas as pd
import maskpass
import sqlite3

class password:
    def __init__(self):
        self.__password = None

    def setpassword(self,email, password):
        try:
            conn = sqlite3.connect('diagnostics.db')
            cursor = conn.cursor()

            # Execute an UPDATE statement to change the password
            cursor.execute('UPDATE users SET password=? WHERE email=?', (password, email))

            # Commit the changes to the database
            conn.commit()

            # Close the cursor and the connection
            cursor.close()
            conn.close()

            print('Password changed successfully!')
        except:
            print("Somthing Went Wrong **Password not changed**")
def main():
    while True:
        pwd_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email=input("Enter Your Email: ")
        pwd_cmp = re.compile(pwd_reg) 
        if(re.fullmatch(email_regex, email)):
            conn = sqlite3.connect('diagnostics.db')

            # Create a cursor object to execute SQL statements
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM users')
            rows = cursor.fetchall()
            for row in rows:
                if (email==row[1]):
                    while True:
                        new_password=str(maskpass.askpass(prompt='Enter New Password: ', mask="*"))
                        if re.search(pwd_cmp,new_password):
                            password().setpassword(email,new_password)
                            exit(0)
                        else:
                            print("Please Enter Password correctly")
            else:
                print("Email Has Not Registered")
                break
        else:
            print("Please Check Your Email")