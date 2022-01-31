import random

def countTries():
    '''
    appends the player's trie's numbers to list so we can use len function
    :return: add numbers to list
    '''
    tries.append(stepsNum)

def forwardPointerMove():
    '''
    insert number of steps + the place pointer is, minus 1 place (starting from 0)
    :return: move seek back and print the syntax where the pointer is
    '''
    FWplace = (int(readTreaser.tell()) + stepsNum) -1
    readTreaser.seek(FWplace)
    print(readTreaser.readline(1))

def backwardsPointerMove():
    '''
    insert number of steps - the place pointer is, minus 1 place (starting from 0)
    :return: move seek back and print the syntax where the pointer is
    '''
    BWplace = (int(readTreaser.tell()) - stepsNum) - 1
    readTreaser.seek(BWplace)
    print(readTreaser.readline(1))

def treasureFound():
    '''
    Move pointer step back for printing the right place
    :return: if the pointer prints one letter from 'TREASURE' then there is a win
    '''
    readTreaser.seek(readTreaser.tell() - 1)
    if readTreaser.readline(1).isalpha():
        return True

with open(r'C:\Users\lidor\Desktop\hodi\FindTreasure.txt','w') as writeTreaser: # open as 'w' to overwrite file
    x = random.randint(1, 20) # Random times to print the numbers(0-9)
    for num in range(0, 10):
        num1 = str(num) # string to write file
        numlist = num1 * x # duplicate every number at random times
        writeTreaser.writelines(numlist)

    writeTreaser.writelines('TREASURE') # print the treasure between numbers

    for numR in range(9,-1,-1): # Reversed numbers
        numR1 = str(numR)
        numRlist = numR1 * x
        writeTreaser.writelines(numRlist)

    maxSteps = writeTreaser.tell()
    print(f'End of steps are in {maxSteps} moves') # Print the amount of steps the player can move

with open(r'C:\Users\lidor\Desktop\hodi\FindTreasure.txt') as readTreaser: # open as 'r' only
    tries = [] #count the number of player's tries with len function
    while True:
        try:  # The player need to insert an int!
            stepsNum = int(input('How many step would you like to go? '))
            if stepsNum > maxSteps: #check that the player's steps not out of range
                print('Out of range, please try again')
                continue
            direction = int(input('Press 1 to move FORWARD, Press 2 for BACKWARDS '))
            if direction == 1: # checks if the player choose right direction
                forwardPointerMove()
                countTries()
            elif direction == 2: # checks if the player choose right direction
                backwardsPointerMove()
                countTries()
            else:
                print('Out of Range')
                continue #if direction not 1 or 2
        except:
            print('Error Value!')
            continue

        if treasureFound() == True:
            print(f'Number of tries are {len(tries)}') # print the number of player's tries
            break
