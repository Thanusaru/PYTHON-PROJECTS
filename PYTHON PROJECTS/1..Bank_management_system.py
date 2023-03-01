""" welcome to the project of Bank Management System
    its very useful and important project to build ours knowledge too.
"""

from datetime import datetime
ct = datetime.now()

Holder_Names=[]
Acc_PIN=[]
Acc_Balance=[]
Deposit=0
Withdraw=0
Balance=0
add_n=0

while True:  
        print('-_-'*20,'\n') 
        print('*******  WELCOME TO SBI BANK  ********\n')
        print("DATE :",ct.strftime("%x"), ct.strftime("%A"),"TIME =", ct.strftime("%I"),":",ct.strftime("%M"),ct.strftime("%p"),"\n")
        print('--      CREATE A NEW ACCOUNT  ------->   1')
        print('--      WITHDRAW              ------->   2')
        print('--      DEPOSIT               ------->   3')
        print('--      BALANCE               ------->   4')
        print('--      EXIT                  ------->   5\n')
        print('-_-'*20,'\n')
        user_option=int(input('PLEASE ENTER YOUR OPTION : '))
        print()
        if user_option==1: #create new account
                print('===  NOW YOU CAN CREATE YOUR ACCOUNT  ===\n')            
                name=input('PLEASE ENTER YOUR FULL NAME : ')
                Holder_Names.append(name)
                def create_pin(acc_pin):
                        pin=str(input('CREATE YOUR 4 DIGIT PIN : '))
                        if len(pin) == 4:
                                acc_pin.append(pin)
                        else:
                                print('YOUR PIN TOO LONG OR TOO SHORT')
                                create_pin(acc_pin)
                create_pin(Acc_PIN)
                balance=eval(input('DEPOSITE YOUR AMOUNT : '))
                Acc_Balance.append(balance)
                print("\nDATE :",ct.strftime("%x"), ct.strftime("%A"),"TIME =", ct.strftime("%I"),":",ct.strftime("%M"),ct.strftime("%p"),"\n")
                print('NAME :',Holder_Names[add_n])
                print('PIN :',Acc_PIN[add_n])
                print('BALANCE :',Acc_Balance[add_n],'-/RS')
                print('\n YOUR DETAILS ARE ADDED TO OUR BANK')
                # add_n=add_n+1
                print('****  SUCCESSFULLY YOUR ACCOUNT IS CREATED ****\n')
                print('NOTE : PLEASE REMEMBER THE PASSWORD')
                print('*** THANK YOU FOR VISITING OUR SBI BANK ***')
                print('='*20)
                add_n=add_n+1
                main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :')
                #it helps to go back to hame page
        elif user_option==2: #withdra amount
                p = 0 # i took this 0 to run the while loop without terminate
                print('===  WITHDRAWAL YOUR AMMOUNT  ===')  
                while p < 1: # 0<1 condition is satisfied
                        r = -1 # hear i took r=-1 
                        name=input('ENTER YOUR NAME : ')
                        pin=input('ENTER YOUR PIN : ')
                        while r < len(Holder_Names)-1: #index value start with 0 
                                #len function gives the length of character # to get the index value #thats why i took -1
                                r=r+1 # it helps to matches the name and pin with the help of index 
                                if name == Holder_Names[r]:
                                        if pin == Acc_PIN[r]:
                                                p = p + 1 # it stops the while looping by adding + 1
                                                print('\n YOUR BALANCE : ',Acc_Balance[r],'-/RS')
                                                balance=Acc_Balance[r]
                                                def wit_draw(balance): #hear im using function to get the correct results 
                                                        withdraw=eval(input('ENTER YOUR WITHDRAWAL AMOUNT : '))
                                                        if withdraw <= balance: 
                                                                balance=balance-withdraw
                                                                Acc_Balance[r]=balance
                                                                print('\nYOUR TRANSACTION IS COMPLETED\n PLEASE COLLECT YOUR AMOUNT')
                                                                print('\nYOUR REMAINING BALANCE : ',balance,'-/RS SBI BANK')
                                                                print("DATE :",ct.strftime("%x"), ct.strftime("%A"),"TIME =", ct.strftime("%I"),":",ct.strftime("%M"),ct.strftime("%p"),"\n")
                                                                print('*** THANK YOU FOR VISITING OUR SBI BANK ***')
                                                                print('='*20)
                                                        elif withdraw > balance:
                                                                print('YOUR AMOUNT IS MORE THAN YOUR BALANCE! \n SO PLEASE SELECT APPROPRIATE AMOUNT ')
                                                                wit_draw(balance)                      
                                                wit_draw(balance)                
                        if p < 1:
                                #when above condition is not works then it will returs this statment
                                print('''YOUR NAME AND PIN DOES NOT MATCHE TO YOUR RECORDS \n SO PLEASE ENTER YOUR VALID DETAILS''')
                                break
                main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :')
                #it helps to go back to hame page
        elif user_option==3: # deposit your amount
                h = 0
                print('===  DEPOSIT YOUR AMOUNT  ===')
                while h<1:
                        r=-1
                        name=input('ENTER YOUR NAME : ')
                        pin=input('ENTER YOUR PIN : ')
                        while r < len(Holder_Names)-1: #index value start with 0 
                                #len function gives the length of charecter # to get theindex value #thats why i took -1
                                r=r+1 # it helps to matches the name and pin with the help oof index 
                                if name == Holder_Names[r]:
                                        if pin == Acc_PIN[r]:
                                                h=h+1
                                                print('YOUR BALANCE : ',Acc_Balance[r],'-/RS\n')
                                                deposit=eval(input('DEPOSIT YOUR AMOUNT : '))
                                                balance=Acc_Balance[r]
                                                balance=balance+deposit
                                                Acc_Balance[r]=balance
                                                print('**** SUCCESFULLY YOUR AMOUNT IS CREDITED **** \n')
                                                print('AVILABLE BALANCE',balance,'-/RS SBI BANK')
                                                print("DATE :",ct.strftime("%x"), ct.strftime("%A"),"TIME =", ct.strftime("%I"),":",ct.strftime("%M"),ct.strftime("%p"),"\n")
                                                print('*** THANK YOU FOR VISITING OUR SBI BANK ***')
                                                print('='*20)
                        if h<1:
                                print('YOUR NAME AND PIN DOES NOT MATCHE TO YOUR RECORDS \n SO PLEASE ENTER YOUR VALID DETAILS')
                                break                
                main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :')
                #it helps to go back to hame page                                
        elif user_option==4: # check you balance
                g=0
                print('===  CHECK YOUR BALANCE  ===')
                while g<1:
                        r=-1
                        name=input('ENTER YOUR NAME : ')
                        pin=input('ENTER YOUR PIN : ')
                        while r < len(Holder_Names)-1:
                                r=r+1
                                if name==Holder_Names[r]:
                                        if pin==Acc_PIN[r]:
                                                g=g+1
                                                balance=Acc_Balance[r]
                                                print('\nNAME : ',Holder_Names[r])
                                                print('YOUR AVILABLE BALANCE',balance,'-/RS SBI BANK\n')
                                                print("DATE & TIME :",ct)
                                                print("DATE :",ct.strftime("%x"), ct.strftime("%A"),"TIME =", ct.strftime("%I"),":",ct.strftime("%M"),ct.strftime("%p"),"\n")
                                                print('*** THANK YOU FOR VISITING OUR SBI BANK ***')
                                                print('='*40)
                        if g<1:
                                print('YOUR NAME AND PIN DOES NOT MATCHE TO YOUR RECORDS \n\n SO PLEASE ENTER YOUR VALID DETAILS')
                                break                
                main_menu=input('PRESS ANY KEY TO GO BACK TO HOME :')
                #it helps to go back to hame page                
        elif user_option==5:
                print('\n===***  EXIT  ***===\n')
                print('*** THANK YOU FOR VISITING OUR SBI BANK ***')
                print('='*40)
                break
        else:
                print('YOUR SELECTED OPTION IS WRONG \n  PLEASE ENTER THE VALID OPTION')
                print('\n')
                print('***  FROM SBI BANK  ***')
                print('='*40)
                main_menu=input('PRESS ANY KEY TO GO BACK TO MAIN MENU :')
                #it helps to go back to hame page

#########################    **Thank you**!   ###############################        