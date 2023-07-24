#Title of the application :Organic Product Ordering System
#Author:Vaishnavi G
#Created on:18/02/23
#Last Modified Date:22/02/23
#Reviwed By:
#Reviewed On:
from validate import Validate
from category import Category 
from category import Menu 
#from login import menu 
print("\n\n\t******** W E L C O M E   TO   O R G A N I C   P R O D U C T   S A L E ********\n") 
print(" ___________________________") 
print("|        SIGNUP/LOGIN       |") 
print("|__________1______2_________|") 
choice=int(input("\nchoose 1 or 2:")) 
if choice==1: 
    s=Validate() 
    s.signup() 
    s.login() 
    m=Menu 
    c=Category 
    m.order_menu() 
    print("H A V E   A   N I C E   D A Y") 
elif(choice==2): 
    s=Validate() 
    s.login() 
    m=Menu 
    c=Category 
    m.order_menu() 
else:
    print("Invalid Input")
