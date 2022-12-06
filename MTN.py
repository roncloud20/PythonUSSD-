# Recharge4ME
def rechame():
    tweak = input("Enter 1 to recharge #100 to get #600\n")
    if tweak == "1":
        print("You have been credited with #600")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        rechame()

# enjoy 200MB for #50
def enfive():
    tweet = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
        "Select an option: "
    )
    if tweet == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif tweet == "2":
        print("Activation of 200MB was successful")
    elif tweet == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        enfive()

# enjoy 1GB for #200
def enjz():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
        "Select an option: "
    )
    if twen == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of 1GB was successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        enjz()

# TopDeal4ME
def topDeal():
    topMe = input(
        "Enter 1 to enjoy 1GB for #200\n"
        "Enter 2 to enjoy 200MB for #50\n"
        "Select an option: "
    )
    if topMe == "1":
        enjz()
    elif topMe == "2":
        enfive()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!\n"
        )
        topDeal()

# Hot Deals
def hotdeals():
    hod = input(
        "Enter 1 to TopDeal4ME\n"
        "Enter 2 to Recharge4ME\n"
        "Select an option: "
    )
    if hod == "1":
        topDeal()
    elif hod == "2":
        rechame()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        hotdeals()

# Showmax Pro(LIVE Football,Movies,Series & Kids)
def showmaxlive():
    slim = input(
        "Enter 1 to Access only @N3200\n"
        "Enter 2 to Access + 2.5GB@N3700\n"
        "Enter 3 to Access + 5.5GB@N4200\n"
        "Enter 99 to Go back\n"
        "Select an option: "
    )
    if slim == "1":
        hod = input(
            "Enter 1 to Proceed\n"
            "Enter 99 to Go back\n"
            "Select an option: "
        )
        if hod == "1":
            print("Activation of Showmax Mobile Pro(Access only) for 30days at N3200 was successful")
        elif hod == "99":
            videopacks()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            selectTrans()
    elif slim == "2":
        hod = input(
            "Enter 1 to Proceed\n"
            "Enter 99 to Go back\n"
            "Select an option: "
        )
        if hod == "1":
            print("Activation of Showmax Mobile Pro Access for 30days + 2.5GB@N3700 was successful")
        elif hod == "99":
            videopacks()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            selectTrans()
    elif slim == "3":
        hod = input(
            "Enter 1 to Proceed\n"
            "Enter 99 to Go back\n"
            "Select an option: "
        )
        if hod == "1":
            print("Activation of Showmax Mobile Pro Access for 30days + 5.5GB@N4200 was successful")
        elif hod == "99":
            videopacks()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            selectTrans()
    elif slim == "99":
        videopacks()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        selectTrans()

# Showmax(Movies,Series & Kids)
def showmaxmovies():
    slim = input(
        "Enter 1 to Access only @N1200\n"
        "Enter 2 to Access + 2.5GB@N1700\n"
        "Enter 3 to Access + 5.5GB@N2200\n"
        "Enter 99 to Go back\n"
        "Select an option: "
    )
    if slim == "1":
        hod = input(
            "Enter 1 to Proceed\n"
            "Enter 99 to Go back\n"
            "Select an option: "
        )
        if hod == "1":
            print("Activation of Showmax Mobile(Access only) for 30days at N1200 was successful")
        elif hod == "99":
            videopacks()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            selectTrans()
    elif slim == "2":
        hod = input(
            "Enter 1 to Proceed\n"
            "Enter 99 to Go back\n"
            "Select an option: "
        )
        if hod == "1":
            print("Activation of Showmax Mobile Access for 30days + 2.5GB@N1700 was successful")
        elif hod == "99":
            videopacks()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            selectTrans()
    elif slim == "3":
        hod = input(
            "Enter 1 to Proceed\n"
            "Enter 99 to Go back\n"
            "Select an option: "
        )
        if hod == "1":
            print("Activation of Showmax Mobile Access for 30days + 5.5GB@N2200 was successful")
        elif hod == "99":
            videopacks()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            selectTrans()
    elif slim == "99":
        videopacks()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        selectTrans()

# 3 Hours@N400 for 2.25GB
def threehour():
    calm = input(
        "You will be charged N400 for 2.25GB 3 Hours access time on StarTimes.Available for use within for 24 hours\n"
        "Enter 1 to Proceed\n"
        "Enter 2 to buy for a friend\n"
        "Enter 0 to go back\n"
        "Select an option: "
    )
    if calm == "1":
        print("Activation of 750MB at N150 has been successful")
    elif calm == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            selectTrans()
    elif calm == "0":
        videopacks()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        selectTrans()

# 1 Hour@N150 for N750MB
def one():
    calm = input(
        "You will be charged N150 for 750MB 1 Hour access time on StarTimes.Available for use within for 24 hours\n"
        "Enter 1 to Proceed\n"
        "Enter 2 to buy for a friend\n"
        "Enter 0 to go back\n"
        "Select an option: "
    )
    if calm == "1":
        print("Activation of 750MB at N150 has been successful")
    elif calm == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            selectTrans()
    elif calm == "0":
        videopacks()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        selectTrans()

# 2GB Weekly@N200(11pm - 6am)
def two():
    calm = input(
        "You will be charged N200 for 2GB weekly streaming on YouTube.Available for use within for 11pm - 6am\n"
        "Enter 1 to Proceed\n"
        "Enter 2 to buy for a friend\n"
        "Enter 0 to go back\n"
        "Select an option: "
    )
    if calm == "1":
        print("Activation of 500MB at N50 has been successful")
    elif calm == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            selectTrans()
    elif calm == "0":
        videopacks()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        selectTrans()

# 500MB@N50(12am - 5am)
def five():
    calm = input(
        "You will be charged N50 for 500MB streaming on YouTube.Available for use within for 12am - 5am\n"
        "Enter 1 to Proceed\n"
        "Enter 2 to buy for a friend\n"
        "Enter 0 to go back\n"
        "Select an option: "
    )
    if calm == "1":
        print("Activation of 500MB at N50 has been successful")
    elif calm == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            selectTrans()
    elif calm == "0":
        videopacks()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        selectTrans()

# 3hours@N130 for 1.2GB
def three():
    calm = input(
        "You will be charged N130 for 1.2GB 3 Hours streaming on YouTube.Available for use within for 24 hours\n"
        "Enter 1 to Proceed\n"
        "Enter 2 to buy for a friend\n"
        "Enter 0 to go back\n"
        "Select an option: "
    )
    if calm == "1":
        print("Activation of 1.2GB at N130 has been successful")
    elif calm == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            selectTrans()
    elif calm == "0":
        videopacks()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        selectTrans()

# 1hour@N50 for 400MB
def four():
    calm = input(
        "You will be charged N50 for 400MB 1 Hour streaming on YouTube.Available for use within for 24 hours\n"
        "Enter 1 to Proceed\n"
        "Enter 2 to buy for a friend\n"
        "Enter 0 to go back\n"
        "Select an option: "
    )
    if calm == "1":
        print("Activation of 400MB at N50 has been successful")
    elif calm == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            selectTrans()
    elif calm == "0":
        videopacks()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        selectTrans()

# Video Packs
def videopacks():
    car = input(
        "Enter 1 to YouTube Video Packs\n"
        "Enter 2 to StarTimes Video Packs\n"
        "Enter 3 to 1GB(YouTube Only) + 500MB(Data access)\n"
        "Enter 4 to Showmax Mobile\n"
        "Select an option: "
    )
    if car == "1":
        calm = input(
            "Enter 1 to 1hour@N50 for 400MB\n"
            "Enter 2 to 3hours@N130 for 1.2GB\n"
            "Enter 3 to 500MB@N50(12am - 5am)\n"
            "Enter 4 to 2GB Weekly@N200(11pm - 6am)\n"
            "Enter 5 to Check Balance\n"
            "Select an option: "
        )
        if calm == "1":
            four()
        elif calm == "2":
            three()
        elif calm == "3":
            five()
        elif calm == "4":
            two()
        elif calm == "5":
            Balance()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            videopacks()
    elif car == "2":
        cool = input(
            "Subscribe to a plan & enjoy video streaming or download on StarTimes.\n"
            "Enter 1 to 1 Hour@N150 for N750MB\n"
            "Enter 2 to 3 Hours@N400 for 2.25GB\n"
            "Enter 3 to Check Balance\n"
            "Select an option: "
        )
        if cool == "1":
            one()
        elif cool == "2":
            threehour()
        elif cool == "3":
            Balance()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            videopacks()
    elif car == "3":
        cool = input(
            "Enter 1 to 1hour @N50 for 400MB\n"
            "Enter 2 to 3hours@N130 for 1.2GB\n"
            "Enter 3 to 500MB@N50(12am - 5am)\n"
            "Enter 4 to 2GB Weekly@N200(11pm - 6am)\n"
            "Enter 5 to Check Balance\n"
            "Select an option: "
        )
        if cool == "1":
            four()
        elif cool == "2":
            three()
        elif cool == "3":
            five()
        elif cool == "4":
            two()
        elif cool == "5":
            two()
        elif cool == "6":
            Balance()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            videopacks()
    elif car == "4":
        cool = input(
            "Select a plan for content + access on Showmax\n"
            "Enter 1 to Showmax(Movies,Series & Kids)\n"
            "Enter 2 to Showmax Pro(LIVE Football,Movies,Series & Kids)\n"
            "Enter 3 to Check Balance\n"
            "Select a plan: "
        )
        if cool == "1":
            showmaxmovies()
        elif cool == "2":
            showmaxlive()
        elif cool == "3":
            Balance()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        videopacks()

# Request from friends
def friends():
    one = input("Enter phone number: ")
    if len(one) == 11:
        print("Your request has been sent")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
            )
        friends()

# Opera Mini
def OperaMinib():
    opera = input(
        "Enter 1 for #20/25mb/1 day\n"
        "Enter 2 for #50/100mb/7 days\n"
        "Enter 3 for #100/300mb/30 days\n"
        "Select an option: "
    )
    if opera == "1":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif opera == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif opera == "3":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        OperaMinib()

# YIT
def YITb():
    yit = input("Enter 1 to buy #100 for 350mb @ daily\n"
                "Select an option: ")
    if yit == "1":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        YITb()

# Social App
def socialAppb():
    SocialA = input(
        "Enter 1 for daily @ #50 for 150mb\n"
        "Enter 2 for weekly @ #100 for 350mb\n"
        "Enter 3 for monthly @ #250 for 1GB\n"
        "Select an option: "
    )
    if SocialA == "1":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif SocialA == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif SocialA == "3":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        socialAppb()

# Ayoba
def Ayobab():
    Ay = input(
        "Enter 1 to buy #25 for 25mb/1day\n"
        "Enter 2 to buy #50 for 50mb/7days\n"
        "Enter 3 to buy #150 for 150mb\n"
        "Select an option: "
    )
    if Ay == "1":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif Ay == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif Ay == "3":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        Ayobab()

# Tiktok
def Tiktokb():
    Tik = input(
        "Enter 1 to buy #50 for 200mb/1day\n"
        "Enter 2 to buy #350 for 2GB/7days\n"
        "Select an option: "
    )
    if Tik == "1":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif Tik == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        Tiktokb()

# Instagram
def Instagramb():
    Insta = input(
        "Enter 1 to buy #100 for 250mb/1 day\n"
        "Enter 2 to buy #100 for 350mb\n"
        "Enter 3 to buy #200 for 1GB\n"
        "Enter 4 to buy #200 for 1GB/3-days\n"
        "Select an option: "
    )
    if Insta == "1":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif Insta == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif Insta == "3":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif Insta == "4":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        Instagramb()

# Facebook
def FaceB():
    faceB = input(
        "Enter 1 to buy daily @ #25 for 25mb\n"
        "Enter 2 to buy weekly @ #50 for 50mb\n"
        "Enter 3 to buy monthly @ #150 for 150\n"
      )
    if faceB == "1":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif faceB == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif faceB == "3":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        FaceB()

# Whatsapp
def WhatsAppb():
    watsup = input(
        "Enter 1 for daily @ #25 for 25mb\n"
        "Enter 2 for weekly @ #50 for 50mb\n"
        "Enter 3 for monthly @ #150 for 150mb\n"
        "Select an option: "
       )
    if watsup == "1":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif watsup == "2":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    elif watsup == "3":
        Tfive = input("Enter Recipient Number: ")
        if len(Tfive) == 11:
            print("Your transfer was successful")
        else:
            print(
                "Wrong number\n"
                "Try Again\n"
            )
            giftData()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        WhatsAppb()

# Social Bundles
def socialBun():
    socials = input(
        "Enter 1 for WhatsApp\n"
        "Enter 2 for FaceBook\n"
        "Enter 3 for Instagram\n"
        "Enter 4 for Tiktok\n"
        "Enter 5 for Ayoba\n"
        "Enter 6 for All Social Bundles\n"
        "Enter 7 for YouTube, Instagram, and TikTok\n"
        "Enter 8 for Opera Mini $ News\n"
        "Select an option: "
        )
    if socials == "1":
        WhatsAppb()
    elif socials == "2":
        FaceB()
    elif socials == "3":
        Instagramb()
    elif socials == "4":
        Tiktokb()
    elif socials == "5":
        Ayobab()
    elif socials == "6":
        socialAppb()
    elif socials == "7":
        YITb()
    elif socials == "8":
        OperaMinib()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        giftData()

# SeventyFive
def seventyFive():
    seven = input("Enter Recipient Number: ")
    if len(seven) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        seventyFive()

# FiftyK
def fiftyK():
    Fiftyk = input("Enter Recipient Number: ")
    if len(Fiftyk) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
            )
        fiftyK()

# ThreeM
def threeM():
    ThreeM = input(
        "Enter 1, #50000 for 400GB\n"
        "Enter 2, #75000 for 600GB\n"
        "Select an option"
    )
    if ThreeM == "1":
        fiftyK()
    elif ThreeM == "2":
        seventyFive()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        threeM()

# Thirty
def thirtyb():
    Thirty = input("Enter Recipient Number: ")
    if len(Thirty) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        thirtyb()

# Twenty
def twentya():
    Twenty = input("Enter Recipient Number: ")
    if len(Twenty) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
            )
        twentya()

# Eight
def eight():
    Eight = input("Enter Recipient Number: ")
    if len(Eight) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
            )
        eight()

# twoM
def twoM():
    TwoM = input(
        "Enter 1, #8000 for 30GB\n"
        "Enter 2, #20000 for 100GB\n"
        "Enter 3, #30000 for 160GB\n"
        "Select an option: "
    )
    if TwoM == "1":
        eight()
    elif TwoM == "2":
        twentya()
    elif TwoM == "3":
        thirtyb()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        twoM()

# threeK
def threeK():
    Three = input("Enter Recipient Number: ")
    if len(Three) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        threeK()

# fourK
def fourK():
    Four = input("Enter Recipient Number: ")
    if len(Four) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        fourK()

# SixK
def sixK():
    six = input("Enter Recipient Number: ")
    if len(six) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        sixK()

# TwoK
def twoK():
    Two = input("Enter Recipient Number: ")
    if len(Two) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        twoK()

# OneTwo
def oneTwoa():
    oneK = input("Enter Recipient Number: ")
    if len(oneK) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        oneTwoa()

# Monthly
def monthlya():
    Monthly = input(
        "Enter 1, #1200 for 2GB\n"
        "Enter 2, #2000 for 6GB\n"
        "Enter 3, #6000 for 25GB\n"
        "Enter 4, #4000 for 17GB\n"
        "Enter 5, #3000 for 2GB(2 days)\n"
        "Select an option: "
    )
    if Monthly == "1":
        oneTwoa()
    elif Monthly == "2":
        twoK()
    elif Monthly == "3":
        sixK()
    elif Monthly == "4":
        fourK()
    elif Monthly == "5":
        threeK()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        monthlya()

# Five Hundred
def FiveH():
    fiveh = input("Enter Reciepient Number: \n")
    if len(fiveh) == 11:
        print("Your transfer was sucessful\n")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        FiveH()

# One Thousand
def oneThousandb():
    oneT = input("Enter Reciepient Number: \n")
    if len(oneT) == 11:
        print("Your transfer was sucessful\n")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        oneThousandb()

# One five
def oneFiveb():
    one = input("Enter Reciepient Number: \n")
    if len(one) == 11:
        print("Your transfer was sucessful\n")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        oneFiveb()

# Five Hundred
def Fhundred():
    five = input("Enter Recipient Number: ")
    if len(five) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        Fhundred()

# Three Hundred
def Thundred():
    three = input("Enter Recipient Number: ")
    if len(three) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        Thundred()

# Weekly
def weeklya():
    Weekly = input(
        "Enter 1, #300 for 350mb\n"
        "Enter 2, #500 for 750mb\n"
        "Enter 3, #1500 for 6GB\n"
        "Enter 4, #1000 for 2GB\n"
        "Enter 5, #500 for 1GB\n"
        "Select an option: "
    )
    if Weekly == "1":
        Thundred()
    elif Weekly == "2":
        Fhundred()
    elif Weekly == "3":
        oneFiveb()
    elif Weekly == "4":
        oneThousandb()
    elif Weekly == "5":
        FiveH()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        weeklya()

# Five Hundred
def fiveHundred():
    fiveH = input("Enter Recipient Number: ")
    if len(fiveH) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        fiveHundred()

# Three Hundred
def threeHundred():
    threeH = input("Enter Recipient Number: ")
    if len(threeH) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        threeHundred()

# Two Hundred
def twoHundred():
    twoH = input("Enter Recipient Number: ")
    if len(twoH) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
            )
        twoHundred()

# One Hundred
def hundreda():
    Hundred = input("Enter Recipient Number: ")
    if len(Hundred) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        hundreda()

# Fifty
def fiftya():
    Fifty = input("Enter Recipient Number: ")
    if len(Fifty) == 11:
        print("Your transfer was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        dataP()

# Dailya
def dailya():
    Daily = input(
        "Enter 1, #50 for 40mb\n"
        "Enter 2, #100 for 100mb\n"
        "Enter 3, #200 for 200MB(3-days plan)\n"
        "Enter 4, #300 for 1GB\n"
        "Enter 5, #500 for 2GB(2 days)\n"
        "Select an option: "
    )
    if Daily == "1":
        fiftya()
    elif Daily == "2":
        hundreda()
    elif Daily == "3":
        twoHundred()
    elif Daily == "4":
        threeHundred()
    elif Daily == "5":
        fiveHundred()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        dailya()

# Data plans
def dataP():
    data = input(
        "Enter 1 for daily plans\n"
        "Enter 2 for Weekly plans\n"
        "Enter 3 for Monthly plans\n"
        "Enter 4 for 2-Months plans\n"
        "Enter 5 for 3-Months plans\n"
        "Select an option: "
    )
    if data == "1":
        dailya()
    elif data == "2":
        weeklya()
    elif data == "3":
        monthlya()
    elif data == "4":
        twoM()
    elif data == "5":
        threeM()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )

# Buy for friends
def Friends():
    friend = input(
        "Enter 1 to buy data plans\n"
        "Enter 2 to buy social bundles\n"
        "Enter 3 for video packs\n"
        "Select an option: "
    )
    if friend == "1":
        dataP()
    elif friend == "2":
        socialBun()
    elif friend == "3":
        print("Select plan: \n")
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        Friends()

# Amount
def amount(num):
    amt = input("Enter Amount: ")
    if amt.isnumeric():
        print(f"{num} has been credited with {amt} megabyte")
    else:
        print(
            "Invalid Number\n"
            "Try Again\n"
        )
        amount(num)

# From data balance
def dataB():
    num = input("Enter Recipient Number: ")
    if len(num) == 11:
        amount(num)
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
              )
        dataB()

# Gift Data
def giftData():
    gift = input(
        "Enter 1 to transfer from Data Balance\n"
        "Enter 2 to buy for a friend\n"
        "Enter 3 to request from a friend\n"
        "Enter 4 to view pending request\n"
        "Enter 0 to go back\n"
        "Select an option: "
    )
    if gift == "1":
        dataB()
    elif gift == "2":
        print(
            "Welcome to MTN Data Gifting."
        )
        Friends()
    elif gift == "3":
        print(
            "To request Data from a friend"
        )
        friends()
    elif gift == "4":
        print(
            "Yello! You have no pending request\n"
            "Thank You\n"
            )
    elif gift == "0":
        selectTrans()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        giftData()

# Borrow Credit or Recharge
def borrowCredit():
    credit = input(
        "Enter 1 to borrow airtime\n"
        "Enter 2 to borrow data\n"
        "Enter 3 to recharge\n"
        "Enter 0 to go back\n"
        "Select an option: "
    )
    if credit == "1":
        print("""You are qualified for this process but your airtime
        balance is high. You borrow airtime or data when your balance is lower than N5.00""")
    elif credit == "2":
        print("""You are qualified for this process but your airtime
        balance is high. You borrow airtime or data when your balance is lower than N5.00""")
    elif credit == "3":
        print("You will be referred to MTN OnDemand")
    elif credit == "0":
        selectTrans()
    else:
        print(
            "Invalid code\n"
            "Try Again\n"
        )
        borrowCredit()

# Onefiftymins
def onefiftyMin():
    ofm = input(
        "1. Proceed: \n"
        "0. Back\n"
        "00. MainMenu\n"
        "Select an option: "
    )
    if ofm == "1":
        print("Your activation of IDB1,500 is successful, valid for only 30 days")
    elif ofm == "0":
        Suscribe()
    elif ofm == "00":
        selectTrans()
    else:
        print(
            "Invalid code\n"
            "Try Again\n"
        )
        onefiftyMin()

# Fortymins
def fortyMin():
    fm = input(
        "1. Proceed: \n"
        "0. Back\n"
        "00. MainMenu\n"
    )
    if fm == "1":
        print("Your activation of IDB500 is successful, valid for only 7 days")
    elif fm == "0":
        Suscribe()
    elif fm == "00":
        selectTrans()
    else:
        print(
            "Invalid code\n"
            "Try Again\n"
        )
        fortyMin()

# Twentymins
def twentyMin():
    tm = input(
        "1. Proceed: \n"
        "0. Back\n"
        "00. MainMenu\n"
        "Select an option: "
    )
    if tm == "1":
        print("Your activation of IDB300 is successful, valid for only 3 days")
    elif tm == "0":
        Suscribe()
    elif tm == "00":
        selectTrans()
    else:
        print(
            "Invalid code\n"
            "Try Again\n"
        )
        twentyMin()

# Subscribe
def Subscribe():
    sus = input(
        "1. IDB300\n"
        "2. IDB500\n"
        "3. IDB1,500\n"
        "0. Back\n"
        "00. MainMenu\n"
        "Select an option: "
    )
    if sus == "1":
        print("Buy IDB300 and get 20mins for calls to eligible destinations, valid for 3 days")
        twentyMin()
    elif sus == "2":
        print("Buy IDB500 and get 40mins for calls to eligible destinations, valid for 7 days")
        fortyMin()
    elif sus == "3":
        print("Buy IDB1,500 and get 150mins for calls to eligible destinations, valid for 30 days")
        onefiftyMin()
    elif sus == "0":
        ICB()
    elif sus == "00":
        Roaming()
    else:
        print(
            "Invalid code\n"
            "Try Again\n"
        )
        Subscribe()


# International Calling Bundle
def ICB():
    icb = input(
        "Enter 1 to suscbribe to Int'L Calling Bundles\n"
        "Enter 2 for Eligible Countries(Bundle applicable to selected networks in destinations listed\n"
        "0. back\n"
        "Select an option: "
    )
    if icb == "1":
        Subscribe()
    elif icb == "2":
        print(
            "1. Canada\n"
            "2. China\n"
            "3. Denmark\n"
            "4. Norway\n"
            "5. India\n"
            "6. Ireland\n"
            "7. Malaysia\n"
            "8. Romania\n"
            "9. South Korea\n"
            "10. United State"
        )
    elif icb == "0":
        Roaming()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        ICB()

# Eligible Destinations
def ED():
    ed = input(
        "Enter 1 for UK(Vodafone, 02, Orange $ T-Mobile)\n"
        "Enter 2 for USA(AT&T)\n"
        "Enter 3 for France(SFR & Orange)\n"
        "Enter 4 for Germany(Vodafone $ T-Mobile)\n"
        "Enter 5 for Italy(Vodafone $ H3G)\n"
        "Select an option: "
    )
    if ed == "1":
        print("Invalid input, please try again")
    elif ed == "2":
        print("Invalid input, please try again")
    elif ed == "3":
        print("Invalid input, please try again")
    elif ed == "4":
        print("Invalid input, please try again")
    elif ed == "5":
        print("Invalid input, please try again")
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        ED()

# Free incoming roaming call
def FIRC():
    firc = input(
        "Enter 1 to Check Eligibility\n"
        "Enter 2 for Eligible Destination\n"
        "Enter 3 to Check free incoming minutes\n"
    )
    if firc == "1":
        print(
            "Dear customer, you are eligible to recieve calls for free during your next trip abroad.\n"
            "Please dial *131*5*3*3# for applicable incoming minutes."
            )
    elif firc == "2":
        ED()
    elif firc == "3":
        print("You have 300 Mins from your free incoming mins, valid till 24/11/22")
    else:
        print(
            "Invalid code\n"
            "Try Again\n"
        )
        FIRC()

# Country
def country():
    C = input(
        "Enter 1 for Lufthansa\n"
        "Enter 2 for Turkish\n"
        "Enter 3 for Emirate\n"
        "Enter 4 for Qatar\n"
        "Enter 5 for Etihad\n"
        "Enter 6 for Camp Nou\n"
        "Select an option: "
    )
    if C == "1":
        print("Invalid input, try again")
    elif C == "2":
        print("Invalid input, try again")
    elif C == "3":
        print("Invalid input, try again")
    elif C == "4":
        print("Invalid input, try again")
    elif C == "5":
        print("Invalid input, try again")
    elif C == "6":
        print("Invalid input, try again")
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        country()

# bBF
def bBF():
    bff = input("Enter Recipients Number: ")
    if len(bff) == 11:
        print(f"The activation of #5000 TravelPass for 7days to {bff} is successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
        )
        Roaming()

# Next
def next():
    P = input("Enter to 'Proceed' to continue: ")
    if P == "Proceed":
        print("Your activation of 50mb for #2,000 was successful\n")
    else:
        print(
            "Insufficient Balance\n"
            "Try Again\n"
            )
        Roaming()

# Inflight Roaming Data
def IRD():
    ird = input(
        "Enter 1 for 50mb @ #2,000\n"
        "Enter 2 view Airlines\n"
    )
    if ird == "1":
        calm = input(
            "1. Next\n"
            "2. Buy for a friend\n"
            "Select: "
        )
        if calm == "1":
            next()
        elif calm == "2":
            bBF()
        else:
            print(
                "Invalid Entry\n"
                "Try Again\n"
            )
            Roaming()
    elif ird == "2":
        print(
            "Aeromobile Inflight service will be available on select airplanes from the below airlines\n"
            "Select: \n"
        )
        country()
    else:
        print(
            "Invalid Entry\n"
            "Try Again\n"
        )
        IRD()

# Destination
def eDestination():
    destination = input(
        "Enter 1 for UAE(Etisalat)\n"
        "Enter 2 for (AT&T & T-Mobile)\n"
        "Enter 3 for Saudi Arabia(Eithad & Zain)\n"
        "Enter 4 for Canada(Bell, Rogers, Sask Tel & TELUS)\n"
        "Select an option: "
    )
    if destination == "1":
        print("Sorry service is temporary unavailable")
    elif destination == "2":
        print("Sorry service is temporary unavailable")
    elif destination == "3":
        print("Sorry service is temporary unavailable")
    elif destination == "4":
        print("Sorry service is temporary unavailable")
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        eDestination()

# Eligible Bundles
def eBundles():
    Ebundles = input(
        "Enter 1 to buy #2000 for 4.5GB\n"
        "Enter 2 to buy #2500 for 6GB\n"
        "Enter 3 to buy #3000 for 10GB\n"
        "Enter 4 to buy #3500 for 12GB\n"
        "Enter 5 to buy #5000 for 20GB\n"
        "Enter 6 to buy #10000 for 40GB\n"
        "Enter 7 to buy #3500 for 15GB\n"
        "Select an option: "
    )
    if Ebundles == "1":
        print("Sorry service is temporary unavailable")
    elif Ebundles == "2":
        print("Sorry service is temporary unavailable")
    elif Ebundles == "3":
        print("Sorry service is temporary unavailable")
    elif Ebundles == "4":
        print("Sorry service is temporary unavailable")
    elif Ebundles == "5":
        print("Sorry service is temporary unavailable")
    elif Ebundles == "6":
        print("Sorry service is temporary unavailable")
    elif Ebundles == "7":
        print("Sorry service is temporary unavailable")
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        eBundles()

# Data Hybrid
def DataH():
    dataH = input(
        "Enter 1 for Eligible Bundles\n"
        "Enter 2 for Destination\n"
        "Select an option: "
    )
    if dataH == "1":
        eBundles()
    elif dataH == "2":
        eDestination()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        DataH()

# Eligible Destination
def EligibleD():
    eligible = input(
        "Enter 1 for UAE(Etisalat)\n"
        "Enter 2 for (AT&T & T-Mobile)\n"
        "Enter 3 for Saudi Arabia(Eithad & Zain)\n"
        "Enter 4 for Canada(Bell, Rogers, Sask Tel & TELUS)\n"
        "Select an option: "
    )
    if eligible == "1":
        print("Sorry service is temporary unavailable")
    elif eligible == "2":
        print("Sorry service is temporary unavailable")
    elif eligible == "3":
        print("Sorry service is temporary unavailable")
    elif eligible == "4":
        print("Sorry service is temporary unavailable")
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        EligibleD()

# BFF3
def BFF3():
    bff = input("Enter Recipients Number: ")
    if len(bff) == 11:
        print(f"The activation of #5000 TravelPass for 7days to {bff} is successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
        )
        BFF3()

# Seven Days 2
def sevenDays2():
    seven2 = input(
        "Enter 1 to proceed(One-off)\n"
        "Enter 2 to buy for a friend\n"
    )
    if seven2 == "1":
        print("Activation of #10000 TravelPass for 14days was successful")
    elif seven2 == "2":
        BFF3()
    else:
        print(
            "Insufficient balance\n"
            "Try Again\n"
        )
        sevenDays2()

# BFF2
def BFF2():
    bff = input("Enter Recipients Number: ")
    if len(bff) == 11:
        print(f"The activation of #10000 TravelPass for 14days to {bff} is successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
        )
        BFF2()

# 14 DAYS
def fourteenDays():
    four = input(
        "Enter 1 to proceed(One-off)\n"
        "Enter 2 to buy for a friend\n"
    )
    if four == "1":
        print("Activation of #10000 TravelPass for 14days was successful")
    elif four == "2":
        BFF2()
    else:
        print(
            "Insufficient balance\n"
            "Try Again\n"
        )
        fourteenDays()

# BFF
def BFF():
    bff = input("Enter Recipients Number: ")
    if len(bff) == 11:
        print(f"The activation of #5000 TravelPass for 7days to {bff} was successful")
    else:
        print(
            "Wrong number\n"
            "Try Again\n"
        )
        BFF()

# Seven Days
def sevenDays():
    seven = input(
        "Enter 1 to proceed(One-off)\n"
        "Enter 2 to buy for a friend\n"
    )
    if seven == "1":
        print("Activation of #5000 TravelPass for 7days was sucessful\n")
    elif seven == "2":
        BFF()
    else:
        print(
            "Insufficient balance\n"
            "Try Again\n"
        )
        sevenDays()

# Travel Pass
def TravelPass():
    travel = input(
        "Enter 1 for 7Days TravelPass @#5000\n"
        "Enter 2 for 14Days TravelPass @#10000\n"
        "Enter 3 for 7Days TravelPass(Data) @#5000\n"
        "Enter 4 for Eligible Destination\n"
        "Select an option: "
    )
    if travel == "1":
        print(
            "Enjoy unlimited outgoing calls $ SMS with 7days TravelPass Plan@#5000(Fair Usage apply)"
        )
        sevenDays()
    elif travel == "2":
        print(
            "Enjoy unlimited outgoing calls/SMS with 14days TravelPass Plan@#10000(Fair Usage apply)"
        )
        fourteenDays()
    elif travel == "3":
        print(
            "Get 1GB TravelPass valid for 7days @#5000"
        )
        sevenDays2()
    elif travel == "4":
        print("Select plan: \n")
        EligibleD()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        TravelPass()

# ROAMING
def Roaming():
    roaming = input(
        "Enter 1 for TravelPass Plans\n"
        "Enter 2 for Data Hybrid\n"
        "Enter 3 for Inflight Roaming Data\n"
        "Enter 4 for Free incoming roaming call\n"
        "Enter 5 for Intl Calling Bundle\n"
        "Enter 6 for Roaming Balance Check\n"
        "Enter 0 to Go Back\n"
        "Select an option: "
    )
    if roaming == "1":
        print("Select Plans: \n")
        TravelPass()
    elif roaming == "2":
        print("Select Plans: \n")
        DataH()
    elif roaming == "3":
        print("Select Plans: \n")
        IRD()
    elif roaming == "4":
        print("Select Plans: \n")
        FIRC()
    elif roaming == "5":
        print("Select Plans: \n")
        ICB()
    elif roaming == "6":
        print(
            "Dear customer, you do not have any active data bundles.\n"
            "Please dial *131*1# to buy another Data Bundle\n"
              )
    elif roaming == "0":
        selectTrans()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        Roaming()

# BALANCE CHECK
def Balance():
    print(
        "Your Balance:\n"
        "Airtime is N1,850\n"
        "Data is 2430MB expires on 12/9/2022"
    )

# Social Mega Bundles
def SMB():
    smb = input(
        "Enter 1 for 750mb for #200(3 days)\n"
        "Enter 2 for 2GB for #300(7 days)\n"
    )
    if smb == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Social Mega Bundles Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 750MB for 3 days has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif smb == "2":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Social Mega Bundles Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 2GB for 7 days has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        SMB()

# OPERA MINI AND NEWS
def OperaMini():
    opera = input(
        "Enter 1 for #20/25mb/1 day\n"
        "Enter 2 for #50/100mb/7 days\n"
        "Enter 3 for #100/300mb/30 days\n"
    )
    if opera == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your OPERA MINI AND NEWS Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 25MB for 1 day has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif opera == "2":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your OPERA MINI AND NEWS Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 100MB for 7 days has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif opera == "3":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your OPERA MINI AND NEWS Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 300MB for 30 days has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        OperaMini()

# YOUTUBE,INSTAGRAM $ TIKTOK
def YIT():
    yit = input("Enter 1 to buy #100 for 350mb @ daily\n")
    if yit == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your YOUTUBE,INSTAGRAM & TIKTOK Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 350MB for daily has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        YIT()

# ALL SOCIAL BUNDLES
def socialApp():
    SocialA = input(
        "Enter 1 for daily @ #50 for 150mb\n"
        "Enter 2 for weekly @ #100 for 350mb\n"
        "Enter 3 for monthly @ #250 for 1GB\n"
    )
    if SocialA == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Social Bundles Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 150MB for daily has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif SocialA == "2":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Social Bundles Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 350MB for weekly has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif SocialA == "3":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Social Bundles Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 1GB for monthly has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        socialApp()

# AYOBA
def Ayoba():
    Ay = input(
        "Enter 1 to buy #25 for 25mb/1day\n"
        "Enter 2 to buy #50 for 50mb/7days\n"
        "Enter 3 to buy #150 for 150mb\n"
    )
    if Ay == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Ayoba Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 25MB for 1 day has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif Ay == "2":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Ayoba Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 50MB for 7 days has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif Ay == "3":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Tiktok Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 150MB has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        Ayoba()

# TIKTOK
def Tiktok():
    Tik = input(
        "Enter 1 to buy #50 for 200mb/1day\n"
        "Enter 2 to buy #350 for 2GB/7days\n"
    )
    if Tik == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Tiktok Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 200MB for 1 day has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif Tik == "2":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Tiktok Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 2GB for 7 days has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        Tiktok()

# INSTAGRAM
def Instagram():
    Insta = input(
        "Enter 1 to buy #100 for 250mb/1 day\n"
        "Enter 2 to buy #100 for 350mb\n"
        "Enter 3 to buy #200 for 1GB\n"
        "Enter 4 to buy #200 for 1GB/3-days\n"
    )
    if Insta == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Instagram Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 250MB for 1 day has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif Insta == "2":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Instagram Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 350MB has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif Insta == "3":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Instagram Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 1GB has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif Insta == "4":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Instagram Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 1GB for 3-days has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        Instagram()


# FACEBOOK
def FaceBook():
    FaceB = input(
        "Enter 1 to buy daily @ #25 for 25mb\n"
        "Enter 2 to buy weekly @ #50 for 50mb\n"
        "Enter 3 to buy monthly @ #150 for 150mb\n"
      )
    if FaceB == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your FaceBook Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 25MB for daily has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif FaceB == "2":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Facebook Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 50MB for weekly has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()

    elif FaceB == "3":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Facebook Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 150MB for monthly has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        FaceBook()

# WHATSAPP
def WhatsApp():
    watsup = input(
        "Enter 1 for daily @ #25 for 25mb\n"
        "Enter 2 for weekly @ #50 for 50mb\n"
        "Enter 3 for monthly @ #150 for 150mb\n"
       )
    if watsup == "1":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Whatsapp Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 25MB for daily has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    elif watsup == "2":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Whatsapp Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 50MB for weekly has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()

    elif watsup == "3":
        calm = input(
            "1. Auto-Renew\n"
            "2. One-off Purchase\n"
            "4. Redeem promo code\n"
            "Select an option: "
        )
        if calm == "1":
            print("Your Whatsapp Plan will be auto renewed upon expiration")
        elif calm == "2":
            print("Activation of 150MB for monthly has been successful")
        elif calm == "4":
            print("Promo code has been redeemed")
        else:
            print(
                "Invalid Entry\n"
                "Try Again!!!"
            )
            socialBundles()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        WhatsApp()


# SOCIAL BUNDLES
def socialBundles():
    socials = input(
        "Enter 1 for WhatsApp\n"
        "Enter 2 for FaceBook\n"
        "Enter 3 for Instagram\n"
        "Enter 4 for Tiktok\n"
        "Enter 5 for Ayoba\n"
        "Enter 6 for All Social Bundles\n"
        "Enter 7 for YouTube, Instagram, and TikTok\n"
        "Enter 8 for Opera Mini $ News\n"
        "Enter 9 for Social Mega Bundles\n"
    )
    if socials == "1":
        print("Select WhatsApp plans: ")
        WhatsApp()
    elif socials == "2":
        print("select FaceBook Plans: ")
        FaceBook()
    elif socials == "3":
        print("Select Instagram Plans: ")
        Instagram()
    elif socials == "4":
        print("Select TikTok Plans: ")
        Tiktok()
    elif socials == "5":
        print("Select Ayoba Plans: ")
        Ayoba()
    elif socials == "6":
        print("Select All Socials Plans: ")
        socialApp()
    elif socials == "7":
        print("Select YouTube, Instagram, and TikTok Plans: ")
        YIT()
    elif socials == "8":
        print("Select Opera Mini $ News Plans: ")
        OperaMini()
    elif socials == "9":
        print("Select Socials Mega Plans: ")
        SMB()
    else:
        print(
            "Invalid Code\n"
            "Try Again\n"
        )
        socialBundles()


# XtraData+ 5000
def xtradataplusfifty():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 0 to Go Back\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N4500 Talk,13GB Data,uduX,Callefeel & Sony one and Gameworld has been successful")
    elif twen == "0":
        xtradataplus()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradataplusfifty()

# XtraData+ 2000
def xtradataplustwenty():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 0 to Go Back\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N1700 Talk,3.5GB Data,uduX,Callefeel & Sony one and Gameworld has been successful")
    elif twen == "0":
        xtradataplus()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradataplustwenty()

# XtraData+ 1000
def xtradataplusten():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 0 to Go Back\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N900 Talk,1303MB Data,Audiomack,Callefeel & Sony one and Gameworld has been successful")
    elif twen == "0":
        xtradataplus()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradataplusten()

# XtraData+ 500
def xtradataplusfive():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 0 to Go Back\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N425 Talk,600MB Data,Audiomack,Callefeel & Sony one and Gameworld has been successful")
    elif twen == "0":
        xtradataplus()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradataplusfive()

# XtraData+ 300
def xtradataplusthree():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 0 to Go Back\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N250 Talk,250MB Data,Audiomack,Callefeel & Sony one and Gameworld has been successful")
    elif twen == "0":
        xtradataplus()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradataplusthree()

# XtraData+
def xtradataplus():
    data = input(
        "Enter 1 to XtraData+ 300\n"
        "Enter 2 to XtraData+ 500\n"
        "Enter 3 to XtraData+ 1000\n"
        "Enter 4 to XtraData+ 2000\n"
        "Enter 5 to XtraData+ 5000\n"
        "Select an option: "
    )
    if data == "1":
        xtradataplusthree()
    elif data == "2":
        xtradataplusfive()
    elif data == "3":
        xtradataplusten()
    elif data == "4":
        xtradataplustwenty()
    elif data == "5":
        xtradataplusfifty()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradataplus()


# XtraData 15000
def xtradatafifteen():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N15000 talk time + 50GB for N5000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradatafifteen()

# XtraData 10000
def xtradatahundred():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N10000 talk time + 30GB for N5000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradatahundred()

# XtraData 5000
def xtradatafifty():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N5000 talk time + 15GB for N5000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradatafifty()

# XtraData 2000
def xtradatatwenty():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N2000 talk time + 4.5GB for N2000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradatatwenty()

# XtraData 1000
def xtradataten():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N1000 talk time + 1.5GB for N500 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradataten()

# XtraData 500
def xtradatafive():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N500 talk time + 750MB for N500 for 14 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradatafive()

# XtraData 300
def xtradatathree():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N300 talk time + 350MB for N300 for 7 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradatathree()

# XtraData 200
def xtradatatwo():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N200 talk time + 200MB for N200 for 3 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtradatatwo()


# XtraData
def xtradata():
    data = input(
        "Enter 1 to XtraData 200\n"
        "Enter 2 to XtraData 300\n"
        "Enter 3 to XtraData 500\n"
        "Enter 4 to XtraData 1000\n"
        "Enter 5 to XtraData 2000\n"
        "Enter 6 to XtraData 5000\n"
        "Enter 7 to XtraData 10000\n"
        "Enter 8 to XtraData 15000\n"
        "Select an option: "
    )
    if data == "1":
        xtradatatwo()
    elif data == "2":
        xtradatathree()
    elif data == "3":
        xtradatafive()
    elif data == "4":
        xtradataten()
    elif data == "5":
        xtradatatwenty()
    elif data == "6":
        xtradatafifty()
    elif data == "7":
        xtradatahundred()
    elif data == "8":
        xtradatafifteen()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )

# XtraTalk 15000
def xtratalkfifteen():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N75000 talk time + 3.5GB for N75000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalkfifteen()

# XtraTalk 10000
def xtratalkhundred():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N50000 talk time + 2.5GB for N10000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalkhundred()

# XtaTalk 5000
def xtratalkfifty():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N25000 talk time + 1.5GB for N5000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalkfifty()

# XtraTalk 2000
def xtratalktwenty():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N10000 talk time + 650MB for N2000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalktwenty()

# XtraTalk 1000
def xtratalkten():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N5000 talk time + 500MB for N1000 for 30 days has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalkten()

# XtraTalk 500
def xtratalkfive():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N2500 talk time + 100MB for N500 has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalkfive()

# XtraTalk 300
def xtratalkthree():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N1500 talk time + 50MB for N300 has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalkthree()

# XtraTalk 200
def xtratalktwo():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your XtraValue Plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of N1000 talk time + 20MB for N200 has been successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalktwo()


# XtraTalk
def xtratalk():
    tal = input(
        "Enter 1 to XtraTalk 200\n"
        "Enter 2 to XtraTalk 300\n"
        "Enter 3 to XtraTalk 500\n"
        "Enter 4 to XtraTalk 1000\n"
        "Enter 5 to XtraTalk 2000\n"
        "Enter 6 to XtaTalk 5000\n"
        "Enter 7 to XtraTalk 10000\n"
        "Enter 8 to XtraTalk 15000\n"
        "Select an option: "
    )
    if tal == "1":
        xtratalktwo()
    elif tal == "2":
        xtratalkthree()
    elif tal == "3":
        xtratalkfive()
    elif tal == "4":
        xtratalkten()
    elif tal == "5":
        xtratalktwenty()
    elif tal == "6":
        xtratalkfifty()
    elif tal == "7":
        xtratalkhundred()
    elif tal == "8":
        xtratalkfifteen()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtratalk()

# Xtravalue
def xtraValue():
    val = input(
        "Enter 1 to XtraTalk\n"
        "Enter 2 to XtraData\n"
        "Enter 3 to Eligible International Destinations\n"
        "Enter 4 to XtraData+\n"
    )
    if val == "1":
        xtratalk()
    elif val == "2":
        xtradata()
    elif val == "3":
        print("Canada", "China", "Denmark", "Germany", "India", "Ireland",
              "Malaysia", "Romania", "South Korea", "United Kingdom", "United States", "Singapore")
    elif val == "4":
        xtradataplus()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        xtraValue()

# 20,000 for 100GB
def twenhunz():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of 100GB was successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twenhunz()

# 30,000 for 200GB
def thirty():
    thirst = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if thirst == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif thirst == "2":
        print("Activation of 200GB was successful")
    elif thirst == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        thirty()

# 20,000 for 120GB
def twenty():
    twelveZ = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twelveZ == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif twelveZ == "2":
        print("Activation of 120GB was successful")
    elif twelveZ == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twenty()

# 15,000 for 75GB
def fifteen():
    fiveZ = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if fiveZ == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif fiveZ == "2":
        print("Activation of 75GB was successful")
    elif fiveZ == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        fifteen()

# 10,000 for 40GB
def fourTen():
    fourZ = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if fourZ == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif fourZ == "2":
        print("Activation of 40GB was successful")
    elif fourZ == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        fourTen()

# 6,000 for 25GB
def twoSix():
    zeroSix = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if zeroSix == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif zeroSix == "2":
        print("Activation of 25GB was successful")
    elif zeroSix == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twoSix()

# 5,000 for 20GB
def fiveTwo():
    zeroFive = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if zeroFive == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif zeroFive == "2":
        print("Activation of 20GB was successful")
    elif zeroFive == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        fiveTwo()

# 2,000- 4.5GB+#2,000 Talktime. Val/30days
def twoThousand():
    pointFour = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if pointFour == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif pointFour == "2":
        print("Activation of 4.5GB+#2,000 Talktime was successful")
    elif pointFour == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twoThousand()

# 1,000- 1.5GB+#1,000 Talktime. Valid 30days
def thousand():
    pointFive = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if pointFive == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif pointFive == "2":
        print("Activation of 1.5GB+#1,000 Talktime was successful")
    elif pointFive == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        thousand()

# 500- 750MB+#500 Talktime. Val/14days
def valTime():
    fiveSeven = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if fiveSeven == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif fiveSeven == "2":
        print("Activation of 750MB+#500 Talktime was successful")
    elif fiveSeven == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        valTime()

# 6,000 for 45GB/30Days
def sixtyFive():
    fourFive = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if fourFive == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif fourFive == "2":
        print("Activation of 45GB was successful")
    elif fourFive == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        sixtyFive()

# 3,000 for 15GB/30Days
def thrays():
    fifteen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if fifteen == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif fifteen == "2":
        print("Activation of 15GB was successful")
    elif fifteen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        thrays()

# 120 for 450MB/7Days
def fourTwo():
    sevo = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if sevo == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif sevo == "2":
        print("Activation of 450MB was successful")
    elif sevo == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        fourTwo()

# 60 for 200MB/24Hrs
def sixByte():
    hours = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if hours == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif hours == "2":
        print("Activation of 200MB was successful")
    elif hours == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        sixByte()

# 75,000 for 600GB/90Days
def sevFive():
    ninety = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if ninety == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif ninety == "2":
        print("Activation of 600GB was successful")
    elif ninety == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        sevFive()

# 50,000 for 400GB/90Days
def finity():
    fort = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if fort == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif fort == "2":
        print("Activation of 400GB was successful")
    elif fort == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        finity()

# 30,000 for 160GB/60Days
def thirtero():
    thirt = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if thirt == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif thirt == "2":
        print("Activation of 160GB was successful")
    elif thirt == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        thirtero()

# 20,000 for 100GB/60Days
def twenhun():
    twen = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twen == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif twen == "2":
        print("Activation of 100GB was successful")
    elif twen == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twenhun()

# 8,000 for 30GB/6ODays
def eighZero():
    eight = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if eight == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif eight == "2":
        print("Activation of 30GB was successful")
    elif eight == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        eighZero()

# 6,000 for 25GB
def sixFive():
    twilight = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twilight == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif twilight == "2":
        print("Activation of 25GB was successful")
    elif twilight == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        sixFive()

# 5,000 for 20GB
def fiftwen():
    ifrit = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if ifrit == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif ifrit == "2":
        print("Activation of 20GB was successful")
    elif ifrit == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        fiftwen()


# 3,500 for 12GB
def threeTwelve():
    thrive = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if thrive == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif thrive == "2":
        print("Activation of 12GB was successful")
    elif thrive == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        threeTwelve()

# 2,500 for 6GB
def twoix():
    twix = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twix == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif twix == "2":
        print("Activation of 6GB was successful")
    elif twix == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twoix()

# 2,000 for 4.5GB
def twoFour():
    fofive = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if fofive == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif fofive == "2":
        print("Activation of 4.5GB was successful")
    elif fofive == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twoFour()

# 1,500 for 3GB
def oneFive():
    threeGig = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if threeGig == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif threeGig == "2":
        print("Activation of 3GB was successful")
    elif threeGig == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        oneFive()

# 1,200 for 2GB
def oneTwo():
    twoGig = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if twoGig == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif twoGig == "2":
        print("Activation of 2GB was successful")
    elif twoGig == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        oneTwo()

# 1,000 for 1.5GB
def oneThousand():
    onePoint = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if onePoint == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif onePoint == "2":
        print("Activation of 1.5GB was successful")
    elif onePoint == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        oneThousand()

# 500 for 750MB+#500 Talktime(Val/14days)
def seventyTime():
    talk = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if talk == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif talk == "2":
        print("Activation of 750MB + #500 talktime was successful")
    elif talk == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        seventyTime()

# 500 for 750MB(2-Week plan)
def sevenhun():
    tweek = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if tweek == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif tweek == "2":
        print("Activation of 40MB was successful")
    elif tweek == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        sevenhun()

# 300 for 350MB
def zero():
    threeZero = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if threeZero == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif threeZero == "2":
        print("Activation of 350MB was successful")
    elif threeZero == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        zero()

# 200 for 1GB(IG/TIKTOK/YOUTUBE ONLY)
def twoTok():
    gily = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if gily == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif gily == "2":
        print("Activation of 1GB was successful")
    elif gily == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twoTok()

# 500 for 2GB
def fivehundred():
    ive = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if ive == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif ive == "2":
        print("Activation of 2GB was successful")
    elif ive == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        fivehundred()

# 300 for 1GB
def threehundred():
    reed = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if reed == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif reed == "2":
        print("Activation of 1GB was successful")
    elif reed == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        threehundred()

# 200 for 200MB
def twohundred():
    hund = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if hund == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif hund == "2":
        print("Activation of 200MB was successful")
    elif hund == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        twohundred()

# 100 for 350MB
def hund():
    byte = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if byte == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif byte == "2":
        print("Activation of 350MB was successful")
    elif byte == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        hund()

# 100 for 100MB
def hundred():
    mega = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if mega == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif mega == "2":
        print("Activation of 100MB was successful")
    elif mega == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        hundred()
# 50 for 40MB
def fifty():
    forty = input(
        "Enter 1 to Auto-Renew\n"
        "Enter 2 to One-off\n"
        "Enter 4 to Redeem Promo Code\n"
    )
    if forty == "1":
        print("Your data plan will be auto renewed upon expiration")
    elif forty == "2":
        print("Activation of 40MB was successful")
    elif forty == "4":
        print("Promo code has been redeemed")
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        fifty()

# 5G Plans
def gPlans():
    fiveg = input(
        "Enter 1 to #5,000 for 20GB\n"
        "Enter 2 to #6,000 for 25GB\n"
        "Enter 3 to #10,000 for 40GB\n"
        "Enter 4 to #15,000 for 75GB\n"
        "Enter 5 to #20,000 for 120GB\n"
        "Enter 6 to #30,000 for 200GB\n"
        "Enter 7 to #20,000 for 100GB\n"
    )
    if fiveg == "1":
        print("Select an option:")
        fiveTwo()
    elif fiveg == "2":
        print("Select an option:")
        twoix()
    elif fiveg == "3":
        print("Select an option:")
        fourTen()
    elif fiveg == "4":
        print("Select an option:")
        fifteen()
    elif fiveg == "5":
        print("Select an option:")
        twenty()
    elif fiveg == "6":
        print("Select an option:")
        thirty()
    elif fiveg == "7":
        print("Select an option:")
        twenhunz()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )

# Hot Deals
def hotDeals():
    hot = input(
        "Enter 1 to #500- 750MB+#500 Talktime. Val/14days\n"
        "Enter 2 to #1,000- 1.5GB+#1,000 Talktime. Valid 30days\n"
        "Enter 3 to #2,000- 4.5GB+#2,000 Talktime. Val/30days\n"
    )
    if hot == "1":
        print("Select an option:")
        valTime()
    elif hot == "2":
        print("Select an option:")
        thousand()
    elif hot == "3":
        print("Select an option:")
        twoThousand()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        hotDeals()

# Family Packs
def familyPacks():
    fam = input(
        "Enter 1 to Buy Family Pack\n"
        "Enter 2 to Add New Beneficiary/Sponsor\n"
        "Enter 3 to Manage Beneficiary/Sponsor\n"
        "Enter 4 to Balance enquiry\n"
        "Enter 5 to Deactivate service\n"
        "Enter 6 to Help\n"
    )

# Broadband Plans
def broadPlans():
    band = input(
        "Enter 1 to Link Device\n"
        "Enter 2 to Recharge Device\n"
        "Enter 3 to Buy Data Bundle on Device\n"
        "Enter 4 to Check Device Balance\n"
        "Enter 5 to View & Unlink Device\n"
    )

# Always ON plans
def always():
    onPlans = input(
        "Enter 1 to #60 for 200MB/24Hrs\n"
        "Enter 2 to #120 for 450MB/7Days\n"
        "Enter 3 to #3,000 for 15GB/30Days\n"
        "Enter 4 to #6,000 for 45GB/30Days\n"
    )
    if onPlans == "1":
        print("Select an option:")
        sixByte()
    elif onPlans == "2":
        print("Select an option:")
        fourTwo()
    elif onPlans == "3":
        print("Select an option:")
        thrays()
    elif onPlans == "4":
        print("Select an option:")
        sixtyFive()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        always()

# 2-3 Monthly
def threeMon():
    twoMon = input(
        "Enter 1 to #8,000 for 30GB/6ODays\n"
        "Enter 2 to #20,000 for 100GB/60Days\n"
        "Enter 3 to #30,000 for 160GB/60Days\n"
        "Enter 4 to #50,000 for 400GB/90Days\n"
        "Enter 5 to #75,000 for 600GB/90Days\n"
    )
    if twoMon == "1":
        print("Select an option")
        eighZero()
    elif twoMon == "2":
        print("Select an option:")
        twenhun()
    elif twoMon == "3":
        print("Select an option")
        thirtero()
    elif twoMon == "4":
        print("Select an option:")
        finity()
    elif twoMon == "5":
        print("Select an option:")
        sevFive()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        threeMon()

# Monthly
def monthly():
    month = input(
        "Enter 1 to #1,000 for 1.5GB\n"
        "Enter 2 to #1,200 for 2GB\n"
        "Enter 3 to #1,500 for 3GB\n"
        "Enter 4 to #2,000 for 4.5GB\n"
        "Enter 5 to #2,500 for 6GB\n"
        "Enter 6 to #3,500 for 12GB\n"
        "Enter 7 to #5,000 for 20GB\n"
        "Enter 8 to #6,000 for 25GB\n"
    )
    if month == "1":
        print("Select an option:")
        oneThousand()
    elif month == "2":
        print("Select an option:")
        oneTwo()
    elif month == "3":
        print("Select an option:")
        oneFive()
    elif month == "4":
        print("Select an option:")
        twoFour()
    elif month == "5":
        print("Select an option:")
        twoSix()
    elif month == "6":
        print("Select an option:")
        threeTwelve()
    elif month == "7":
        print("Select an option:")
        fiftwen()
    elif month == "8":
        print("Select an option:")
        sixFive()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        monthly()

# Weekly
def weekly():
    we = input(
        "Enter 1 to #200 for 1GB(IG/TIKTOK/YOUTUBE ONLY)\n"
        "Enter 2 to #300 for 350MB\n"
        "Enter 3 to #500 for 750MB(2-Week plan)\n"
        "Enter 4 to #500 for 750MB+#500 Talktime(Val/14days)\n"
    )
    if we == "1":
        print("Select an option:")
        twoTok()
    elif we == "2":
        print("Select an option:")
        zero()
    elif we == "3":
        print("Select an option:")
        sevenhun()
    elif we == "4":
        print("Select an option:")
        seventyTime()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        weekly()

# Daily
def daily():
    day = input(
       "Enter 1 to #50 for 40MB\n"
       "Enter 2 to #100 for 100MB\n"
       "Enter 3 to #100 for 350MB(IG/TIKTOK/YOUTUBE)\n"
       "Enter 4 to #200 for 200MB\n"
       "Enter 5 to #300 for 1GB\n"
       "Enter 6 to #500 for 2GB\n"
    )
    if day == "1":
        print("Select an option:")
        fifty()
    elif day == "2":
        print("Select an option:")
        hundred()
    elif day == "3":
        print("Select an option:")
        hund()
    elif day == "4":
        print("Select an option:")
        twohundred()
    elif day == "5":
        print("Select an option:")
        threehundred()
    elif day == "6":
        print("Select an option:")
        fivehundred()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        daily()

# Data plans
def dataPlans():
    data = input(
        "Enter 1 to Daily\n"
        "Enter 2 to Weekly\n"
        "Enter 3 to Monthly\n"
        "Enter 4 to 2-3 Monthly\n"
        "Enter 5 to Always ON Plans\n"
        "Enter 6 to Broadband Plans\n"
        "Enter 7 to Family Packs\n"
        "Enter 8 to Hot Deals\n"
        "Enter 9 to 5G plans\n"
    )
    if data == "1" :
        print("Select data plan:")
        daily()
    elif data == "2" :
        print("Select data plan:")
        weekly()
    elif data == "3" :
        print("Select data plan:")
        monthly()
    elif data == "4" :
        print("Select data plan:")
        threeMon()
    elif data == "5":
        print("Select data plan:")
        always()
    elif data == "6":
        print("Select data plan:")
        broadPlans()
    elif data == "7":
        print("Select data plan:")
        familyPacks()
    elif data == "8":
        print("Select data plan:")
        hotDeals()
    elif data == "9":
        print("Select data plan:")
        gPlans()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        dataPlans()

# Select Transaction
def selectTrans():
    trans = input(
        "Enter 1 to Data Plans\n"
        "Enter 2 to XtraValue\n"
        "Enter 3 to Social Bundles\n"
        "Enter 4 to Balance Check\n"
        "Enter 5 to Roaming\n"
        "Enter 6 to Borrow Credit/Recharge\n"
        "Enter 7 to Gift Data\n"
        "Enter 8 to Video Packs\n"
        "Enter 9 to Hot Deals\n"
        "Select an option: "
    )
    if trans == "1":
        print("Buy Data plan")
        dataPlans()
    elif trans == "2":
        print("Buy XtraValue")
        xtraValue()
    elif trans == "3":
        print("Buy Social Bundles")
        socialBundles()
    elif trans == "4":
        print("Check Balance")
        Balance()
    elif trans == "5":
        print("Roaming")
        Roaming()
    elif trans == "6":
        print("Borrow Credit or Recharge")
        borrowCredit()
    elif trans == "7":
        print("Gift Data")
        giftData()
    elif trans == "8":
        print("Video packs")
        videopacks()
    elif trans == "9":
        print("Hot Deals")
        hotDeals()
    else:
        print(
            "Invalid Entry\n"
            "Try Again!!!"
        )
        selectTrans()

# USSD Code for MTN
def mtnUSSD():
    ussd = input("Enter Code: ")
    if ussd == "*131#":
        selectTrans()
    else:
        print(
            "Invalid Code\n"
            "Try Again!!!"
        )
        mtnUSSD()
mtnUSSD()
