import time

with open('4.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split(',')

#part 1
start_time = time.perf_counter()
counter = 0

for i in range(len(lines)):
    firstRange = lines[i][0].split('-')
    secondRange = lines[i][1].split('-')
    
    if(int(firstRange[0]) <= int(secondRange[0]) and int(firstRange[1]) >= int(secondRange[1])):
        counter+=1
    elif(int(firstRange[0]) >= int(secondRange[0]) and int(firstRange[1]) <= int(secondRange[1])):
        counter+=1

print("Part 1",counter)
elapsed = time.perf_counter() - start_time
print("Finished in",elapsed*1000,"ms")
#part 2
start_time = time.perf_counter()
counter = 0
for i in range(len(lines)):
    firstRange = lines[i][0].split('-')
    secondRange = lines[i][1].split('-')
    
    #2-6,6-8
    if(int(secondRange[0]) <= int(firstRange[1]) and int(firstRange[0]) <= int(secondRange[1])):
        counter+=1

print("Part 2",counter)
elapsed = time.perf_counter() - start_time
print("Finished in",elapsed*1000,"ms")