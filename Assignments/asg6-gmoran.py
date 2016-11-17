#Assignment 6
#By Guillermo Moran

def main():

    teams = ["Orioles", "Red Sox", "Rangers", "Indians", "Tigers", "Astros", "Royals", "Angels"]
    printTeamNamesAndLenghts(teams, stringLengthList(teams))
    
    teams[1] = "Mets" #Replace Red Sox with Mets
    printTeamNamesAndLenghts(teams, stringLengthList(teams))
        
    teams.remove("Angels")
    teams.append("Marlins")
    printTeamNamesAndLenghts(teams, stringLengthList(teams))


def stringLengthList(teamList):

    teamNameLengthList = []
    
    for teamName in teamList:

        strLength = len(teamName)
        teamNameLengthList.append(strLength)

    return teamNameLengthList
        

def printTeamNamesAndLenghts(teamList, lengthList):
         
    print("Team Names:",teamList)
    print("Team String Lenghts:", lengthList,"\n")

main()
