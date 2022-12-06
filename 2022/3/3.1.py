with open('3.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

totalPrio = 0

for i in range(len(lines)):
    halfPoint = int(len(lines[i])/2)
    firstHalf = lines[i][0:halfPoint]
    secondHalf = lines[i][halfPoint:len(lines[i])]
    duplicates = [letter for letter in firstHalf if letter in secondHalf]

    if(duplicates[0].islower()):
        totalPrio += ord(duplicates[0])-96
    else:
        totalPrio += ord(duplicates[0])-38
        

print(totalPrio)