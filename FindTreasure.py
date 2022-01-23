import random

x = random.randint(1, 20)
ran = list(range(0, 10)) * x #random list of number

with open(r'C:\Users\lidor\Desktop\hodi\FindTreasure.txt','w') as writeTreasure:
    y = random.randint(0, x * 10)
    ran[y] = 'TREASURE' #insert the string in a random index(place)
    ran = str(ran)
    writeTreasure.write(ran)
    length = len(ran)
    print(f'The length of number is {length-1}') #show the player the length of options

with open(r'C:\Users\lidor\Desktop\hodi\FindTreasure.txt') as readTreasure:
    fullList = ['A', 'E', 'E', 'R', 'R', 'S', 'T', 'U'] #sorted list of the word TREASURE
    emptyList = []
    numberOfTry = []
    while True:
        try:
            x = int(input('For Forward hit 1, backwards hit 2: '))
            numberOfTry.append(x)
            if 1 <= x <= 2:
                y = int(input('Enter the numbers of steps: '))
                if 0 <= y <= length:
                    readTreasure.seek(y) #move the pointer to the steps player inserted
                    where = readTreasure.tell() #where is the pointer
                    print(ran[where]) #print the string of the place the player moved to
                    if ran[where] == 'T' or ran[where] == 'R' or ran[where] == 'E' or ran[where] == 'A' or \
                        ran[where] == 'S' or ran[where] == 'U' or ran[where] == 'R' or ran[where] == 'E':
                        emptyList.append(ran[where])
                        emptyList.sort()
                        print(emptyList)
                        if emptyList == fullList:
                            print('You found the treasure!!!')
                            tries = len(numberOfTry)
                            print(f'Number Of Tries are {tries}')
                            break
                else: print('Out Of Range!')
            else: print('Wrong Direction!')
        except:
            print('Out of the rules!') #if the player inserted anything else but string

with open(r'C:\Users\lidor\Desktop\hodi\FindTreasure.txt','a+') as score:
    for num in score.readline():
        print(num)
