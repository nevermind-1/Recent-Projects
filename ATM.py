from ATM_EX import password
import math
import random

#DATABASE SYSTEM
DSTV_plans = {"Bi-weekly":2500, "monthly": 4000, "Anually": 45000}
GOTV_plans = {"Bi-weekly":3500, "monthly": 6500, "Anually": 72000}
NEPA_plans = {"Bi-weekly":5000, "monthly": 9000, "Anually": 100000}
BANKS = ['UBA','GTC','STERING','FIRST','ZENNIT','ACCESS','OTHERS']
receipient_account_numbers = ["1501175655","2112544470","112344465","5447688890"]


print("***WELCOME TO UBA MOBILE BANKING***")
Your_account_number = input("Please Enter Your Account Number: ")

Account_number = "2112544470"
Account_balance = 50000
pin = "1234"cls
transactions = "(a)transfer \n(b)withdraw \n(c)check Balance \n(d)pay bills \n(e)Recharge"

#account number checking
if (Your_account_number != Account_number):
    print("Invalid Account Number! Try Again")
else:
    Your_pin = input("Please Enter Your Pin To Proceed: ")
    if (Your_pin != pin):
        print("Wrong...! Enter correct Pin")
    else:
        print(transactions)
        Your_transaction = input("Choose transaction: ").lower()

        #transaction checking block
        if (Your_transaction == "a"):
            banks = "(1) UBA (2) GTC (3) STERING (4) FIRST (5) ZENNIT (6) ACCESS (7) OTHERS"
            print(banks)
            receipient_bank = input("Choose the receipient Bank: ")

            if(receipient_bank == '1' or receipient_bank == '2' or receipient_bank == '3' or receipient_bank == '4' or receipient_bank == '5'):
                receipient_an = int(input("Please enter reciepient account number: "))
                for receipient_an in receipient_account_numbers:
                    if receipient_an in receipient_account_numbers:
                        transfer_amount = int(input("How much do you want to transfer: "))
                        if transfer_amount < Account_balance:
                            transfer_amount = str(transfer_amount)
                            confirmation = input("You about transfering " + transfer_amount + " to " + "anthony: Y/N to continue/cancel: ").upper()
                            if confirmation == 'Y':
                                transfer_amount = int(transfer_amount)
                                Account_balance -= transfer_amount
                                print("Your Account Balance is",Account_balance)
                                print("Transaction successful!")
                            else:
                                print("Transaction cancelled. Thanks")
                                
                        elif transfer_amount >= Account_balance:
                            print("Insuficient Balance")
                        else:
                            print("Ivalid input!")

                    elif receipient_an not in receipient_account_numbers:
                        print("Account number not in existence!")
                    else:
                        print("Invalid input!")
                    quit()
                      
            elif(receipient_bank == '6'):
                print("Other banks")
            else:
                print("Invalid input!")
                
        elif (Your_transaction == "b"):
            withdrawal_amount = "(1) 1000 \n(2)5000 \n(3) 10000 \n(4) 'input_amount' \n(5) 'other amounts'"
            print(withdrawal_amount)
            Your_withdrawal_amount = input("Choose Amount To Withdraw: ")
            if (Your_withdrawal_amount == "1"):
                Account_balance -= 1000
                #Machine dispenses cash...
                #receives alert(to be worked on too)
                print("Your account balance is ",Account_balance)
            elif(Your_withdrawal_amount == "2"):
                Account_balance -= 5000
                #Machine dispenses cash...
                print("Your account balance is ",Account_balance)
            elif(Your_withdrawal_amount == "3"):
                Account_balance -= 10000
                #Machine dispenses cash...
                print("Your account balance is ",Account_balance)
                #Here chokes! you  need to fix it later. dont forget!
            elif(Your_withdrawal_amount == "4"):
                input_amount = Number(input("Enter Amount Here: "))
                if(input_amount < Account_balance):
                    print("Insufficient Fund!")
                else:
                    Account_balance -= input_amount
                    #Machine dispenses cash...
                    print("Your account balance is ",Account_balance)

                #TO BE CONTINUED
        elif(Your_transaction == "c"):
            print("Your Account Balance is ",Account_balance)
            print("Would you love to perform any transaction?")

        elif(Your_transaction == "d"):
            bil_options = "(1)DSTVs \n(2)GOTVs \n(3)Nepa Bills \n(4)Tax \n(5)Others"
            print(bil_options)
            your_bill_option = input("What Bill do want to pay for? ")
            if(your_bill_option == "1"):
                DSTV_plansEl = "(1) Bi-weekly: 2500 \n(2) Monthly: 4000 \n(3) Anually: 45000"
                print(DSTV_plansEl)
                DSTV_input = input("choose your plan: ")
                if(DSTV_input == "1"):
                    Account_balance -= DSTV_plans["Bi-weekly"]
                    #linking with/to DSTv sever(web) and obtain the info; perform the transaction
                    print("You have successfully subscribed for a DSTV Bi-weekly plan\nYou now have access to our 200+ programs")
                    print("Here is your DSTV Encrypted login password:")
                    password()
                    print("Please Do not disclose to a third party for it's not adviceable")
                    print("***ENJOY!***")
                elif(DSTV_input == "2"):
                    Account_balance -= DSTV_plans["monthly"]
                    #linking with/to DSTv sever(web) and obtain the info; perform the transaction
                    print("You have successfully subscribed for a DSTV monthly plan\nYou now have access to our 200+ programs")
                    print("Here is your DSTV Encrypted login password:")
                    password()
                    print("Please Do not disclose to a third party for it's not adviceable")
                    print("***ENJOY!***")
                elif(DSTV_input == "3"):
                    Account_balance -= DSTV_plans["Anually"]
                    #linking with/to DSTv sever(web) and obtain the info; perform the transaction
                    print("You have successfully subscribed for a DSTV anual plan\n You now have access to our 200+ programs")
                    print("Here is your DSTV Encrypted login password:")
                    password()
                    print("Please Do not disclose to a third party for it's not adviceable")
                    print("***ENJOY!***")
                else:
                    print("Invalid Plan! Please Choose from the above Options")

            elif(your_bill_option =="2"):
                GOTV_plansEl = "(1) Bi-weekly: 3500 \n(2) Monthly: 6500 \n(3) Anually: 72000"
                print(GOTV_plansEl)
                GOTV_input = input("choose your plan: ")
                if(GOTV_input == "1"):
                    Account_balance -= GOTV_plans["Bi-weekly"]
                    #linking with/to DSTv sever(web) and obtain the info; perform the transaction
                    print("You have successfully subscribed for a GOTV Bi-weekly plan\nYou now have access to our 400+ programs")
                    print("Here is your GOTV Encrypted login password:")
                    password()
                    print("Please Do not disclose to a third party for it's not adviceable")
                    print("***ENJOY!***")
                elif(GOTV_input == "2"):
                    Account_balance -= GOTV_plans["monthly"]
                    #linking with/to DSTv sever(web) and obtain the info; perform the transaction
                    print("You have successfully subscribed for a GOTV monthly plan \n You now have access to our 400+ programs")
                    print("Here is your GOTV Encrypted login password:")
                    password()
                    print("Please Do not disclose to a third party for it's not adviceable!")
                    print("***ENJOY!***")
                elif(GOTV_input == "3"):
                    Account_balance -= GOTV_plans["Anually"]
                    #linking with/to DSTv sever(web) and obtain the info; perform the transaction
                    print("You have successfully subscribed for a GOTV anual plan \n You now have access to our 400+ programs")
                    print("Here is your GOTV Encrypted login password:")
                    password()
                    print("Please Do not disclose to a third party for it's not adviceable")
                    print("***ENJOY!***")
                else:
                    print("Invalid Plan! Please Choose from the above Options")
                
            elif(your_bill_option =="3"):
                Nepa_pay_options = "(1)Desired Amount \n (2)Nepa_pay_default"
                print(Nepa_pay_options)
                Nepa_pay_optionsEl = input("How do you want to Pay? ")
                if(Nepa_pay_optionsEl == "1"):
                    Nepa_subscription = input("Enter amount to subscribe: ")
                    if(Nepa_subscription < Account_balance):
                        print("Insufficient Balance!")
                    else:
                        daily_sub = 500
                        number_of_days = 0
                        subscription_days = math.ceil(Nepa_subscription / daily_sub)
                        print("Thanks for subscribing for " + subscription_days + "days of Nepa usage")
                        print("Here is your Meter passward:")
                        password()
                        print("Warning-Disclose not to the third party!")
                elif(Nepa_pay_optionsEl == "2"):
                    NEPA_plansEl = "(1) Bi-weekly: 3500 \n(2) Monthly: 6500 \n(3) Anually: 72000"
                    print(NEPA_plansEl)
                    NEPA_input = input("choose your plan: ")
                    if(NEPA_input == "1"):
                        Account_balance -= NEPA_plans["Bi-weekly"]
                        #linking with/to NEPA sever(web) and obtain the info; perform the transaction
                        print("You have successfully subscribed for a NEPA Bi-weekly plan")
                        print("Here is your meter password:")
                        password()
                        print("Please Do not disclose to a third party for it's not adviceable")
                        print("***ENJOY!***")
                    elif(NEPA_input == "2"):
                        Account_balance -= NEPA_plans["monthly"]
                        #linking with/to NEPA sever(web) and obtain the info; perform the transaction
                        print("You have successfully subscribed for a NEPA monthly plan")
                        print("Here is your meter password:")
                        password()
                        print("Please Do not disclose to a third party for it's not adviceable!")
                        print("***ENJOY!***")
                    elif(NEPA_input == "3"):
                        Account_balance -= GOTV_plans["Anually"]
                        #linking with/to DSTv sever(web) and obtain the info; perform the transaction
                        print("You have successfully subscribed for a GOTV anual plan")
                        print("Here is your meter password:")
                        password()
                        print("Please Do not disclose to a third party for it's not adviceable")
                        print("***ENJOY!***")
                else:
                    print("...coming")
            elif(your_bill_option =="4"):
                print("...coming")
            elif(your_bill_option =="5"):
                print("Sorry! \n No further options for Now \nYour may like to perform other available transactions")
            
        elif(Your_transaction == "e"):
            print("I think you should be the first to work on. we are coming!")
        else:
            print("Thanks for banking with UBA")#For now...will be updated later.


#creation of password generator
#wow! Just done with the creation of the password. That's great.
#still have to add a while loop  in the card pin confirmation code block fron =>line 27
#Work on your Database.