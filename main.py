#Enter Amount
def checkAmount(x):
    amt = input("Enter Amount: ")
    if amt.isnumeric():
        print(f"The {x} has been credited with {amt}")
    else:
        print(
            "Invalid Amount Entry\n"
            "Try Again"
        )
        checkAmount(x)

# Airtime Transaction
def airtimeTrans():
    phone = input("Enter Phone Number: ")
    if len(phone) == 11 and phone.isnumeric():
        checkAmount(phone)
    else:
        print(
            "Invalid Phone Number\n"
            "Try Again\n"
        )
        airtimeTrans()

# Transaction Entry
def transEntry():
    transCode = input(
        "1. Check Balance\n"
        "2. Buy Airtime\n"
        "3. Fund Tranfer\n"
        "Select Transaction: "
    )
    if transCode == "1":
        print("Your Account Balance is 200,000 naira")
    elif transCode == "2":
        airtimeTrans()
    elif transCode == "3":
        print("Fund Transfer")
    else:
        print(
            "Invalid Entry\n"
            "Try Again"
        )
        transEntry()


# Function To Cross-check USSD Code
def confirmUSSD():
    ussd = input("Enter USSD code: ")
    if ussd == "*123#":
        transEntry()
    else:
        print(
            "Invalid USSD code\n"
            "Try Again"
        )
        confirmUSSD()

#Calling the Function
confirmUSSD()