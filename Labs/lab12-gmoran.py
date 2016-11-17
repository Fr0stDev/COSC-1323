##########
# Guillermo Moran
# Lab 12 - Bryan
##########

import pickle
import sys

FACTOR_VARIABLE = 1024
FILE_PATH = "factors.dat"

def main():
    factors = calculateFactors(FACTOR_VARIABLE)
    print("Initial Factors:", factors)
    
    #Save factors in binary FILE_PATH
    
    try:
        save_file = open(FILE_PATH, "wb")
    except IOError as e:
        print(e)
        sys.exit()
        
    pickle.dump(factors,save_file)
    save_file.close()
        
    # Unpickle FILE_PATH and print factors in reverse order
    
    try:
        open_file = open(FILE_PATH, "rb")
    except IOError as e:
        print(e)
        sys.exit()
        
    #load factors from binary file
    reversedFactors = pickle.load(open_file)
    reversedFactors.reverse() # reverse factors
    
    print("Reverse factors from binary file:", reversedFactors)
    open_file.close()
    

def calculateFactors(number):
    factors = []
    for i in range (1, number + 1):
        if (number % i == 0):
            factors.append(i)
            
    #print(factors)
    return factors

main()