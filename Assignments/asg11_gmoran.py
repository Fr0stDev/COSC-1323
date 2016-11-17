# Assignment 11
# Guillermo Moran


def main():
    
    square = Rectangle()
    
    proceed = 0
    
    while (proceed == 0):
        try:
            userHeight = int(input("\nEnter a height for your rectangle: "))
            square.setHeight(userHeight)
        
            userWidth = int(input("\nEnter a width for your rectangle: "))
            square.setWidth(userWidth)
        
        except ValueError:
            print("Numeric characters only!")
        else:
            proceed = 1
        
    print("\n===== RECTANGLE ATTRIBUTES =====")
    print("\nSquare Height:", square.getHeight())
    print("Square Width:", square.getWidth())
    print("Square Perimeter:", square.getPerimeter())
    print("Square Area:", square.getArea())
    

######################################################
# Rectangle Class
######################################################

class Rectangle(object):
    
    def __init__(self):
        
        print("A rectangle has been spawned.")
        self.height = 0
        self.width = 0
        self.area = 0
        self.perimiter = 0
        
    def setHeight(self, height):
        
        self.height = height
        print("Set height:", height)
        
    def setWidth(self, width):
        
        self.width = width
        print("Set Width:", self.width)
        
    def calculateArea(self):
        
        self.area = self.height * self.width

    def calculatePerimeter(self):
        
        self.perimeter = 2*(self.height) + 2*(self.width)
        
    def getArea(self):
        
        self.calculateArea()
        return self.area
    
    def getPerimeter(self):
        
        self.calculatePerimeter()
        return self.perimeter
    
    def getHeight(self):
        
        return self.height
    
    def getWidth(self):
        
        return self.width
        
main()