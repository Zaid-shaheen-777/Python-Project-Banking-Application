import math
print("::: \\Welcome to Online Banking Application// :::")
def signin():
        global name # username
        global pin # password
        global cb # current balance
        name = str(input(" Please Create Your User Name : "))
        pin = str(input("Please Create Your 6 six Digits Pin : "))
        if len(pin) == 6:
                pin = pin
        else:
                print(" The has to 6 digits : ")
                newpin = str(input("Please Create Your 6 six Digits Pin : "))   
                if len(newpin) != 6:
                        print("The pin has to be 6 digits ")
                        signin()  
                else:
                        pin = newpin
        print("\\:: Thanks For Creating Your Bank Account :://")      

def forgotpin():
        recoverpin = str(input("Please Create Your 6 six Digits Pin : "))
        if len(recoverpin) != 6:
                print(": The Pin has to be in 6 digits :")
                forgotpin()
        else:
                print(": The New Pin Has Been Restored, Please Log In")
                pin = recoverpin
def depositInterest(p,r,t):
        # A= Pe^(rt) Formula for calculating compound interest
        p = float(input("Enter Value of p :"))
        r = float(input("Enter Value of r :"))
        t = float(input("Enter Value of t :"))
        rt = r * t
        e = math.exp(rt)
        #Calculate
        a = p * e #Future Value Of Your Investment
        return a
def login():
        # name1 is represnting the username
        #pin1 is representing the user's pin
        name1 =str(input("Enter Your User Name : "))
        pin1 =str(input("Enter Your password : "))
        # Checking The name and pin matched or not : 
        if name1 == name and pin1 == pin:
                print(" \\ :: Welcome To Online Banking Application :: // "," ",name)
                print(":: Please Choose the Menu downhere :: ") 
                listmenu = ["1-Deposit","2-Withdraw","3-Transfer","4-Check Balance","5-Deposite Interest rate","6-Calculate Compound interest : "]
                for b in listmenu:
                        print(b)
                choose = int(input("Enter Your Number from your choices "))        
                d = 0 # represents deposit
                w = 0 # represents withdraw
                cd = 0 # represents current balance 
                if choose == 1:
                        d = int(input("Enter the Amount of Money You want to Deposit :"))
                        cd = d
                        print("Your current Balance is : ",str(cd))
                elif choose == 2:
                        w = int(input(" Enter Amount of Money you want to withdraw "))
                        if w > cd:
                                print(" Not enough Money For this Transaction : ") 
                                login()       
                        else:
                                cd = d-w
                                print(str(w)+" "+ "Has been withdrawn from your Account : And Your Current Balance is : ",str(cd))
                elif choose == 3:
                        dest = str(input("Enter The Account number of your destination in 8 digits : "))
                        if len(dest) == 8:
                                amount = int(input("Enter the amount you want to transfer : "))
                                if amount > cd:
                                        print("Not enough Money For this Transaction : ")
                                        login()
                                else:
                                        cd = d - amount
                                        print(f"The Transaction of {str(amount)} has been transfered to {str(dest)} Your current Balance is {str(cd)}")        
                        else:
                                print("Account Number is invalid the transaction is rejected : ")
                                login()
                elif choose == 4:
                        print(f"Your Currenty Balance is : {str(cd)}")   

                elif choose == 5:
                        if d > 50000:
                                rate = 3        
                        elif d > 30000:
                                rate = 2
                        else:
                                rate = 1.5
                        print(f"Your Current Deposite interest rate is {str(rate)}% : ")                        
                elif choose == 6:
                        listoption = ["1- Calculate you deposite compund based on your CB :", "2- Calculate you deposite compund based on your Deposit input :"]
                        for n in listoption:
                                print(n)
                        choice = int(input("Please Enter your Choice From the choice above : "))
                        if choice == 1:
                                timing = str(input("How many years you want to invest your money : "))
                                if d > 50000:
                                        ratex = 3/100
                                elif d > 30000:
                                        ratex = 2/100
                                else:
                                        ratex = 1.5/100  
                                print("Your current Balance in Timing , Years will be ")
                                print(depositInterest(cd,ratex,timing))   
                        elif choice == 2:
                                timing1 = str(timing("How many years you want to invest your money : "))
                                money = str(input("Enter Amount of money you would like to deposte : "))
                                money = int(money)  
                                if d > 50000:
                                        ratex = 3/100
                                elif d > 30000:
                                        ratex = 2/100
                                else:
                                        ratex = 1.5/100 
                                print("Your current Balance in Timing , Years will be ")
                                print(depositInterest(money,ratex,timing)) 
                else:
                        print(" Option is not available , Back to main menu ")
                        login()                                                
        else:
                print(": Either your user name or pin is wrong : Did you Create your Account ") 
                list1 = ["Press 1 for yes", "Press 2 for No"]
                for i in list1:
                        print(i)
                inp = int(input("Enter Your Choice Below"))
                if inp == 1:
                        list2 = [" 1--Do you want to attempt login again :"," 2- You Forget Your Pin code "]
                        for e in list2:
                                print(e)
                        theanswer = str(input("Please Enter Your Choice : ")) 
                        theanswer = int(theanswer)  
                        if theanswer == 1:
                                login()
                        elif theanswer == 2:
                                forgotpin()
                        else:
                                print(" Option not Available : ")
                                login()     
                elif inp == 2:
                        print("Please Create your Account : ")
                        signin()
        exit()                             
def mainmenu ():
        optionone=int(input("Choose 1 to sign in and choose 2 to log in : "))
        if optionone == 1:
                signin()
        elif optionone == 2:
                login()
        else:
                print("Option not available : ")
                mainmenu
        exit()        

def exit():
        answer = str(input("Do you still want to conduct Transactions : Yes Or No : "))   
        if answer == "Yes":
                login()
        elif answer == "No":
                print("Thanks for using this app :")
        else:
                print("Option not Available")
                mainmenu()

mainmenu()