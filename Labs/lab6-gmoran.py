#Coin Flip Program - Lab 6
#Guillermo Moran

import random

def main():
    
    flipCount = 1
    totalFlips = 100
    headsCount = 0
    tailsCount = 0
    
    while (flipCount <= totalFlips):
        coinFace = random.randint(1,2)
        print("Iteration Number:",flipCount)
        
        if (coinFace == 1):
            print("Heads")
            headsCount += 1
        else:
            print("Tails")
            tailsCount += 1
            
        flipCount += 1
    
    print("Total Heads:", headsCount)
    print("Total Tails:", tailsCount)
    
main()