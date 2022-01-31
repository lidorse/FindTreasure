with open(r'C:\Users\lidor\Desktop\hodi\Score.txt','r+') as score:
    listOfScore = []
    numOftries = len(tries)
    for small in score.readlines(): #check all the numbers that smaller from numOftries Then appended to listOfScore
        if int(small) < numOftries:
            listOfScore.append(small)
    listOfScore.append(str(numOftries) + '\n') #append the player's numOftries to the listOfScore
    score.seek(0)
    for big in score.readlines(): #check all the number that big from numOftries Then appended to listOfScore
        if int(big) > numOftries:
            listOfScore.append(big)

with open(r'C:\Users\lidor\Desktop\hodi\Score.txt', 'w') as score: #open file to overwrite the listOfScore
    score.writelines(listOfScore[:-1]) #overwrite the file and remove the last score so there will be 10 places
