with open('2.txt') as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = lines[i].split(" ")
    lines[i][1] = int(lines[i][1].strip())

x = 0
y = 0

for i in lines:
    value = i[1]

    if(i[0] == "forward"):
        x += value

    if(i[0] == "down"):
        y += value

    if(i[0] == "up"):
        y -= value

#print(lines)
print(x*y)