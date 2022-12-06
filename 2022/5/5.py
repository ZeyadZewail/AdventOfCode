import time
import numpy
import copy

with open('5.txt') as f:
    lines = f.readlines()

commands = lines[10:]
for i in range(len(commands)):
    commands[i] = commands[i].strip()

boxes = lines[0:8]

for i in range(len(boxes)):
    boxes[i] = boxes[i].replace('    ',' [0]').strip().replace(' ','')
    boxes[i] = boxes[i].replace('[',' ').replace(']',' ').split()

boxes = numpy.rot90(boxes,3)
boxes = list(boxes)

for i in range(len(boxes)):
    boxes[i] = list(filter(lambda x: x!= '0',boxes[i]))


#part 1
def part1(boxes):
    temp_boxes = copy.deepcopy(boxes)
    start_time = time.perf_counter()
    for i in range(len(commands)):
        numbers = list(filter(lambda x: x.isnumeric(),commands[i].split()))
        count = int(numbers[0])
        col1 = int(numbers[1])-1
        col2 = int(numbers[2])-1

        for c in range(count):
            temp_boxes[col2].append(temp_boxes[col1][-1])
            del temp_boxes[col1][-1]

    answer = ''
    for b in temp_boxes:
        answer += b[-1] 

    print("Part 1",answer)
    elapsed = time.perf_counter() - start_time
    print("Finished in",elapsed*1000,"ms")
    
#part 2
def part2(boxes):
    temp_boxes = copy.deepcopy(boxes)
    start_time = time.perf_counter()
    for i in range(len(commands)):
        numbers = list(filter(lambda x: x.isnumeric(),commands[i].split()))
        count = int(numbers[0])
        col1 = int(numbers[1])-1
        col2 = int(numbers[2])-1

        moved = temp_boxes[col1][-count:]
        del temp_boxes[col1][-count:]
        temp_boxes[col2].extend(moved)

    answer = ''
    for b in temp_boxes:
        answer += b[-1] 
    
    print("Part 2",answer)
    elapsed = time.perf_counter() - start_time
    print("Finished in",elapsed*1000,"ms")

part1(boxes)
part2(boxes)