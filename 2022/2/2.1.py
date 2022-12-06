with open('2.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


def convert(letter):
    if(letter == 'A' or letter == 'X'):
        return 'Rock'
    if(letter == 'B' or letter == 'Y'):
        return 'Paper'
    if(letter == 'C' or letter == 'Z'):
        return 'Scissors'


score = 0

for i in range(len(lines)):
    Letters = lines[i].split()
    Letters[0] = convert(Letters[0])
    Letters[1] = convert(Letters[1])

    #choice value
    if(Letters[1]=='Rock'):
        score+=1
    elif(Letters[1]=='Paper'):
        score+=2
    elif(Letters[1]=='Scissors'):
        score+=3

    #draw
    if(Letters[0] == Letters[1]):
        score+=3

    #win con
    if(Letters[0]== 'Scissors' and Letters[1] == 'Rock'):
        score+=6
    if(Letters[0]== 'Rock' and Letters[1] == 'Paper'):
        score+=6
    if(Letters[0]== 'Paper' and Letters[1] == 'Scissors'):
        score+=6
    
print(score)