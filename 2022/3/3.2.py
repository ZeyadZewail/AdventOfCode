import time

with open('3.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


start_time = time.perf_counter()

totalPrio = 0
for i in range(0,len(lines),3):
    firstElf = lines[i]
    secondElf = lines[i+1]
    thirdElf = lines[i+2]
    duplicates = [letter for letter in firstElf if letter in secondElf]
    duplicates = [letter for letter in duplicates if letter in thirdElf]

    if(duplicates[0].islower()):
        totalPrio += ord(duplicates[0])-96
    else:
        totalPrio += ord(duplicates[0])-38
        

print(totalPrio)

elapsed = time.perf_counter() - start_time
print("Finished in",elapsed*1000,"ms")