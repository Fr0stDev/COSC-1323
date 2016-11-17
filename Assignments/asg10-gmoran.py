######################################################
# Alien Spacecraft / Assignment 10
# By Guillermo Moran
# Nov 15 2015
######################################################

#Just for fun.
#Probably shouldn't be using global variables like this either
#But I'm too lazy to implement this any other way
#Sorry! :P
USERNAME = input("Please enter a username: ")

def main():
    
    spacecraft = AlienSpacecraft()
    showUserMenuForSpacecraft(spacecraft)
    
######################################################
# fireWeaponsForSpacecraft(spacecraft)
# fires weapons for the passed spacecraft object
# Then returns to the control menu
######################################################
    
def fireWeaponsForSpacecraft(spacecraft):
    
    spacecraft.fireWeapons()
    showUserMenuForSpacecraft(spacecraft)
    
######################################################
# setDirectionForSpacecraft(spacecraft)
# sets direction for the passed spacecraft object
# Then returns to the control menu
######################################################
    
def setDirectionForSpacecraft(spacecraft):
    
    directionToSet = ""
    validDirections = ["north", "east", "south", "west"]
    
    while (directionToSet not in validDirections):
        try:
            directionToSet = input("\nPlease enter the desired direction (North, East, South, West): ")
            directionToSet = directionToSet.lower()
            spacecraft.setDirection(directionToSet)
        except ValueError:
            print("\nThat was not a valid direction.")
    
    
        
    showUserMenuForSpacecraft(spacecraft)
    
######################################################
# setVelocityForSpacecraft(spacecraft)
# sets velocity for the passed spacecraft object
# Then returns to the control menu
######################################################
    
def setVelocityForSpacecraft(spacecraft):
    
    velocityLevelToSet = 0 #Nothing set yet
    
    while (velocityLevelToSet < 1 or velocityLevelToSet > 10):
        
        try:
            velocityLevelToSet = int(input("\nEnter Velocity (1-10): "))
            spacecraft.setVelocity(velocityLevelToSet)
        except ValueError:
            print("Invalid velocity.")
    
    showUserMenuForSpacecraft(spacecraft)
    
######################################################
# addAmmunitionForSpacecraft(spacecraft)
# adds ammunition to the passed spacecraft object
# Then returns to the control menu
######################################################
    
def addAmmunitionForSpacecraft(spacecraft):
    
    ammunitionLevelToSet = 0 #Nothing set yet
    
    while (ammunitionLevelToSet < 1 or ammunitionLevelToSet > 10):
        
        try:
            ammunitionLevelToSet = int(input("\nEnter ammunition level (1-10): "))
            spacecraft.setAmmunitionLevel(ammunitionLevelToSet)
        except ValueError:
            print("Invalid ammunition level.")
    
    showUserMenuForSpacecraft(spacecraft)
    
######################################################
# printValuesForSpacecraft(spacecraft)
# prints values for the passed spacecraft object
# Then returns to the control menu
######################################################
    
def printValuesForSpacecraft(spacecraft):
    
    spacecraft.printCurrentValues()
    showUserMenuForSpacecraft(spacecraft)
    
######################################################
# showUserMenuForSpacecraft(spacecraft)
# Displays the list of commands for the passed 
# spacecraft object. 
#
# This would also allow for various spacecraft objects
# to be managed at the same time. Yay!
######################################################
                    
def showUserMenuForSpacecraft(spacecraft):
    
    print("\nHello %s, welcome to your spacecraft!" % USERNAME)
    
    userSelection = 0 #Nothing is selected
    
    while ((userSelection > 6) or (userSelection < 1)):
        
        print("\nPlease make a selection from the following choice of commands:")
        
        print("\n1) Add Ammunition (1-10)")
        print("2) Set Velocity (0-10)")
        print("3) Set Direction (North, South, East, West)")
        print("4) Fire Weapons")
        print("5) Print Current Values")
        print("6) Exit\n")
        
        try:
            userSelection = int(input("Please enter your selection: "))
        except ValueError:
            print("\nThat was not a number.")
            
    if (userSelection == 1):
        #Add Ammunition
        addAmmunitionForSpacecraft(spacecraft)
        
    if (userSelection == 2):
        # Set Velocity
        setVelocityForSpacecraft(spacecraft)
        
    if (userSelection == 3):
        #Set Direction
        setDirectionForSpacecraft(spacecraft)
        
    if (userSelection == 4):
        #Fire Weapons
        fireWeaponsForSpacecraft(spacecraft)
        
    if (userSelection == 5):
        #Print Values
        printValuesForSpacecraft(spacecraft)
        
    if (userSelection == 6):
        #Set Direction
        print("Shutting down Spacecraft. Goodbye, %s." % USERNAME)

# =================================================================
# AlienSpacecraft Class
# =================================================================
class AlienSpacecraft(object):
    
    # Constructor
    # Creates an AlienSpacecraft and initializes class variables
    #
    def __init__(self):
        
        print("A alien spacecraft has been born!")
        self.velocity = 0
        self.direction = "north"
        self.ammunitionLevel = 0  
    
    # setVelocity()
    # Sets the velocity of the alien spacecraft
    # Valid values are 0 - 10
    # raises ValueError if velocity is out of range
    #    
    def setVelocity(self, velocity) :
        
        if (velocity < 0 or (velocity + self.velocity) > 10 ) :
            raise ValueError("Error: velocity must be between 0 and 10")
        
        self.velocity = velocity
        
        print("Moving ", self.direction, "at velocity of ", self.velocity)
    
    # getVelocity()
    # returns the current spacecraft velocity
    #    
    def getVelocity(self) :
        return self.velocity
    
    # setDirection()
    # Sets the direction of the spacecraft
    # Valid directions are north, south, east or west
    # Raises a ValueError for an invalid direction
    def setDirection(self, direction) :
        
        allDirections = ["north", "south", "east", "west"]
        
        if (direction not in allDirections ) :
            raise ValueError("Error: direction must be north, south, east or west")
        
        self.direction = direction
        
        print("Direction set to", self.direction)
    
    # getDirection()
    # Returns the current direction
    #
    def getDirection(self):
        
        return self.direction
    
    # setAmmunitionLevel()
    # Sets the ammunitionLevel of the spacecraft
    # Valid values are 0 - 10
    # Raises a ValueError if for an invalid ammunitionLevel
    #
    def setAmmunitionLevel(self, ammunitionLevel):
        
        if (ammunitionLevel < 0 or ammunitionLevel > 10) :
            raise ValueError("AmmunitionLevel must be between 0 and 10")
    
        self.ammunitionLevel = ammunitionLevel
        
        print("AmmunitionLevel set to ", self.ammunitionLevel)

    # getAmmunitionLevel()
    # Returns the current ammumition level
    #
    def getAmmunitionLevel(self):
        
        return self.ammunitionLevel

    # fireWeapons()
    # Fires the alien spacecraft weapons.
    # Decrements ammunitionlevel by 1
    # Prints error message if weapons fired and there is no
    # ammunition
    def fireWeapons(self):
        
        if (self.ammunitionLevel ==  0) :
            print("No Ammunition!  Rats, we're done for!")
            return
        else :
            self.ammunitionLevel -= 1
            print("Weapons fired!")

    # printCurrentValues()
    # Prints current values of object attributes
    #
    def printCurrentValues(self):
        
        print("\nCurrent Values:\n-------------------")
        print("Velocity: ", self.getVelocity())
        print("Direction: ", self.getDirection())
        print("Ammunition Level: ", self.getAmmunitionLevel())
        print("\n\n")

   
main()