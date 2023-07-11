from sys import exit
import re
import maskpass
import booking
import changepwd
import sqlite3

def choice_method():
    print("-----------------------------------Welcome User--------------------------------------------")
    while(True):
        print("Please Enter Choice Given \n1.Login\n2.Register\n3.Change Password\n4.Exit")
        try:
            choice=int(input("Enter Here: "))
        except:
            print("XXXXXX---Warning---XXXXXX\nPlease Follow The Instruction Correctly")
        else:
            if choice==1:
                auth.login()
                break
            elif choice==2:
                auth.sign_up()
                break
            elif choice==3:
                changepwd.main()
                break
            elif choice==4:
                exit
                break
            else:
                print("XXXXXX---Warning---XXXXXX\ninvalid choise\nEnter The Choice Correctly")

class auth:
    def login():
        email = str(input('Email: '))
        password = str(maskpass.askpass(prompt='Password: ', mask="*"))   
        if auth.check_login(email, password):
            print('-----------------------------------Logged in successfully!---------------------------------\n')
            print('                              *********Booking Details*********                            ')
            booking.book().booking()
            exit(0)
        print("Sorry, you aren't signed up yet.")
        choice_method()

    def sign_up():
        while True:
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            pwd_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            ph_pattern = re.compile("(0|91)?[6-9][0-9]{9}")
            pwd_cmp = re.compile(pwd_reg)                
            email = str(input('Email: '))
            password = str(maskpass.askpass(prompt='Password: ', mask="*"))
            re_password= str(maskpass.askpass(prompt='Re-Enter Password: ', mask="*"))
            phone_no=input('Ph_No: ')
            if(re.fullmatch(email_regex, email) and re.search(pwd_cmp,password) and ph_pattern.match(phone_no)):
                if(password==re_password):
                    conn = sqlite3.connect('diagnostics.db')

                    # Create a cursor object to execute SQL statements
                    cursor = conn.cursor()

                    # Execute SQL statements
                    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT,
                        password TEXT
                    )''')
                    cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))

                    # Commit the changes to the database
                    conn.commit()
                    print('Do you want to log in? [Yes/No]')
                    start_over = str(input()).lower()
                    if 'y' in start_over:
                        auth.login()
                    else:
                        choice_method()
                        break
                else:
                   print("Password doesnot match")
            else:
                print("Please enter the valid email and password and ph number")
    

    def check_login(email, password):
        conn = sqlite3.connect('diagnostics.db')
        cursor = conn.cursor()

        # Execute a SELECT statement to check login details
        cursor.execute('SELECT COUNT(*) FROM users WHERE email=? AND password=?', (email, password))
        result = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        # Check if a user with the provided login details exists
        if result[0] > 0:
            return True
        else:
            return False

