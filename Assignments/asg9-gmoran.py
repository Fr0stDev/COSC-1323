#Assignment 9 - Bryan
#By Guillermo Moran

import sys

def main():
    
    try:
        ahs1 = open("ahs1.txt", "r")
        ahs2 = open("ahs2.txt", "w")
    except IOError as e:
        print("An Error Occurred:")
        print(e)
        sys.exit()
    
    for line in ahs1:
        
        newLine = line.replace("Lady Gaga", "Taylor Swift")
        
        ahs2.write(newLine)
        
        print("Old:", line)
        print("New:", newLine)
            
    ahs1.close()
    ahs2.close()
        
main()