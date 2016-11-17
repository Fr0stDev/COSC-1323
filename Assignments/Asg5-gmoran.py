#Assignment 5
#Guillermo Moran

def main():

    sentence = input("Enter a sentence: ")

    aCount = 0
    eCount = 0
    iCount = 0
    oCount = 0
    uCount = 0

    for letter in sentence:
        if (letter == "a"):
            aCount += 1
        if (letter == "e"):
            eCount += 1
        if (letter == "i"):
            iCount += 1
        if (letter == "o"):
            oCount += 1
        if (letter == "u"):
            uCount += 1

    print("The letter 'a' was found", aCount, "times")
    print("The letter 'e' was found", eCount, "times")
    print("The letter 'i' was found", iCount, "times")
    print("The letter 'o' was found", oCount, "times")
    print("The letter 'u' was found", uCount, "times")

main()
    
        
    
