##          ###    ########        ##      ##                 ########  ########  ##    ##    ###    ##    ## 
##         ## ##   ##     ##     ####    ####                 ##     ## ##     ##  ##  ##    ## ##   ###   ## 
##        ##   ##  ##     ##       ##      ##                 ##     ## ##     ##   ####    ##   ##  ####  ## 
##       ##     ## ########        ##      ##      #######    ########  ########     ##    ##     ## ## ## ## 
##       ######### ##     ##       ##      ##                 ##     ## ##   ##      ##    ######### ##  #### 
##       ##     ## ##     ##       ##      ##                 ##     ## ##    ##     ##    ##     ## ##   ### 
######## ##     ## ########      ######  ######               ########  ##     ##    ##    ##     ## ##    ## 



 ######   ##     ##  #######  ########     ###    ##    ##                                                    
##    ##  ###   ### ##     ## ##     ##   ## ##   ###   ##                                                    
##        #### #### ##     ## ##     ##  ##   ##  ####  ##                                                    
##   ###  ## ### ## ##     ## ########  ##     ## ## ## ##                                                    
##    ##  ##     ## ##     ## ##   ##   ######### ##  ####                                                    
##    ##  ##     ## ##     ## ##    ##  ##     ## ##   ###                                                    
 ######   ##     ##  #######  ##     ## ##     ## ##    ##    
 
TODO_LIST_NAME = "ToDoList.txt"
 
def main():
    showUserMenu()

######################################################
# addNewTaskToList()
# Prompts the user to enter a new task to
# appent to a list, and then returns to the main menu
######################################################

def addNewTaskToList():
    
    newTask = input("New task: ")
    
    todoList = open(TODO_LIST_NAME, "a") #No exception handling. This creates a file if it doesn't already exist! 
    todoList.write(newTask + "\n") #Append the task + a new line operator 
    todoList.close()
    
    showUserMenu() #Go back to the user menu
    
######################################################
# printListItems()
# Prints all the items on the list.
# If the list does not exist, it is automatically
# created by the program.
# Returns to main menu at the end of the function
######################################################
    
def printListItems():
    
    try:
        todoList = open(TODO_LIST_NAME, "r")
        
        print("\n======= TO DO LIST =======\n")
        for task in todoList:
            print(task)
        print("\n======= END OF LIST =======\n")
        
    except IOError as error:
        print("To do list file not found")
        print(error)
        print("Creating file...")
        
        #create a new file, then close it
        newFile = open(TODO_LIST_NAME, "w")
        newFile.close() 
        
    showUserMenu() #Go back to the user menu
        
######################################################
# showUserMenu()
# Displays the user menu
# Mainly written so I won't have to write this code 
# again and I can just modify it for future labs ;)
# But also because it makes my code look nicer
######################################################
    
def showUserMenu():
    
    print("Main Menu!\n")
    
    errorOccurred = True #Because we expect an error
    userSelection = 0 #Nothing is selected
    
    while (errorOccurred or (userSelection > 3) or (userSelection < 1)):
        
        print("1) Add an Item \n2) Print List \n3) Exit \n")
        
        try:
            userSelection = int(input("Please enter your selection: "))
        except ValueError:
            print("Please make a selection from the following choices")
        else:
            errorOccured = False
            
        if (userSelection == 1):
            addNewTaskToList()
        if (userSelection == 2):
            printListItems()
        if (userSelection == 3):
            print("Goodbye.")
            exit()
    
main()