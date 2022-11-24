#CREATING A SEQUENCE OF RANDOM NUMBERS / WORDS AS DATABASE
import random

plans = ('SmartTrybe', 'smartOPTIMIZER', 'SmartCoonect', 'SmartTalk', 'SmartValue', 'SmartPremier')
num_list = ('0802', '0808', '0701', '0812','0708','0902', '0901', '0904', '0907', '0912')
airtel_start = random.choice(num_list)
begin = '234'
def random_end(n):
    rangestart = 10**(n-1)
    rangeend = (10**n)-1
    return random.randint(rangestart,rangeend)
airtel_end = str(random_end(7))

airtel_tariff = random.choice(plans)
phone_number = begin + airtel_start[1:] + airtel_end
alt_phone_number = airtel_start + airtel_end
puk_code = str(random_end(7))
serial_number = str(random_end(23))
data_balance = random_end(3)
airtime_balance = random.randint(0,1000)
# print(alt_phone_number)

# Airtel Social Media Handles
def socMed():
        social = input("1. Twitter\n"
                       "2. Email Me\n"
                       "3. Facebook\n"
                       "4. Download Airtel Care App\n"
                       "# Previous Menu\n")
        if social == "1":  #Twitter
            print("Airtel Twitter handle is @airtel_care and we are available 24/7 for support\n")
            twitter = input("# Previous Menu\n")
            if twitter == "#":
                socMed()

        if social == "2":   #Email
            print("Send an email to Airtel at customercare@ng.airtel.com\n")
            mail = input("# Previous Menu\n")
            if mail == "#":
                socMed()

        if social == "3":    #Facebook
            print("Follow the Airtel Facebook page www.facebook.com/AirtelNigeria\n")
            mail = input("# Previous Menu\n")
            if mail == "#":
                socMed()

        if social == "4":     #airtel Care App
            print("Our Mobile App (Airtel Care) is available on Google play store and Apple App Store\n"
                  "Download it for free. (data charges apply)")
            mail = input("# Previous Menu\n")
            if mail == "#":
                socMed()

        if social == '#':
            selectTrans()

#Billing & Tariff
def billTar():
    trans = input(
        "1. Smart Connect.\n"
        "2. Smart Trybe @11k(After 50 sec)\n"
        "3. Freedom Plan @12k flat rate\n"
        "4. Smart Talk @11k (N7 Access fee)\n"
        "5. Smart Value\n"
        "*. Next\n"
    )

    if trans == "1":   #Smartconnect
        print("Dial *311*2*Phone Number# to add FAF or *311*3*Phone Number# to remove FAF")
        x = input("# Previous Menu\n")
        while x != '#':
            print("Dial *311*2*Phone Number# to add FAF or *311*3*Phone Number# to remove FAF")
            x = input("# Previous Menu\n")
            if x == '#':
                billTar()

    elif trans == "2":   #SmartTrybe
        opt = input("Smart Trybe: 11k/s. 5. 1GB/N500 for 7 days\n"
                    "Press 1 to activate or dial *318#\n")
        if opt == "1":
            print("You are now on Airtel smartTRYBE. Make call to ALL NETWORKS in Nigeria at 11k/sec all day; after 1st 50secs at 25k/sec. Enjoy special data")
        law = input("* next\n")
        if law == "*":
            print("plan of N25 for 250MB (1 night) and N500 for 1GB (7 days). Dial *312# to purchase data plan\n"
                  "Session has ended")
            quit()

    elif trans == "3":     #Freedom Plan
        free = input("Freedom Plan: Flat rate 12k/sec from the 1st sec. N4/SMS\n"
                "Press 1 to activate or dial *152#\n")
        if free == "1":
            bACK =input("You can only migrate multiple times within 30 days if you have a balance of N100\n"
                        "#. For Previous menu\n")
            if bACK == '#':
                billTar()
            else:
                print('Session Has Ended')
                quit()

    elif trans == "4":    #sMART tALK
        smart = input("Smart Talk: All Networks @11k/s 24/7 Access fee N7\n"
                    "Press 1 to activate or dial *318#\n")
        if smart == "1":
            if airtime_balance < 100:
                print("You can only migrate multiple times within 30 days if you have a balance of N100")
            else:
                print('You  have successfully subscribed to Airtel Smart Talk. Congratulations')

    elif trans == "5":  # sMART vALUE
        value=input("Smart Value: All Networks @15/s 24/7. No Access fee\n"
                    "Press 1 to activate or dial *314#\n")
        if value=="1":
            print("You can only migrate multiple times within 30 days if you have a balance of N100")

    elif trans == "*":
        ast = input("15K flat rate\n"
                  "# Previous Menu\n")
        if ast == "#":
            selectTrans()

#Borrow
def borrCred():
    trans = input(
        "1. Borrow Credit(Welcome to Extra Credit)\n"
        "2. Me2u\n"
        "3. Do not Disturb\n"
        "4. VAS\n"
        "5. Loyalty\n"
        "6. Log a Complaint\n"
        "7. Store Locator\n"
        "# Previous Menu\n"
    )

    if trans =="1":
        print("Dial *500# to borrow Airtime/Data")

    elif trans == "2":
        print("You will be redirected to the Me2U menu")

    elif trans == "3":   #Do not disturb
        print("SMS STOP to 2442 for full DND\n"
              "SMS HELP to 2442 for partial DND")
        y = input("# Previous Menu\n")
        while y != '#':
            print("SMS STOP to 2442 for full DND\n"
                  "SMS HELP to 2442 for partial DND")
            y = input("# Previous Menu\n")
            if y == '#':
                borrCred()

    elif trans == "4":   #VAS
        print("You will be redirected to the VAS Services menu")

    elif trans == "5":
        print("You will be redirected to the Loyalty Scheme menu")

    elif trans == "6":
        print("Kindly visit this link https://selfcare.ng.airtel.com/LogRequest")

    elif trans == "7":
        print("Kindly visit this link http://www.alwayson.ng/Storelocator")

    else:
        borrCred()

# Manage my account
def manageAcc():
    trans = input(
        "1. My Data Balance\n"
        "2. My Balance\n"
        "3. My Data Plan\n"
        "4. My Number\n"
        "5. My Tariff Plan\n"
        "6. KYC Status\n"
        "7. My PUK\n"
        "8. My Serial Number\n"
        "# Previous menu\n"
    )

    if trans == "1":
        print(f"Dear Customer, your data balance is {data_balance}MB till 20/11/2022.\n")
    elif trans == "2":
        print(f"Your account balance is N {airtime_balance}.")
    elif trans == "3":
        print("You're subscribed to Airtel 2gb Monthly plan, valid for 30 days.")
    elif trans == "4":
        print(f"Your number is {phone_number}.")
    elif trans == "5":
        print(f"Your Tariff plan is {airtel_tariff}.")
    elif trans == "6":
        print("Service Temporarily unavailable.")
    elif trans == "7":
        print(f"Your PUK: {puk_code}.")
    elif trans == "8":
        print(f"Sim serial for the requesting number {alt_phone_number} is {serial_number}.")
    elif trans == '#':
        selectTrans()
    else:
        print('Invalid Code Entered\n"'
              '"start again')
        manageAcc()

#Transaction
def selectTrans():
    trans = input(
        "1. NIN Capture\n"
        "2. Buy bundles & Services\n"
        "3. Manage my Account\n"
        "4. Borrow Credit & other self services\n"
        "5. Billing and Tariff\n"
        "6. Bank Codes\n"
        "7. KYC Update\n"
        "* Next\n"
    )

    if trans =="1":
        print("Kindly dial *121*1# to submit your Government approved NIN")

    elif trans == "2":
        print("You will be redirected to the Buy Bundle and Services Menu")

    elif trans == "3":
        manageAcc()

    elif trans == "4":
        borrCred()

    elif trans == "5":
        billTar()

    elif trans == "6":
        print("Service Temporarily Unavailable")

    elif trans == "7":
        print("Service Temporarily Unavailable")

    elif trans == "*":
        contact = input("8. Contact us\n")
        if contact == "8":
         socMed()

    else:
        print('Invalid Entry')
        # selectTrans()
        x = input("Press 1 to try again\n"
                  "Press 2 to Quit\n"
                  )
        if x == '1':
            selectTrans()
        if x == '2':
            print('Seesion Ended')
            quit()


#DIALPAD
def confirmUSSD():
    ussd = input("Enter Code: ")
    if ussd == "*121#":
        print("Enter Transaction")
        selectTrans()

    else:
        print("Connection problem or invalid MMI.")
        confirmUSSD()

confirmUSSD()