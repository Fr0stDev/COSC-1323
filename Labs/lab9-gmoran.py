#Lab 9 - Bryan
#Guillermo Moran

def main():
    
    colors = ["Green", "Red", "Blue", "White", "Black"]
    
    colorsDictionary = {}
    
    i = 1
    
    while (i < 100):
        
        for colorName in colors:
            colorsDictionary[i] = colorName
            i += 1
    
    print(colorsDictionary)
    
main()