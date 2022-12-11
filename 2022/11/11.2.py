import time

with open('11.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

class Monkey:
    def __init__(self, monkeyLines):
        self.items = monkeyLines[1].replace(',','').split()[2:]
        for i in range(len(self.items)):
            self.items[i] = int(self.items[i])

        self.operation = monkeyLines[2].split()[3:]
        self.testText = monkeyLines[3].split()[1:]
        self.trueAction = monkeyLines[4].split()
        self.falseAction = monkeyLines[5].split()
        self.inspectorCount = 0


    def test(self,value):
        if self.testText[0] == 'divisible':
            factor = int(self.testText[2])
            return value%factor == 0

    def operate(self,value):
        if(self.operation[2] == 'old'):
            return value * value
        
        factor = int(self.operation[2])
        if self.operation[1] == '+':
            return value + factor

        if self.operation[1] == '*':
            return value * factor

    def inspectAll(self):
        testValues = []
        for i in range(len(self.items)):
            self.items[i] = self.operate(self.items[i])
            #self.items[i] = self.items[i] // 3
            #self.items[i] = self.items[i] % 9699690

            testValues.append(self.test(self.items[i]))

        self.inspectorCount += len(self.items)
        return testValues

    def clearItems(self):
        self.items = []

monkeys:list[Monkey] = []
for i in range(8):
    start = 7*i
    end = 7*(i+1)-1
    monkeys.append(lines[start:end])

for i in range(len(monkeys)):
    monkeys[i] = Monkey(monkeys[i])

for round in range(10000):
    
    for monkey in monkeys:
        testValues = monkey.inspectAll()

        for i in range(len(testValues)):
            if(testValues[i]):
                monkeys[int(monkey.trueAction[-1])].items.append(monkey.items[i])
            else:
                monkeys[int(monkey.falseAction[-1])].items.append(monkey.items[i])

        monkey.clearItems()
    
    # print("Round",round+1)
    # for monkey in monkeys:
    #     print(monkey.items)

counts = []
for monkey in monkeys:
    counts.append(monkey.inspectorCount)

print(sorted(counts)[-1]*sorted(counts)[-2])
