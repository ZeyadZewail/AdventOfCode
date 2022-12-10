import time

with open('10.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split()



#print(lines)
x = 1
signal = []
scores = []
for i in range(40*6):
    realIndex = i%len(lines)
    command = lines[realIndex][0]

    if(command == 'noop'):
        signal.append(x)
    elif(command == 'addx'):
        value = int(lines[realIndex][1])
        signal.extend([x,x])
        x+= value

    if(i in [19,59,99,139,179,219]):
        print(i+1,signal[i]*(i+1))
        scores.append(signal[i]*(i+1))

print("Part 1:",sum(scores))
    

drawIndex = 0
crt = ['']
lineIndex = 0
while drawIndex < 40*6:
    x = signal[drawIndex]
    if(abs((drawIndex%40)-x) < 2):
        crt[lineIndex] += '#'
    else:
        crt[lineIndex] += '.'
    
    drawIndex+=1
    if(drawIndex%40 == 0):
        crt.append('')
        lineIndex+=1

print("Part 2:")
for i in crt:
    if(i != ''):
        print(i)

