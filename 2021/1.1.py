with open('1.txt') as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

counter = 0
for i in range(len(lines)-1):
    if(lines[i+1] > lines[i]):
        counter += 1

print(counter)