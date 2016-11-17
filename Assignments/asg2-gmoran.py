#Assignment 2

def main():
    #String formatting
    
    print("This is:")
    print("\"String 1\"")
    print("And this is:")
    print("\"String 2\"")
    print("") #Line break
    print("When I concatenate these two strings together, I get:")
    print("\"String 1\" + \"String 2\" = \"String 3\"")
    
    print("") #Line break to seperate the other statement
    
    print("This is:\"String 1\" \nAnd this is:\"String 2\"\n\nWhen I concatenate these two strings together, I get:\n\"String 1\" + \"String 2\" = \"String 3\"")

    #Repeating String

    string = "\"String\""
    
    print("This is another:")
    print("\"String\"")
    print("I can write it 5 times as follows:")
    print("\"String\"\"String\"\"String\"\"String\"\"String\"")

    print("This is another:\n\"String\"\nI can write it 5 times as follows:\n" + string[:8]*5)

    #Mathematical Operators

    print("7 + 3 =", 7+3)
    print("7 - 3 =", 7-3)
    print("7 * 3 =", 7*3)
    print("7 / 3 =", 7/3)
    print("7 // 3 =", 7//3)
    print("7 % 3 =", 7%3)
    

main()
