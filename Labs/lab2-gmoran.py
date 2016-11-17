
def main() :

         doMathOne()
         doMathTwo()
         doMathThree()
         doMathFour()

# ***********************************************************************
# doMathOne()
# Write a function that stores the value 5 in the variable 'num' and prints 
# the contents of 'num'
# then stores 7 in 'num' and prints the contents of 'num'.
#
# Help: To print the contents of a variabe x: print(x)
# ***********************************************************************
def doMathOne() :
         print("Now in the doMathOne() function")
         num = 5
         print("'num' is now set to:",num)
         num = 7
         print("'num' is now set to:",num)


# ***********************************************************************
# doMathTwo()
# Write a function that adds 5 + 7 and stores the result in the variable 'mySum'
# then prints the contents of the variable 'mySum'
# ***********************************************************************
def doMathTwo() :
         print("Now in the doMathTwo() function")
         mySum = 5+7
         print(mySum)

# ***********************************************************************
# doMathThree()
# Write a function that stores 5 in the variable 'num' and prints 'num'
# then stores num + 7 in the variable 'mySum' and prints the contents of 'mySum'
# 
# Help: To add a number to what is already in variable a: a = a + (Number)
# ***********************************************************************
def doMathThree() :
         print("Now in the doMathThree() function")
         num = 5
         mySum = num +7
         print(mySum)

# *********************************************************************** 
# doMathFour()
# Write a function that prints "13" + "16"
# and then prints 13 + 16 (without quotes)
# Now add 13 + 16 and store the result in a variable named "mySum"
# The program should then print "13 + 16 = 29", in a way that uses
# the contents of mySum.
#
# Help: To print a string that includes double quotes, you can surround
# the string with single quotes.
# ***********************************************************************
def doMathFour() :
         print("Now in the doMathFour() function")
         print("\"13\" + \"16\"")
         print("13 + 16")
         mySum = 13+16
         print("13 + 16 = %d" % mySum)

main()
