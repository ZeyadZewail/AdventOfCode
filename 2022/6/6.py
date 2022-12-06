import time

with open('6.txt') as f:
    lines = f.readlines()

input = lines[0]

last4 = []

def checkUnique(list):
    if(len(set(list)) == len(list)):
        return True
    else:
        return False

#part 1
start_time = time.perf_counter()
counter = 0
for i in range(len(input)):
    if(len(last4)<4):
        last4.append(input[i])
    else:
        last4.append(input[i])
        del last4[0]

    counter += 1 

    if(checkUnique(last4) and len(last4) == 4):
        break

print("Part 1",counter)
elapsed = time.perf_counter() - start_time
print("Finished in",elapsed*1000,"ms")

#part 22
start_time = time.perf_counter()
counter = 0
for i in range(len(input)):
    if(len(last4)<14):
        last4.append(input[i])
    else:
        last4.append(input[i])
        del last4[0]

    counter += 1 

    if(checkUnique(last4) and len(last4) == 14):
        break

print("Part 2",counter)
elapsed = time.perf_counter() - start_time
print("Finished in",elapsed*1000,"ms")