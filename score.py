with open(r'C:\Users\lidor\Desktop\hodi\Score.txt','r+') as score:
    listOfScore = []
    num = 8
    for small in score.readlines(): #check all the number that smaller from num. of tries. Then appended to listOfScore
        if int(small) < num:
            listOfScore.append(small)
    listOfScore.append(str(num) + '\n') #append the num. of tries to the listOfScore
    score.seek(0)
    for big in score.readlines(): #check all the number that big from num. of tries. Then appended to listOfScore
        if int(big) > num:
            listOfScore.append(big)

with open(r'C:\Users\lidor\Desktop\hodi\Score.txt', 'w') as score: #open file to overwrite the list
    score.writelines(listOfScore[:-1]) #overwrite the file and remove the last score so there will be 10 places
