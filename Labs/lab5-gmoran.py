# Guillermo Moran
# Calculator - Lab 5 
# 9-22-15

def main():
    
    firstNumber = int(input("Please enter the first number: "))
    secondNumber = int(input("Please enter the second number: "))
    
    print("Please enter the number that corresponds to the desired operator\n 1) +\n 2) -\n 3) *\n 4) /\n 5) %")
    selectedOperator = int(input("Your selection: "))
    
    #There's only 5 options. Anything more than 5 is invalid.
    if (selectedOperator > 5):
        print("Invalid Selection")
    else:
        result = doMath(firstNumber, secondNumber, selectedOperator)
        print("The answer is:", result)
        
        
def doMath(firstNumber, secondNumber, selectedOperator):
    
    if (selectedOperator == 1):
        result = firstNumber + secondNumber
    elif (selectedOperator == 2):
        result = firstNumber - secondNumber
    elif (selectedOperator == 3):
        result = firstNumber * secondNumber
    elif (selectedOperator == 4):
        result = firstNumber / secondNumber
    elif (selectedOperator == 5):
        result = firstNumber % secondNumber
        
    return result
    
main()
    
    
