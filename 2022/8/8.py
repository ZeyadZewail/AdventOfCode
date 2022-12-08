import time

with open('8.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()


#part 1
start_time = time.perf_counter()
counter = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        value = int(lines[i][j])
        visible = False
        #print(i,j,value)
        #edge
        if(j == 0 or j == len(lines[i])-1 or i == 0 or i == len(lines)-1):
            counter+=1
            continue
        
        #top
        newI = i-1
        while(newI>=0):
            if(int(lines[newI][j]) >= value):
                visible = False
                break
            visible = True
            newI -=1
        
        if(visible):
            #print("Top | I:",i,"J:",j,"N:",lines[i][j])
            counter+=1
            continue

        #bot
        newI = i+1
        while(newI<=len(lines)-1):
            if(int(lines[newI][j]) >= value):
                visible = False
                break
            visible = True
            newI +=1
        
        if(visible):
            #print("Bot | I:",i,"J:",j,"N:",lines[i][j])
            counter+=1
            continue

        #Right
        newJ = j+1
        while(newJ<=len(lines[0])-1):
            if(int(lines[i][newJ]) >= value):
                visible = False
                break
            visible = True
            newJ +=1
        
        if(visible):
            #print("Right | I:",i,"J:",j,"N:",lines[i][j])
            counter+=1
            continue

        #Left
        newJ = j-1
        while(newJ>=0):
            if(int(lines[i][newJ]) >= value):
                visible = False
                break
            visible = True
            newJ -=1
        
        if(visible):
            #print("Left | I:",i,"J:",j,"N:",lines[i][j])
            counter+=1
            continue
        

print("Part 1",counter)
elapsed = time.perf_counter() - start_time
print("Finished in",elapsed*1000,"ms")

#part 2
start_time = time.perf_counter()
max = -999
for i in range(len(lines)):
    for j in range(len(lines[i])):
        value = int(lines[i][j])
        visible = False
        top = 0
        bot = 0
        right = 0
        left = 0
        
        #top
        newI = i-1
        while(newI>=0):
            top+=1
            if(int(lines[newI][j]) >= value):
                break
            newI -=1
        
        #bot
        newI = i+1
        while(newI<=len(lines)-1):
            bot+=1
            if(int(lines[newI][j]) >= value):
                break
            newI +=1
        
        #Right
        newJ = j+1
        while(newJ<=len(lines[0])-1):
            right+=1
            if(int(lines[i][newJ]) >= value):
                break
            newJ +=1
        
        #Left
        newJ = j-1
        while(newJ>=0):
            left+=1
            if(int(lines[i][newJ]) >= value):
                break
            newJ -=1
        
        score = top*bot*left*right
        if(score > max):
            max = score
        

print("Part 2",max)
elapsed = time.perf_counter() - start_time
print("Finished in",elapsed*1000,"ms")