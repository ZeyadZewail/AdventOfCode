with open('2.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


def convert(line):
    Letters = line.split()

    if(Letters[0] == 'A'):
        Letters[0] =  'Rock'
    if(Letters[0] == 'B'):
        Letters[0] =  'Paper'
    if(Letters[0] == 'C'):
        Letters[0] =  'Scissors'
    
    if(Letters[1] =='Y'):
        Letters[1] = Letters[0]

    if(Letters[1] == 'X'):
        if(Letters[0] == 'Rock'):
            Letters[1] = 'Scissors'
        elif(Letters[0] == 'Paper'):
            Letters[1] = 'Rock'
        elif(Letters[0] == 'Scissors'):
            Letters[1] = 'Paper'

    if(Letters[1] == 'Z'):
        if(Letters[0] == 'Rock'):
            Letters[1] = 'Paper'
        elif(Letters[0] == 'Paper'):
            Letters[1] = 'Scissors'
        elif(Letters[0] == 'Scissors'):
            Letters[1] = 'Rock'

    
    return Letters

score = 0

for i in range(len(lines)):
    Letters = convert(lines[i])

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