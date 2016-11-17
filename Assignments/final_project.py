######################################################
# Final Project - Login Python Script
# By Nicolas and Guillermo
######################################################

SAVE_FILE_NAME = "login_data"

import shelve

def main():
    showUserMenu()
    
######################################################
# loginUser()
# Allows the user to login
######################################################

def loginUser():
    
    print("""  _                 _       
 | |               (_)      
 | |     ___   __ _ _ _ __  
 | |    / _ \ / _` | | '_ \ 
 | |___| (_) | (_| | | | | |
 |______\___/ \__, |_|_| |_|
               __/ |        
              |___/         \n""")
    
    
    save_file = openSaveFile()
    
    #check if user exists
    
    username = input("Enter your username: ")
  
    try:
        save_file[username]
    except KeyError:
        print("Username does not exist. Please create a new account.")
        showUserMenu()
        return

    
    attempts = 0
    loginAttempt = False
    while (loginAttempt == False and attempts < 5):
        
        password = input("Enter your password: ")
        
        if (password == save_file[username]):
            
            print("\nLog in successful!")
            loginAttempt = True

        else:
            print("\nLog in unsuccessful, please try again.")
            attempts += 1
        
    if (attempts == 5):
        print("\nLogin attempts exceeded. Returning to the main menu.")

    save_file.close()
    showUserMenu()
            
######################################################
# createNewUser()
# Create a new user and password combination
# Check if the username is already in the database
# Check if usernames and passwords are valid 
# If valid, write to the database
######################################################
    
def createNewUser():
    
    print("""  _   _                 _    _               
 | \ | |               | |  | |              
 |  \| | _____      __ | |  | |___  ___ _ __ 
 | . ` |/ _ \ \ /\ / / | |  | / __|/ _ \ '__|
 | |\  |  __/\ V  V /  | |__| \__ \  __/ |   
 |_| \_|\___| \_/\_/    \____/|___/\___|_|   \n""")
    
    print("Type \"exit\" to return to the user menu")
    
    save_file = openSaveFile() #Open the save file and store it on a variable
    
    newUser = "" #Start with an empty username to initiate the while loop
    while (isUsernameValid(newUser) == False):
        newUser = input("Enter your new username: ")
        
        if (newUser.lower() == "exit"):
            showUserMenu()
            return
    
        
    #Check if username exists
    
    try:
        save_file[newUser]
    except KeyError:
        print("\nNo user file found! Creating...")
        accountExists = False
    else:
        print("\nUser already exists!\n")
        accountExists = True
        
    #Proceed to enter password for new account IF account doesn't exist
        
    if (accountExists == False):
        newPassword = "" #Start with an empty password to initiate the while loop
        
        while (isPasswordValid(newPassword) == False):
            newPassword = input("Enter your new password: ")
            
        save_file[newUser] = newPassword
        print("Created new account for:", newUser)
    
    save_file.close()
    showUserMenu()
    
######################################################
# isUsernameValid(username)
# isPasswordValid(password)
#####################################################
# Check if the username is a valid .edu email
# Check if the password is 6-10 characters long and 1 digit
######################################################    

def isUsernameValid(username):
    
    if (("@" in username) and (".edu" in username)):
        return True
    else:
        print("\nYour username must be a valid .edu email")
        return False
    
def isPasswordValid(password):
     
    containsDigit = any(letter.isdigit() for letter in password) #Check if string contains a number 
    passwordLength = len(password)
     
    if ((passwordLength >= 6 and passwordLength <= 10) and containsDigit):
        return True
    else:
        print("\nPasswords require a length between 6 and 10 digits and at least 1 number.")
        return False
    
######################################################
# openSaveFile()
# Open and return the save file
# Avoid opening the file over
# and doing exception handling again
######################################################

def openSaveFile(): 
    
    try:
        save_file = shelve.open(SAVE_FILE_NAME, "c") #We shouldn't have issues. This automatically creates the save file
    except IOError as e:
        print("An error occured while opening the database file.")
        print(e) 
           
    return save_file
    
######################################################
# showUserMenu()
# Displays the user menu
# Mainly written so I won't have to write this code 
# again and I can just modify it for future labs ;)
# But also because it makes my code look nicer
######################################################
    
def showUserMenu():
    
    print("""  __  __       _         __  __                  
 |  \/  |     (_)       |  \/  |                 
 | \  / | __ _ _ _ __   | \  / | ___ _ __  _   _ 
 | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |
 | |  | | (_| | | | | | | |  | |  __/ | | | |_| |
 |_|  |_|\__,_|_|_| |_| |_|  |_|\___|_| |_|\__,_|\n""")
    
    userSelection = 0 #Nothing is selected
    
    while ((userSelection > 3) or (userSelection < 1)):
        
        print("1) New User \n2) Log In \n3) Exit \n")
        
        try:
            userSelection = int(input("Please enter your selection: "))
        except ValueError:
            print("\nPlease make a selection from the following choices:")
            
        if (userSelection > 3):
            print("\nPlease make a selection from the following choices:")
            
    if (userSelection == 1):
        createNewUser()
    if (userSelection == 2):
        loginUser()
    if (userSelection == 3):
        print("Goodbye.")
  
main()



######################################################
# Pseudocode for creating a new account
#
# Display the user menu: New User, Log In, Exit
#
#
# User is prompted to enter a new username.
# Check username for correct format, ask again if incorrect.
# Check if username already exists, show menu if it does.
# User is prompted to enter a new password.
# Check if password is in the correct format.
# If password is correct, write the new user/pass to a shelve db
# return to the main menu
######################################################

######################################################
# Login User pseudo code
#
# Open the shelve file. Prompts the user to enter their username.
# Then, the function checks to see if the user exists; if the user
# does not exist, it raises an error message and prompts the user 
# to create a new account. If the user does exist, it will then 
# prompt the user to enter their password. If the password matches 
# the password in the file for that specific username, then the login 
# will be successful; if the password does not match then the user 
# will need to re-enter their password. If the number of attempts 
# to login reaches 5, the user will be redirected to the main menu 
# and will have to start again.
######################################################