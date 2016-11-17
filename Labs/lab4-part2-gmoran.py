#Adding Calculator (lab 4 part 2)
#Guillermo Moran

def myAdd(num1, num2):
    return num1 + num2

def main():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    result = myAdd(num1, num2)

    print("The sum of the two numbers entered is:", result)

main()
