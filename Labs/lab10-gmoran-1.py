# __          ___      .______       __    ___   
#|  |        /   \     |   _  \     /_ |  / _ \  
#|  |       /  ^  \    |  |_)  |     | | | | | | 
#|  |      /  /_\  \   |   _  <      | | | | | | 
#|  `----./  _____  \  |  |_)  |     | | | |_| | 
#|_______/__/     \__\ |______/      |_|  \___/  

#  _______ .___  ___.   ______   .______          ___      .__   __. 
# /  _____||   \/   |  /  __  \  |   _  \        /   \     |  \ |  | 
#|  |  __  |  \  /  | |  |  |  | |  |_)  |      /  ^  \    |   \|  | 
#|  | |_ | |  |\/|  | |  |  |  | |      /      /  /_\  \   |  . `  | 
#|  |__| | |  |  |  | |  `--'  | |  |\  \----./  _____  \  |  |\   | 
# \______| |__|  |__|  \______/  | _| `._____/__/     \__\ |__| \__| 
                                                

def main():
    
    print("GMoran's Caesar Cipher Program! Please select an option to begin!")
    
    errorOccurred = True #Expect an error
    userSelection = 0 #Nothing selected yet
    programIsAllowedToExit = False #User is trapped until they select option 3!
    
    while (programIsAllowedToExit == False):
        while (errorOccurred or (userSelection < 1 or userSelection > 3)):
            
            try:
                print(" 1) Encrypt \n 2) Decrypt \n 3) Exit")
                userSelection = int(input("Please enter your selection: "))
                
            except ValueError:
                print("Please enter a choice between 1 and 3")
                
            else:
               errorOccurred = False
            
        if (userSelection == 1):
            textToEncrypt = input("Enter text to encrypt: ")
            textToEncrypt = textToEncrypt.lower() #We only take lowercase
            print("Encrypted Text:", encryptText(textToEncrypt), "\n")
            userSelection = 0 #Reset the user input 
        
        if (userSelection == 2):
            textToDecrypt = input("Enter text to decrypt: ")
            textToDecrypt = textToDecrypt.lower()
            print("Decrypted Text:",decryptText(textToDecrypt))
            userSelection = 0
        
        if (userSelection == 3):
            programIsAllowedToExit = True
            exit()
   
            

#---------------------------------------------------------------
# encryptText()
# Encrypts text passed an an argument
#---------------------------------------------------------------

def encryptText(textToEncode):
    
    encodeDict = createEncode()
    encodedText = ""
    
    for letter in textToEncode :
        encodedText += encodeDict[letter]
        
    #print("Encoded Text:", encodedText)
    return encodedText

#---------------------------------------------------------------
# decryptText()
# Decrypts text passed an an argument
#---------------------------------------------------------------

def decryptText(textToDecode):
    
    decodeDict = createDecode()
    decodedText = ""
    
    for letter in textToDecode :
        decodedText += decodeDict[letter]
        
    #print("Decoded Text:", decodedText)
    return decodedText
        
#---------------------------------------------------------------
# createDecode()
# Creates a Ceasar cipher decode dictionary and returns the dictionary
#---------------------------------------------------------------
def createDecode() :

    decodeDict = {}

    decodeDict["d"] = "a"
    decodeDict["e"] = "b"
    decodeDict["f"] = "c"
    decodeDict["g"] = "d"
    decodeDict["h"] = "e"
    decodeDict["i"] = "f"
    decodeDict["j"] = "g"
    decodeDict["k"] = "h"
    decodeDict["l"] = "i"
    decodeDict["m"] = "j"
    decodeDict["n"] = "k"
    decodeDict["o"] = "l"
    decodeDict["p"] = "m"
    decodeDict["q"] = "n"
    decodeDict["r"] = "o"
    decodeDict["s"] = "p" 
    decodeDict["t"] = "q"
    decodeDict["u"] = "r"
    decodeDict["v"] = "s"
    decodeDict["w"] = "t"
    decodeDict["x"] = "u"
    decodeDict["y"] = "v"
    decodeDict["z"] = "w"
    decodeDict["a"] = "x"
    decodeDict["b"] = "y"
    decodeDict["c"] = "z"
    decodeDict[" "] = " "

    return decodeDict

#---------------------------------------------------------------
# createEncode()
# Creates a Ceasar cipher encode dictionary and returns the dictionary
#---------------------------------------------------------------
def createEncode():

    encodeDict = {}

    encodeDict["a"] = "d"
    encodeDict["b"] = "e"
    encodeDict["c"] = "f"
    encodeDict["d"] = "g"
    encodeDict["e"] = "h"
    encodeDict["f"] = "i"
    encodeDict["g"] = "j"
    encodeDict["h"] = "k"
    encodeDict["i"] = "l"
    encodeDict["j"] = "m"
    encodeDict["k"] = "n"
    encodeDict["l"] = "o"
    encodeDict["m"] = "p"
    encodeDict["n"] = "q"
    encodeDict["o"] = "r"
    encodeDict["p"] = "s" 
    encodeDict["q"] = "t"
    encodeDict["r"] = "u"
    encodeDict["s"] = "v"
    encodeDict["t"] = "w"
    encodeDict["u"] = "x"
    encodeDict["v"] = "y"
    encodeDict["w"] = "z"
    encodeDict["x"] = "a"
    encodeDict["y"] = "b"
    encodeDict["z"] = "c"
    encodeDict[" "] = " "

    return encodeDict  

main()