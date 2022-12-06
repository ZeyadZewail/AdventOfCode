with open('1.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

elves =[0]

for i in range(len(lines)):
    if(lines[i] == ''):
        elves.append(0)
    else:
        elves[-1]+= int(lines[i])

print("Top elf:",max(elves))


#part 2

elves.sort(reverse=True)
print("Top 3 total:",sum(elves[0:3]))
