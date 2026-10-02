# Class
class ATM:
    def __init__(self,balance,pin):
        self.balance = balance
        self.limit   = 100000          # Object Attributes
        self.pin     = pin
        self.t_history  = []


    # Deposit Method
    def deposit(self,deposit_balance):
        if deposit_balance > 0:
            if self.balance + deposit_balance > self.limit :
                print("\n<=====Account_No_Limit=====>")
            else:
                self.balance += deposit_balance
                self.t_history.append(("Deposit",deposit_balance))
                print("<===Deposit_Successful===>")
        else:
            print("<==Invalid Amount==>")



    # Withdraw Method
    def withdraw(self,withdraw_balance):
        if withdraw_balance > 0:
            if withdraw_balance > self.balance:
                print("<==Insufficient Balance==>")
            else:
                self.balance -= withdraw_balance
                self.t_history.append(("Withdraw",withdraw_balance))
                print("<==Withdraw_Successful==>")
        else:
            print("<==Invalid Amount==>")


                    
    # Check_Balance Method
    def check_balance(self):
        print("Current Amount:",self.balance)



    # Change PIN Method
    def change_pin(self):
        chance = 3
        while True:
            old_pin = int(input("\nEnter Old Pin:"))
            if old_pin == self.pin:
                new_pin = int(input("Enter New Pin:"))
                self.pin = new_pin
                print("PIN Successful Update")
                break
            else:
                chance -=1

                if chance > 0 :
                    print(f"Incorrect PIN Try Only {chance} Attempts")
                else:
                    print("\n----Sorry Change Pin After 24 Hours----")
                      # Account Locked Condition

                    answer = input("\n24 Hours Complete : Yes/No ").upper()
                    if  answer == "YES" :
                        print("\n<----Login Account---->")
                        chance = 3
                    else:
                        print("Account Still Locked")
                        break

                break


    # Transaction History Method
    def transaction_h(self):
        print("\n---Transaction History---")
        for type,money in self.t_history :
            print(type,"=",money)



    # Latest Five Transactions Method
    def mini_statement(self):
        print("\n--- Mini Statement ---")
        for type, money in self.t_history[-5:]:
            print(type, "=", money)
        print("Current Balance =", self.balance)




acc1 = ATM(10000,12345)

# Account = 1

print("\nLogin Account")

attempts = 3
while True :
    user_pin = int(input("Enter Pin :"))
    if  user_pin == acc1.pin :
        print("Login_Successful")
        while True:
            print("\n-------Select Option------")
            print("1.Deposit_Balance")
            print("2.Withdraw_Balance")
            print("3.Fast Cash")
            print("4.Change Pin")
            print("5.Transaction History")
            print("6.Balance Inquiry")
            print("7.Mini Statement")
            print("8.Exit")


            option = int(input("\n|---Enter Option---|="))

            # Deposit Balance Condition
            if option == 1:
                amount = int(input("Enter Deposit_Balance:"))
                acc1.deposit(amount)

            # Withdraw Condition
            elif option == 2:
                    amount = int(input("Enter Withdraw_Balance:"))
                    acc1.withdraw(amount)

            # Fast Cash Condition
            elif option == 3:
                while True:
                    print("\n---Fast Cash---")
                    print("1.25000")
                    print("2.50000")
                    print("3.100000")

                    choice = int(input("Select Amount:"))
                    if choice == 1:
                        acc1.withdraw(25000)
                        break

                    elif choice == 2:
                        acc1.withdraw(50000)
                        break

                    elif choice == 3 :
                        acc1.withdraw(100000)
                        break
                    else:
                        print("Invalid Option")

            # Change PIN Condition
            elif option == 4:
                acc1.change_pin()
                break

            elif option == 5:
                acc1.transaction_h()

            elif option == 6:
                acc1.check_balance()

            elif option == 7:
                acc1.mini_statement()

            elif option == 8 :
                break


            else:
                print("Invalid Option")
    else:
        attempts -=1
        if attempts > 0 :
            print(f"Incorrect PIN Try Only {attempts} Attempts")
        else:
            print("\n----Sorry Your Account Locked For 24----")

        # Account Locked Condition
            answer = input("\n24 Hours Complete : Yes/No ").upper()
            if  answer == "YES" :
                print("\n<----Login Account---->")
                attempts = 3
            else:
                print("Account Still Locked")

                break