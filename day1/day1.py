inputFile = open("input.txt", "r")

# Part 1
def part1():
    numIncreases = 0
    previousValue = -1

    for line in inputFile:
        line = line.strip()
        print("current: "+line)
        
        if previousValue != -1:
            if line > previousValue:
                print("current value of "+line+" >>> previous of "+previousValue)
                numIncreases = numIncreases + 1
            else: 
                print("current value of "+line+" < previous of "+previousValue)
        else:
            print("First value, not counting.")
        previousValue = line
    
    print(numIncreases)

part1()

def part2():
    numIncreases = 0
    previousValue = -1

    lines = []
    for line in inputFile:
        line = line.strip()
        lines.append(line)
    numLines = len(lines)
    
    for i in range(numLines):
        if i+2 >= numLines:
            print("reached the end, breaking. index is "+str(i))
            break
        sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        print("current index is "+str(i)+", sum is "+str(sum))

        if previousValue != -1:
            if sum > previousValue:
                numIncreases = numIncreases+1
        else:
            print("Skipping first sum")
        previousValue = sum
    print(numIncreases)

#part2()

    


