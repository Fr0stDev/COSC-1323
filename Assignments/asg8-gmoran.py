#Assignment 8
#Guillermo Moran

def main():
    try:
        classesFile = open("Classes.txt", "r")
        
        for line in classesFile:
            print(line)
        
        classesFile.close()
    
    except FileNotFoundError:
        print("Classes file not found")
        
main()