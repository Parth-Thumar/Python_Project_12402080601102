# ---Importing usefull libraries---
import mysql.connector
from datetime import datetime, timedelta
import smtplib
import random
import time

# ---Connecting to database---
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mann_db"
)

# ---Making object of a cursor--- 
mycursor = mydb.cursor()

# ---Class Auction---
class MainPrediction:
    month = 0
    quarter = 0
    year = 0
    
    # ---Method Universal---
    def Universal_Signup(self):
        name = input("\nEnter your name: ")
        gender = input("Enter your gender: ")
        mobile = input("Enter your mobile number: ")
        
        while True:
            email = input("Enter your email: ")
            
            if "@gmail.com" in email or "@hotmail.com" in email or "@yahoo.com" in email:
                qry = ("INSERT INTO universal (name, gender, email, mobile, otp) VALUES (%s, %s, %s, %s, %s)")
                send = random.randint(1000, 9999)
                data = (name, gender, email, mobile, send)
                mycursor.execute(qry, data)
                mydb.commit()
                
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("vasukheni51@gmail.com", "sqlv jvrw rchj siot")
                
                message = f"Thank you for purchasing 'Universal pass' in 'Satta Khelo'!\n Here is your OTP: {send}\n Have a good day:)"
                s.sendmail("vasukheni51@gmail.com", email, message)
                s.quit()
                print("\nOTP has been sent to your E-mail!")    
                break
            else:
                print("\nEnter a valid E-mail!\n")
        
        while True:
            otp = int(input("\nEnter OTP: "))
            if otp == send:
                print("\nSelect time period(per month pirce: 100$)")
                print("1 = monthly(10% discount)!")
                print("2 = Quarterly(4 months: 15% discount)!")
                print("3 = Yearly(20% discount)!")
                ch = int(input("\nEnter your choice: "))
                match ch:
                    case 1:
                        self.month = int(input("\nFor how many months? "))
                        base = 100 * self.month
                        discount = base * 0.10
                        total = base - discount
                        print(f"you have selected universal pass for {self.month} moths!")
                        print("==============================")
                        print("Your total charge is:",total)
                        print("==============================")
                        
                        print("\nDo you want to proceed? ")
                        print("1 = Yes!")
                        print("2 = No!")
                        ch = int(input("\nEnter your choice: "))
                        if ch == 1:
                            qry = "UPDATE universal SET start = %s, expire = %s, validity = %s WHERE mobile = %s;"
                            current = datetime.now().date()
                            expire = current + timedelta(days = self.month * 30)
                            data = (current, expire, 'Monthly', mobile)
                            mycursor.execute(qry, data)
                            mydb.commit()
                            
                            print(f"Your pass will be expired on {expire}!")
                            print("\nUniversal pass has been purchased successfully!")
                            break
                        
                        elif ch == 2:
                            print("\nThank you for visit:)")
                            break
                        
                        else:
                            print("\nEnter valid choice!")
                            
                    case 2:
                        self.quarter = int(input("\nFor how many quarters? "))
                        base = 100 * self.quarter
                        discount = base * 0.15
                        total = base - discount
                        print(f"you have selected universal pass for {self.quarter} quarters!")
                        print("==============================")
                        print("Your total charge is:",total)
                        print("==============================")
                        
                        print("\nDo you want to proceed? ")
                        print("1 = Yes!")
                        print("2 = No!")
                        ch = int(input("\nEnter your choice: "))
                        if ch == 1:
                            qry = "UPDATE universal SET start = %s, expire = %s, validity = %s WHERE mobile = %s;"
                            current = datetime.now().date()
                            expire = current + timedelta(days = self.quarter * 120)
                            data = (current, expire, 'Quarterly', mobile)
                            mycursor.execute(qry, data)
                            mydb.commit()
                            
                            print(f"Your pass will be expired on {expire}!")
                            print("\nUniversal pass has been purchased successfully!")
                            break
                            
                        elif ch == 2:
                            print("\nThank you for visit!")
                            break
                            
                        else:
                            print("\nEnter valid choice!")
                    
                    case 3:
                        self.year = int(input("\nFor how many years? "))
                        base = 100 * self.year
                        discount = base * 0.20
                        total = base - discount
                        print(f"you have selected universal pass for {self.year} years!")
                        print("==============================")
                        print("Your total charge is:",total)
                        print("==============================")
                        
                        print("\nDo you want to proceed? ")
                        print("1 = Yes!")
                        print("2 = No!")
                        ch = int(input("\nEnter your choice: "))
                        if ch == 1:
                            qry = "UPDATE universal SET start = %s, expire = %s, validity = %s WHERE mobile = %s;"
                            current = datetime.now().date()
                            expire = current + timedelta(days = self.year * 365)
                            data = (current, expire, 'Yearly', mobile)
                            mycursor.execute(qry, data)
                            mydb.commit()
                            
                            print(f"Your pass will be expired on {expire}!")
                            print("\nUniversal pass has been purchased successfully!")
                            break
                            
                        elif ch == 2:
                            print("\nThank you for visit!")
                            break
                            
                        else:
                            print("\nEnter valid choice!")
                    
                    case __:
                        print("\nEnter valid choice!")
            
            else:
                print("\nOTP is incorrect!")
            
                print("\n1 = Try again!")
                print("2 = Exit!")
                op = int(input("\nEnter your choice: "))
                match op:
                    case 1:
                        continue
                    case 2:
                        print("\nThank you for visit!:)")
                        break
                    case __:
                        print("\nEnter valid choice!")

    # ---Method Universel---
    def Universal(self):
        print("\n================================================================")
        print("Welcome sir!")
        print("We have a an offer today!")
        print("If you bet your money and win then your amonut will be double!")
        print("================================================================")
        
        print("\nSo are you interested to play satta? ")
        print("1 = Yes!")
        print("2 = No!")
        ready = int(input("\nEnter your choice: "))
        match ready:
            case 1:
                nickname = input("\nEnter your nickname: ")
                mycursor.execute(f"SELECT * FROM min WHERE name = ('{nickname}')")
                result = mycursor.fetchall()
                if result:
                    print("\nThis name is already in use please enter different name!")
                else:
                    print("\n==========================================================================")
                    print("The rules are simple: ")
                    print("1 = If you win the bet then you will get 2x of your amount!")
                    print("2 = If you lose the bet then your amount will be 0!")
                    print("3 = You will get 25,000 coins initially!")
                    print("4 = When you want to leave than you can collect your money from counter!")
                    print("==========================================================================")
                    initial = 25000
                    bet = 0
                    op = 0
                    while op != 4:
                        print("\nWhich bet do you want to play?")
                        print("1 = Bet of 25,000 coins!")
                        print("2 = Bet of 50,000 coins!")
                        print("3 = Bet of 100,000 coins!")
                        print("4 = Take balance from counter!")
                        bet_op = int(input("\nEnter your choice: "))
                        match bet_op:
                            case 1:
                                bet += 1
                                if initial >= 25000:
                                    mycursor.execute(f"INSERT INTO min (name, initial, bet) VALUES ('{nickname}', '{initial}', '{bet}')")
                                    mydb.commit()
                                    mycursor.execute(f"SELECT * FROM min WHERE name = ('{nickname}')")
                                    check = mycursor.fetchall()
                                    if check:
                                        actual = random.randint(1, 30)
                                        guessed = 0
                                        while True:
                                            guessed = int(input("\nChoose a number between 1 to 30: "))
                                            if guessed > 0 and  guessed <= 30:
                                                print("Please wait board is spinning...")
                                                time.sleep(5)
                                                if guessed == actual:
                                                    final = initial * 2
                                                    initial = final
                                                    qry = "UPDATE min SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, True, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Congratulations:) Your ammount is 2x!")
                                                    break
                                                else:
                                                    final = initial - 25000
                                                    initial = final
                                                    qry = "UPDATE min SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, False, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Better luck, next time!")   
                                                    break
                                            else:
                                                print("\nEnter your guessed number between 1 to 30!")
                                else:
                                    print("\ninsufficient balance for this bet!")
                                    break
                                    
                            case 2:
                                bet += 1
                                if initial >= 50000:
                                    mycursor.execute(f"INSERT INTO min (name, initial, bet) VALUES ('{nickname}', '{initial}', '{bet}')")
                                    mydb.commit()
                                    mycursor.execute(f"SELECT * FROM min WHERE name = ('{nickname}')")
                                    check = mycursor.fetchall()
                                    if check:
                                        actual = random.randint(1, 20)
                                        guessed = 0
                                        while True:
                                            guessed = int(input("\nChoose a number between 1 to 20: "))
                                            if guessed > 0 and  guessed <= 20:
                                                print("Please wait board is spinning...")
                                                time.sleep(5)
                                                if guessed == actual:
                                                    final = initial * 2
                                                    initial = final
                                                    qry = "UPDATE min SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, True, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Congratulations:) Your ammount is 2x!")
                                                    break
                                                else:
                                                    final = initial - 50000
                                                    initial = final
                                                    qry = "UPDATE min SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, False, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Better luck, next time!")   
                                                    break
                                            else:
                                                print("\nEnter your guessed number between 1 to 20!")
                                else:
                                    print("\ninsufficient balance for this bet!")
                                    break
                                    
                            case 3:
                                bet += 1
                                if initial >= 100000:
                                    mycursor.execute(f"INSERT INTO min (name, initial, bet) VALUES ('{nickname}', '{initial}', '{bet}')")
                                    mydb.commit()
                                    mycursor.execute(f"SELECT * FROM min WHERE name = ('{nickname}')")
                                    check = mycursor.fetchall()
                                    if check:
                                        actual = random.randint(1, 10)
                                        guessed = 0
                                        while True:
                                            guessed = int(input("\nChoose a number between 1 to 10: "))
                                            if guessed > 0 and  guessed <= 10:
                                                print("Please wait board is spinning...")
                                                time.sleep(5)
                                                if guessed == actual:
                                                    final = initial * 2
                                                    initial = final
                                                    qry = "UPDATE min SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, True, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Congratulations:) Your ammount is 2x!")
                                                    break
                                                else:
                                                    final = initial - 100000
                                                    initial = final
                                                    qry = "UPDATE min SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, False, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Better luck, next time!")   
                                                    break
                                            else:
                                                print("\nEnter your guessed number between 1 to 10!")
                                else:
                                    print("\ninsufficient balance for this bet!")
                                    break
                                
                            case 4:
                                li = []
                                mycursor.execute(f"SELECT final FROM min WHERE name = ('{nickname}')")
                                for i in mycursor.fetchall():
                                    win = int(i[0])
                                    li.append(win)
                                print(f"\nYour total winning money is: {li[-1]}$!")
                                break
                            
                            case __:
                                print("\nEnter valid choice!")
            
            case 2:
                print("\nThanks for visit:)")
                
            case __:
                print("\nEnter valid choice!")
                        
    # ---Method Marvel_Signup---
    def Marvel_Signup(self):
        name = input("\nEnter your name: ")
        gender = input("Enter your gender: ")
        mobile = input("Enter your mobile number: ")
        
        while True:
            email = input("Enter your email: ")
            
            if "@gmail.com" in email or "@hotmail.com" in email or "@yahoo.com" in email:
                qry = ("INSERT INTO marvel (name, gender, email, mobile, otp) VALUES (%s, %s, %s, %s, %s)")
                send = random.randint(1000, 9999)
                data = (name, gender, email, mobile, send)
                mycursor.execute(qry, data)
                mydb.commit()
                
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("vasukheni51@gmail.com", "sqlv jvrw rchj siot")
                
                message = f"Thank you for purchasing 'Universal pass' in 'Satta Khelo'!\n Here is your OTP: {send}\n Have a good day:)"
                s.sendmail("vasukheni51@gmail.com", email, message)
                s.quit()
                print("\nOTP has been sent to your E-mail!")    
                break
            else:
                print("\nEnter a valid E-mail!\n")
        
        while True:
            otp = int(input("\nEnter OTP: "))
            if otp == send:
                print("\nSelect time period(per month pirce: 100$)")
                print("1 = monthly(10% discount)!")
                print("2 = Quarterly(4 months: 15% discount)!")
                print("3 = Yearly(20% discount)!")
                ch = int(input("\nEnter your choice: "))
                match ch:
                    case 1:
                        self.month = int(input("\nFor how many months? "))
                        base = 50 * self.month
                        discount = base * 0.10
                        total = base - discount
                        print(f"you have selected marvel pass for {self.month} moths!")
                        print("==============================")
                        print("Your total charge is:",total)
                        print("==============================")
                        
                        print("\nDo you want to proceed? ")
                        print("1 = Yes!")
                        print("2 = No!")
                        ch = int(input("\nEnter your choice: "))
                        if ch == 1:
                            qry = "UPDATE marvel SET start = %s, expire = %s, validity = %s WHERE mobile = %s;"
                            current = datetime.now().date()
                            expire = current + timedelta(days = self.month * 30)
                            data = (current, expire, 'Monthly', mobile)
                            mycursor.execute(qry, data)
                            mydb.commit()
                            print(f"Your pass will be expired on {expire}!")
                            print("\nMarvel pass has been purchased successfully!")
                            break
                        
                        elif ch == 2:
                            print("\nThank you for visit!")
                            break
                        else:
                            print("\nEnter valid choice!") 
                            
                    case 2:
                        self.quarter = int(input("\nFor how many quarters? "))
                        base = 50 * self.quarter
                        discount = base * 0.15
                        total = base - discount
                        print(f"you have selected marvel pass for {self.quarter} quarters!")
                        print("==============================")
                        print("Your total charge is:",total)
                        print("==============================")
                        
                        print("\nDo you want to proceed? ")
                        print("1 = Yes!")
                        print("2 = No!")
                        ch = int(input("\nEnter your choice: "))
                        if ch == 1:
                            qry = "UPDATE marvel SET start = %s, expire = %s, validity = %s WHERE mobile = %s;"
                            current = datetime.now().date()
                            expire = current + timedelta(days = self.quarter * 120)
                            data = (current, expire, 'Quarterly', mobile)
                            mycursor.execute(qry, data)
                            mydb.commit()
                            print(f"Your pass will be expired on {expire}!")
                            print("\nMarvel pass has been purchased successfully!")
                            break
                            
                        elif ch == 2:
                            print("\nThank you for visit!")
                            break
                            
                        else:
                            print("\nEnter valid choice!")
                    
                    case 3:
                        self.year = int(input("\nFor how many years? "))
                        base = 50 * self.year
                        discount = base * 0.20
                        total = base - discount
                        print(f"you have selected marvel pass for {self.year} years!")
                        print("==============================")
                        print("Your total charge is:",total)
                        print("==============================")
                        
                        print("\nDo you want to proceed? ")
                        print("1 = Yes!")
                        print("2 = No!")
                        ch = int(input("\nEnter your choice: "))
                        if ch == 1:
                            qry = "UPDATE marvel SET start = %s, expire = %s, validity = %s WHERE mobile = %s;"
                            current = datetime.now().date()
                            expire = current + timedelta(days = self.year * 365)
                            data = (current, expire, 'Yearly', mobile)
                            mycursor.execute(qry, data)
                            mydb.commit()
                            print(f"Your pass will be expired on {expire}!")
                            print("\nMarvel pass has been purchased successfully!")
                            break
                            
                        elif ch == 2:
                            print("\nThank you for visit!")
                            break
                            
                        else:
                            print("\nEnter valid choice!")
                    
                    case __:
                        print("\nEnter valid choice!")
            
            else:
                print("\nOTP is incorrect!")
            
                print("\n1 = Try again!")
                print("2 = Exit!")
                op = int(input("\nEnter your choice: "))
                match op:
                    case 1:
                        continue
                    case 2:
                        print("\nThank you for visit!:)")
                        break
                    case __:
                        print("\nEnter valid choice!")
      
    # ---Method Marvel---                  
    def Marvel(self):
        print("\nSo are you interested to play satta? ")
        print("1 = Yes!")
        print("2 = No!")
        ready = int(input("\nEnter your choice: "))
        match ready:
            case 1:
                nickname = input("\nEnter your nickname: ")
                mycursor.execute(f"SELECT * FROM min WHERE name = ('{nickname}')")
                result = mycursor.fetchall()
                if result:
                    print("\nThis name is already in use please enter different name!")
                else:
                    print("\n==========================================================================")
                    print("The rules are simple: ")
                    print("1 = If you win the bet then you will get 2x of your amount!")
                    print("2 = If you lose the bet then your amount will be 0!")
                    print("3 = You will get 25,000 coins initially!")
                    print("4 = When you want to leave than you can collect your money from counter!")
                    print("==========================================================================")
                    initial = 25000
                    bet = 0
                    op = 0
                    while op != 4:
                        print("\nWhich bet do you want to play?")
                        print("1 = Bet of 25,000 coins!")
                        print("2 = Bet of 50,000 coins!")
                        print("3 = Bet of 100,000 coins!")
                        print("4 = Take balance from counter!")
                        bet_op = int(input("\nEnter your choice: "))
                        match bet_op:
                            case 1:
                                bet += 1
                                if initial >= 25000:
                                    mycursor.execute(f"INSERT INTO max (name, initial, bet) VALUES ('{nickname}', '{initial}', '{bet}')")
                                    mydb.commit()
                                    mycursor.execute(f"SELECT * FROM max WHERE name = ('{nickname}')")
                                    check = mycursor.fetchall()
                                    if check:
                                        actual = random.randint(1, 30)
                                        guessed = 0
                                        while True:
                                            guessed = int(input("\nChoose a number between 1 to 30: "))
                                            if guessed > 0 and  guessed <= 30:
                                                print("Please wait board is spinning...")
                                                time.sleep(5)
                                                if guessed == actual:
                                                    final = initial * 2
                                                    initial = final
                                                    qry = "UPDATE max SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, True, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Congratulations:) Your ammount is 2x!")
                                                    break
                                                else:
                                                    final = initial - 25000
                                                    initial = final
                                                    qry = "UPDATE max SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, False, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Better luck, next time!")   
                                                    break
                                            else:
                                                print("\nEnter your guessed number between 1 to 30!")
                                else:
                                    print("\ninsufficient balance for this bet!")
                                    break
                                    
                            case 2:
                                bet += 1
                                if initial >= 50000:
                                    mycursor.execute(f"INSERT INTO max (name, initial, bet) VALUES ('{nickname}', '{initial}', '{bet}')")
                                    mydb.commit()
                                    mycursor.execute(f"SELECT * FROM max WHERE name = ('{nickname}')")
                                    check = mycursor.fetchall()
                                    if check:
                                        actual = random.randint(1, 20)
                                        guessed = 0
                                        while True:
                                            guessed = int(input("\nChoose a number between 1 to 20: "))
                                            if guessed > 0 and  guessed <= 20:
                                                print("Please wait board is spinning...")
                                                time.sleep(5)
                                                if guessed == actual:
                                                    final = initial * 2
                                                    initial = final
                                                    qry = "UPDATE max SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, True, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Congratulations:) Your ammount is 2x!")
                                                    break
                                                else:
                                                    final = initial - 50000
                                                    initial = final
                                                    qry = "UPDATE max SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, False, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Better luck, next time!")   
                                                    break
                                            else:
                                                print("\nEnter your guessed number between 1 to 20!")
                                else:
                                    print("\ninsufficient balance for this bet!")
                                    break
                                    
                            case 3:
                                bet += 1
                                if initial >= 100000:
                                    mycursor.execute(f"INSERT INTO max (name, initial, bet) VALUES ('{nickname}', '{initial}', '{bet}')")
                                    mydb.commit()
                                    mycursor.execute(f"SELECT * FROM max WHERE name = ('{nickname}')")
                                    check = mycursor.fetchall()
                                    if check:
                                        actual = random.randint(1, 10)
                                        guessed = 0
                                        while True:
                                            guessed = int(input("\nChoose a number between 1 to 10: "))
                                            if guessed > 0 and  guessed <= 10:
                                                print("Please wait board is spinning...")
                                                time.sleep(5)
                                                if guessed == actual:
                                                    final = initial * 2
                                                    initial = final
                                                    qry = "UPDATE max SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, True, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Congratulations:) Your ammount is 2x!")
                                                    break
                                                else:
                                                    final = initial - 100000
                                                    initial = final
                                                    qry = "UPDATE max SET guessed = %s, actual = %s,  result = %s, final = %s WHERE name = %s AND bet = %s"
                                                    data = (guessed, actual, False, final, nickname, bet)
                                                    mycursor.execute(qry, data)
                                                    mydb.commit()
                                                    print("Better luck, next time!")
                                                    break
                                            else:
                                                print("\nEnter your guessed number between 1 to 10!")
                                else:
                                    print("\ninsufficient balance for this bet!")
                                    break
                                
                            case 4:
                                li = []
                                mycursor.execute(f"SELECT final FROM min WHERE name = ('{nickname}')")
                                for i in mycursor.fetchall():
                                    win = int(i[0])
                                    li.append(win)
                                print(f"\nYour total winning money is: {li[-1]}$!")
                                break
                            
                            case __:
                                print("\nEnter valid choice!")
            
            case 2:
                print("\nThanks for visit:)")
                
            case __:
                print("\nEnter valid choice!")
       
    # ---Method ValidityCheck---                 
    def ValidityCheck(self):
        op = 0
        while op != 3:
            print("\nWhich pass do you have? ")
            print("1 = Universal pass!")
            print("2 = Marvel pass!")
            print("3 = Exit!")
            op = int(input("\nEnter your choice: "))
            match op:
                case 1:
                    name = input("\nEnter your name: ")
                    mobile = input("Enter mobile number: ")
                    qry = "SELECT * FROM universal WHERE name = %s AND mobile = %s"
                    data = (name, mobile)
                    mycursor.execute(qry, data)
                    res = mycursor.fetchall()
                    if res:
                        qry = "SELECT expire FROM universal WHERE name = %s AND mobile = %s"
                        data = (name, mobile)
                        mycursor.execute(qry, data)
                        expire_tuple = mycursor.fetchone()
                        expire = str(expire_tuple[0])
                        print(f"Your subscription expiry date is: {expire}")
                        
                        current = datetime.now().date()
                        expire_datetime = datetime.strptime(expire, "%Y-%m-%d").date()
                        validity = (expire_datetime - current).days
                        print("==========================")
                        print(f"{validity} days left to expire!")
                        print("==========================")
                        break
                    
                    else:
                        print("\nNo records Found!")
                        
                case 2:
                    name = input("\nEnter your name: ")
                    mobile = input("Enter mobile number: ")
                    qry = "SELECT * FROM marvel WHERE name = %s AND mobile = %s"
                    data = (name, mobile)
                    mycursor.execute(qry, data)
                    res = mycursor.fetchall()
                    if res:
                        qry = "SELECT expire FROM marvel WHERE name = %s AND mobile = %s"
                        data = (name, mobile)
                        mycursor.execute(qry, data)
                        expire_tuple = mycursor.fetchone()
                        expire = str(expire_tuple[0])
                        print(f"Your subscription expiry date is: {expire}")
                        
                        current = datetime.now().date()
                        expire_datetime = datetime.strptime(expire, "%Y-%m-%d").date()
                        validity = (expire_datetime - current).days
                        print("===================================")
                        print(f"{validity} days left to expire!")
                        print("===================================")
                        break
                    
                    else:
                        print("\nNo records Found!")
                        
                case 3:
                    print("\nThank you for visit:)")
                    break
                    
                case __:
                    print("\nEnter valid choice!")
# ---Main---
obj = MainPrediction()

current = datetime.now().time()
morning = datetime.strptime("06:00:00", "%H:%M:%S").time()
afternoon = datetime.strptime("12:00:00", "%H:%M:%S").time()
evening = datetime.strptime("18:00:00", "%H:%M:%S").time()

if morning <= current < afternoon:
    print("\n========================================")
    print("Good morning, Welcome to Satta Khelo:)")
    print("========================================")
elif afternoon <= current < evening:
    print("\n==========================================")
    print("Good afternoon, Welcome to Satta Khelo:)")
    print("==========================================")
else:
    print("\n========================================")
    print("Good evening, Welcome to Satta Khelo:)")
    print("========================================")
   
op = 0 
while op != 4:
    print("\nLogin or Sign-up?")
    print("1 = Login!")
    print("2 = Sign-up!")
    print("3 = Check validity of pass!")
    print("4 = Exit!")
    op = int(input("\nEnter your choice: "))
    match op:
        case 1:
            print("\nWhich pass do you have?")
            print("1 = Universal pass!")
            print("2 = Marvel pass!")
            print("3 = Exit!")
            identify = int(input("\nEnter your choice: "))
            match identify:
                case 1:
                    name = input("\nEnter your name: ")
                    mobile = input("Enter your mobile number: ")
                    qry = "SELECT * FROM universal WHERE name = %s and mobile = %s"
                    data = (name, mobile)
                    mycursor.execute(qry, data)
                    result = mycursor.fetchone()
                    mydb.commit()
                    if result:
                        obj.Universal()
                    else:
                        print("\nNo records found!, Please Sign-Up first!")
                        
                case 2:
                    name = input("\nEnter your name: ")
                    mobile = input("Enter your mobile number: ")
                    qry = "SELECT * FROM marvel WHERE name = %s and mobile = %s"
                    data = (name, mobile)
                    mycursor.execute(qry, data)
                    result = mycursor.fetchone()
                    mydb.commit()
                    if result:
                        obj.Marvel()
                    else:
                        print("\nNo records found!, Please Sign-Up first!")
                        
                case 3:
                    print("\nEnter valid choice!")
               
        case 2: 
            ch = 0
            while ch != 3:
                print("\nWhich pass do you want?")
                print("1 = Universal pass(Only 100$ Including: Food & Drinks)!")
                print("2 = Marvel pass(Only 50$ Including: Drinks)!")
                print("3 = Exit!")
                ch = eval(input("\nEnter your choice: "))
                match ch:
                    case 1:
                        obj.Universal_Signup()
                        obj.Universal()
                        break
                    case 2:
                        obj.Marvel_Signup()
                        obj.Marvel()
                        break
                    case 3:
                        print("\nThank you for visit!")
                        break
                    case __:
                        print("\nEnter valid choice!")
         
        case 3:
            obj.ValidityCheck() 
                   
        case 4:
            print("\nThank you for visit:)")
            break
            
        case __:
            print("\nEnter valid choice!")