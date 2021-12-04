inputFile = open("input.txt", "r")

def part1():
    depth = 0
    distance = 0

    for line in inputFile:
        splitLine = line.strip().split()
        action = splitLine[0]
        degree = splitLine[1]

        (depthGained, distanceGained) = getOutcome(action, int(degree))
        depth = depth + depthGained
        distance = distance + distanceGained
    print("distance is "+str(distance)+", depth is "+str(depth)+", multiplied: "+str(distance*depth))

def getOutcome(action, degree):
    depthGained = 0
    distanceGained = 0
    
    if (action == "forward"):
        distanceGained = degree
    else:
        if (action == "up"):
            depthGained = -degree
        else:
            depthGained = degree
    return (depthGained, distanceGained)

# part1()

def part2():
    depth = 0
    distance = 0
    aim = 0

    for line in inputFile:
        splitLine = line.strip().split()
        action = splitLine[0]
        degree = splitLine[1]

        (depthGained, distanceGained, aim) = getAdjustedOutcome(action, int(degree), aim)
        depth += depthGained
        distance += distanceGained
    print("distance is "+str(distance)+", depth is "+str(depth)+", multiplied: "+str(distance*depth))    

    
def getAdjustedOutcome(action, degree, aim):
    depthGained = 0
    distanceGained = 0

    if (action == "forward"):
        distanceGained = degree
        depthGained  = aim * degree
    else:
        if (action == "up"):
            aim -= degree
        else:
            aim += degree
    return (depthGained, distanceGained, aim)

part2()