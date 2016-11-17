######################################################
# Lab 13
# By Guillermo Moran 
######################################################

NUMBER_TO_CALCULATE = 600851475143

def main():
    
    for i in range(2, NUMBER_TO_CALCULATE):
        if (isPrime(i)):
            if (NUMBER_TO_CALCULATE % i == 0):
                print("Prime Factor Found:", i)
            
    
def isPrime(number):
    
    for i in range (2, number):
        
        if (number % i == 0):
            return False
        
    return True
main()