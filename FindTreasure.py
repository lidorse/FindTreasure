import random

x = random.randint(1, 20)
ran = list(range(0, 10)) * x

with open(r'C:\Users\lidor\Desktop\hodi\FindTreasure.txt','w') as writeTreasure:
    y = random.randint(0, x * 10)
    ran[y] = 'TREASURE'
    ran = str(ran)
    writeTreasure.write(ran)
    length = len(ran)
    print(f'The length of number is {length}')

with open(r'C:\Users\lidor\Desktop\hodi\FindTreasure.txt') as readTreasure:
    while True:
        try:
            x = int(input('For Forward hit 1, backwards hit 2: '))
            if 1 <= x <= 2:
                y = int(input('Enter the numbers of steps: '))
                if 0 <= y <= length:
                    readTreasure.seek(y)
                    where = readTreasure.tell()
                    print(ran[where])
                else: print('Out Of Range!')
            else: print('Wrong Direction!')
        except:
