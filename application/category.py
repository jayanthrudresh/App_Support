from products import Order
import sys 

class Category:  
    def __init__(self, name): 
        self.name=name          
    def skin_care_products(self): 
        if self.name == 'S': 
            print("""list of skin products available: 
                     1. sleeping mask 
                     2. hydrating serum 
                     3. makeup remover 
                     4. facial scrub 
                     5. organic soap 
                     6. organic shampooo""") 
            q1=int(input("select your choice")) 
            f=Order(q1) 
            #for i in range(1,7):        
            if q1==1: 
                f.sleeping_mask() 
            elif q1==2: 
                f.hydrating_serum() 
            elif q1==3: 
                f.makeup_remover() 
            elif q1==4: 
                f.facial_scrub() 
            elif q1==5: 
                f.organic_soap() 
            elif q1==6: 
                f.organic_shampoo() 
            else: 
                print("out of range")          
    def drinks(self): 
        if self.name == 'D': 
            print("""list of organic natural drinks available: 
                     1.tulsi iced tea 
                     2.healing buckwheat tea 
                     3.ginger chai recipes 
                     4.organic maple water beverage""") 
            q2=int(input("select your product:")) 
            f1=Order(q2) 
            #for i in range(1,5): 
            #if q2==i: 
            if q2==1: 
                f1.tulsi() 
            elif q2==2: 
                f1.buckwheat() 
            elif q2==3: 
                f1.ginger() 
            elif q2==4: 
                f1.maple_water() 
            else: 
                print("out of range")         
    def fertilizers(self):    
        if self.name == 'F': 
            print("""list of natural fertilizers available: 
                  1.manure 
                  2.vermicompost 
                  3.chicken litter""") 
            q3=int(input("select your choice")) 
            f2=Order(q3) 
            #for i in range(1,4): 
            #if q3==i: 
            if q3==1: 
                f2.manure() 
            elif q3==2: 
                f2.vermicompost() 
            elif q3==3: 
                f2.chickenlitter()              
            else: 
                print("out of range")  
#c=Category("S") 
class Menu: 
    def order_menu():                                                                              
        while True:                                             # While looping to keep menu alive 
            print("" * 31 + "CATEGORY" + "" * 31 + "\n"     # Mail Menu 
                    "\t(S) SKIN CARE PRODUCTS\n" 
                    "\t(D) DRINKS\n" 
                    "\t(F) FERTILIZERS \n" 
                    # "\t(M) HOME \n" 
                    "\t(E) EXIT \n" + "_" * 72) 
            input_1 = str(input("Please Select Your category: ")).upper()  
            o1=Category(input_1) 
            if len(input_1) == 1: 
                if (input_1 == 'S'):  #Easy Access Checking Logic 
                    print("\n" * 10) 
                    o1.skin_care_products()  
                    break 
                elif (input_1 == 'D'): 
                    print("\n" * 10) 
                    o1.drinks() 
                    break 
                elif (input_1 == 'F'): 
                    print("\n" * 10) 
                    o1.fertilizers()  
                    break  
                elif (input_1 == 'E'): 
                    sys.exit() 
                else:                
                    print("invalid input") 
            else: 
                print("invalid input")        
        #order_menu() 
m=Menu() 