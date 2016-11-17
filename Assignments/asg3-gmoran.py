#Assignment 3
#Guillermo Moran

def main():
    userInput = int(input("Please enter a number: "))
    
    if userInput % 2 == 0 :
        print("Number entered is even")
    else:
        print("Number entered is odd")

    doTestTwo()
    doTestThree()


def doTestTwo():
    hungry = True
    thirsty = False

    if hungry and thirsty :
        print("You are hungry and thirsty")

    elif hungry and thirsty is False :
        print("You are hungry and not thirsty")
        
    elif hungry is False and thirsty :
        print("You are not hungry, but you are thirsty")
        
    elif hungry is False and thirsty is False :
        print("You are not hungry or thirsty")
    

def doTestThree():
    userInput = int(input("Please enter a number: "))

    if userInput % 2 == 0 and userInput % 3 == 0 :
        print("Number entered it divisible by 2 and 3")
         
    elif userInput % 2 == 0 and not userInput % 3 == 0 :
        print("Number entered it divisible by 2 but not 3")

    elif userInput % 3 == 0 and not userInput % 2 == 0 :
         print("Number entered it divisible by 3 and not 2")
    else :
        print("Number entered is not divisible by 2 or 3")
                     
        


main()
        
                    
