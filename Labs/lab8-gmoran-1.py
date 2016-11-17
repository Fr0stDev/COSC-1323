#Lab 8 - Bryan
#Guillermo Moran

NUMBERS_REQUIRED = 5
NUMBER_LIMIT = 20

def main():
    numberList = []
     #Keeps count of how many times we have prompted the user
    
    while (len(numberList) < NUMBERS_REQUIRED):
        
        userInput = NUMBER_LIMIT + 1 #This always runs the while loop the first time, assuring us that the user is prompted the first time 
        print("This program requires that you enter", NUMBERS_REQUIRED, "different numbers")
        
        while (userInput > NUMBER_LIMIT):
            print("Enter an integer that is less than or equal to", NUMBER_LIMIT, ":")
            userInput = int(input())
        
        numberList.append(userInput)
        
        
    histogram(numberList)
        
def histogram(numberList):
    
    print("Inputed List:", numberList)
    
    for number in numberList:
        print("*" * number)
        
main()