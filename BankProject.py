class BankAccount:
    def __init__(self, account_no, name, balance, roi):
        self._account_no = account_no
        self._account_name = name
        self._balance = balance
        self._roi = roi

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Rs. {amount} is deposited. New Balance: Rs.{self._balance}")
            update_file(Account_dict)
        else:
            print("Invalid Amount...")

    def withdrawal(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Rs. {amount} is withdrawn. New Balance: Rs.{self._balance}")
            update_file(Account_dict)
        else:
            print("Insufficient Balance or Invalid Amount...")

    def check_balance(self):
        print(f"Current Balance: Rs. {self._balance}")

    def account_details(self):
        print(f"\n------------Account Details-----------")
        print(f"Account Number: {self._account_no}")
        print(f"Account Holder: {self._account_name}")
        print(f"Balance: {self._balance}")
        print(f"Interest Rate: {self._roi * 100}%")



class SavingAccount(BankAccount):
    def __init__(self, account_no, name, balance=0, roi=0.03):
        super().__init__(account_no, name, balance, roi)


class CurrentAccount(BankAccount):
    def __init__(self, account_no, name, balance=0, roi=0.05):
        super().__init__(account_no, name, balance, roi)



# ---------- File Handling ----------
def load_data():
    try:
        with open("bank_data.txt", "r") as file:
            lines = file.readlines()

        i = 0
        while i < len(lines):
            if lines[i].startswith("Account No"):
                acct_no = lines[i].split(":")[1].strip()
                acct_name = lines[i+1].split(":")[1].strip()
                balance = int(lines[i+2].split(":")[1].strip())
                acct_type = lines[i+3].split(":")[1].strip()
                roi = float(lines[i+4].split(":")[1].strip().replace("%","")) / 100

                if acct_type == "Saving":
                    Account_dict[acct_no] = SavingAccount(acct_no, acct_name, balance, roi)
                else:
                    Account_dict[acct_no] = CurrentAccount(acct_no, acct_name, balance, roi)

                i += 6  # skip to next account
            else:
                i += 1

    except FileNotFoundError:
        open("bank_data.txt", "w")



def update_file(account_dict):
    with open("bank_data.txt", "w") as file:
        file.write("\n-----------------------------------------------------")
        file.write("\n                 ACCOUNT INFORMATION                  ")
        file.write("\n-----------------------------------------------------\n\n")
        for acct in account_dict.values():
            acct_type = "Saving" if isinstance(acct, SavingAccount) else "Current"
           
            file.write(f"Account No     : {acct._account_no}\n")
            file.write(f"Account Name   : {acct._account_name}\n")
            file.write(f"Balance        : {acct._balance}\n")
            file.write(f"Type           : {acct_type}\n")
            file.write(f"ROI            : {int(acct._roi * 100)}%\n")
            file.write("-----------------------------------------------------\n\n")


# ---------- Main Program ----------
if __name__ == "__main__":
    Account_dict = {}
    load_data()

    print("\n")
    print("==============================================================")
    print("                  WELCOME TO BANK APPLICATION                ")
    print("==============================================================")
    print("\n")

    ans = 'yes'
    while ans.lower() == 'yes':

        print("--------------------------------------------------")
        print("  1. Create Saving Account")
        print("  2. Create Current Account")
        print("  3. Deposit Amount")
        print("  4. Withdraw Amount")
        print("  5. Check Balance")
        print("  6. Show Account Details")
        print("  7. Exit")
        print("--------------------------------------------------")

        choice = int(input("\n Enter Your Choice: "))
        print("\n")

        if choice == 1:
            print("------ CREATE SAVING ACCOUNT ------")
            acct_no = input("Enter Saving Account Number: ")
            acct_name = input("Enter Account Holder Name: ")

            if acct_no in Account_dict:
                print("\nSaving Account already exists!")
            else:
                print("\nSaving Account Created Successfully!")
                balance = int(input("Enter Balance: "))
                Account_dict[acct_no] = SavingAccount(acct_no, acct_name, balance, 0.03)

                print("\n------------- ACCOUNT INFO -------------")
                print(f" Account No     : {acct_no}")
                print(f" Holder Name    : {acct_name}")
                print(f" Balance        : Rs. {balance}")
                print(f" Interest Rate  : 3%")
                print("---------------------------------------\n")

                update_file(Account_dict)

        elif choice == 2:
            print("------ CREATE CURRENT ACCOUNT ------")
            acct_no = input("Enter Current Account Number: ")
            acct_name = input("Enter Account Holder Name: ")

            if acct_no in Account_dict:
                print("\nCurrent Account already exists!")
            else:
                print("\nCurrent Account Created Successfully!")
                balance = int(input("Enter Balance: "))
                Account_dict[acct_no] = CurrentAccount(acct_no, acct_name, balance)

                print("\n------------- ACCOUNT INFO -------------")
                print(f" Account No     : {acct_no}")
                print(f" Holder Name    : {acct_name}")
                print(f" Balance        : Rs. {balance}")
                print(f" Interest Rate  : 5%")
                print("----------------------------------------\n")

                update_file(Account_dict)

        elif choice == 3:
            print("------ DEPOSIT AMOUNT ------")
            acct_no = input("Enter Account Number: ")
            if acct_no in Account_dict:
                amount = int(input("Enter Deposit Amount: "))
                print("\n")
                Account_dict[acct_no].deposit(amount)
            else:
                print("\n Invalid Account Number!")

        elif choice == 4:
            print("------ WITHDRAW AMOUNT ------")
            acct_no = input("Enter Account Number: ")
            if acct_no in Account_dict:
                amount = int(input("Enter Withdrawal Amount: "))
                print("\n")
                Account_dict[acct_no].withdrawal(amount)
            else:
                print("\n Invalid Account Number!")

        elif choice == 5:
            print("------ CHECK BALANCE ------")
            acct_no = input("Enter Account Number: ")
            print("\n")
            if acct_no in Account_dict:
                Account_dict[acct_no].check_balance()
            else:
                print("\n Invalid Account Number!")

        elif choice == 6:
            print("------ ACCOUNT DETAILS ------")
            acct_no = input("Enter Account Number: ")
            print("\n")
            if acct_no in Account_dict:
                acct = Account_dict[acct_no]
                acct_type = "Saving" if isinstance(acct, SavingAccount) else "Current"

                print("\n=================================================")
                print("                 ACCOUNT SUMMARY                ")
                print("=================================================")
                print(f" Account Number   : {acct._account_no}")
                print(f" Account Holder   : {acct._account_name}")
                print(f" Account Type     : {acct_type}")
                print(f" Available Balance: Rs. {acct._balance}")
                print(f" ROI              : {int(acct._roi * 100)}%")
                print("=================================================\n")

            else:
                print("\n Invalid Account Number!")

        elif choice == 7:
            print("\n Thank you for using the Bank Application!")
            print(" Have a great day ahead!")
            print("\n=================================================\n")
            break

        else:
            print("\nInvalid Choice! Please enter a valid option.")

        ans = input("\n Do you want to continue (yes/no)? : ")
        print("\n")
