account = {}


def create_account():
    account_number = input("Enter Account Number.")
    if account_number in account:
        print("Account already exit.")
        return 
    name = input("Enter Your Name.")
    balance = float(input("Enter Deposit Amount."))
    account[account_number] = {"name":name,"balance":balance}
    print("Account Created Successfully.")


def account_details():
    account_number = input("Enter Account Number.")
    if account_number in account:
        accounts = account[account_number]
        print(f"Account Number: {account_number}")
        print(f"Your name: {accounts['name']}")
        print(f"your balance: {accounts['balance']}")
    else:
        print("Account Not Found.")


def deposit():
    account_number = input("Enter Account Number.")
    if account_number in account:
        amount = float(input("Enter Amount."))
        account[account_number] ["balance"] += amount
        print("Deposit Successful.")
    else:
        print("Account Not Found.")


def bank_balance():
    account_number = input("Enter Account Number.")
    if account_number in account:
        print(f"balance:{account[account_number] ['balance']}")
    else:
        print("Account not Found.")    


def withdraw():
    account_number=input("Enter Account number.")
    if account_number in account:
        amount=float(input("Enter withdraw Amount."))
        if account[account_number]["balance"] >= amount:
            account[account_number]["balance"] -= amount
            print("Withdrawal Successful.")
        else:
            print("Enter Amount less than or equal to the balance.")    
    else:
        print("Account Not Found.")


def function():
    while True:
        print("\n Bank Managment System.")
        print("1.Create Bank account.")
        print("2.View All Bank Account Details.")
        print("3.Deposit Money.")
        print("4.Check Balance.")
        print("5.Withdraw Money.")
        print("6.Exit.")

        choice = input("Enter Your Choice:")

        if choice == "1":
            create_account()
        elif choice == "2":
            account_details() 
        elif choice == "3":
            deposit()  
        elif choice == "4":
            bank_balance()  
        elif choice ==  "5": 
            withdraw()  
        elif choice == "6":
            print("THANK YOU!")
            break
        else:
            print("Invalid Choice. Please Enter a valid choice.")

function()            