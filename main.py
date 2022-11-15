from colorama import Fore
import time
# the colorama plug-in allows you to change the color of text in the terminal

# All big indents in code help for formatting in terminal to make it look epic.

# First menu that allows you to go into the password manager.

yes = input(Fore.LIGHTGREEN_EX + """
                -----------------------------
                |  Python Password Manager  |
                |  would you like to begin? |
                |      (y)       (n)        |
                |___________________________|
                        """)

while True:
    if yes == "y" or "Y" or "Yes" or "yes":
        pm_hud = input(Fore.LIGHTMAGENTA_EX + """
                ______________________________
                | What would you like to do? |
                | 1: Create New Password     |
                | 2: Retrieve Passwords      |
                | 3: Set up Security Password| 
                | 4: Exit Password Manager   |        
                |____________________________|
                 """)
    if pm_hud != "1" or "2" or "3" or "4":
        print("Please choose a number between 1 and 4.")
        time.sleep(1)
        yes = "y"

    # Allows you to choose one of the four options in the terminal.

    if pm_hud == "1":
        softwareName = input("Enter the name of the software you are using: ")
        username = input("Enter your username for this software: ")
        password = input("Enter your password for this software: ")

        # file open allows the program to write a .txt and change its properties

        file = open("PasswordEntrees.txt", "a")
        file.write(softwareName + ":|" + username + ":|" + password + "\n")
        file.close()
    # This will create a security key that will allow you to access the passwords you've registered on the
    # password manager.
    # The key permanently saves the security key to a . txt file.

    if pm_hud == "3":
        Security_Key = input(Fore.LIGHTBLUE_EX + "Type in your universal password: ")
        file = open("SecurityKey.txt", "a")
        file.write(Security_Key)
        file.close()

    if pm_hud == "2":
        security_pw = input("Please enter Security Password: ")

        # "r" opens the file in read mode, the rest allows python to compair the password in security key file and what
        # was, written in the terminal and if it is the same it will print the passwords.

        file = open("SecurityKey.txt", "r")
        f = file.readline()
        if security_pw == f:

            # Opens The password entry file in read only.

            file = open("PasswordEntrees.txt", "r")
            print("Software\tUsername\tPassword")
            for i in file:
                data = i.split(":|")
                print(data[0] + "\t\t" + data[1] + "\t\t" + data[2])
                time.sleep(50)
        else:
            print("Sorry, Incorrect Password!")

    # allows you to exit the password manager.

    if pm_hud == "4":
        path = input("Thank you for using Password Manager!")
    continue
    if keepgoing == "n" or "N" or "no" or "No":
        print("Have a nice day.")
