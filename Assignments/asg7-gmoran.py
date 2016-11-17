#Assignment 7
#Guillermo Moran

USER_INPUT_MIN = 1
USER_INPUT_MAX = 20

def main() :
      
    answer = 0
 
    while (answer < USER_INPUT_MIN or answer > USER_INPUT_MAX) :

        errorOccurred = True #Expect an error the first time to run the error checking loop

        while (errorOccurred == True) :

            try:
                answer = int(input("Enter number: "))
            except:
                print("Please enter a number greater than or equal to %d and less than %d" % (USER_INPUT_MIN, USER_INPUT_MAX))
            else:
                #No error occured, stop the while loop
                errorOccurred = False        

        if (answer <  USER_INPUT_MIN or answer > USER_INPUT_MAX) :
        
            print("Please enter a number greater than or equal to %d and less than %d" % (USER_INPUT_MIN, USER_INPUT_MAX))

    print("Got it: ", answer)
	
main()
