inputFile = open("input.txt", "r")

# Stuff learnt:
# - Invoking a readline() will progress the file pointer by 1
# - if you are printing a string, you must cast all other types to string accordingly


def part1():
    numZeroes = getNumZeroes()
    oneCounter = [0] * numZeroes
    gamma = [0] * numZeroes
    epsilon = [0] * numZeroes
    numLines = 0

    for line in inputFile:
        line = line.strip()
        digits = list(line)

        for i in range(len(digits)):
            if (digits[i] == '1'):
                oneCounter[i] += 1
        numLines += 1

    for i in range(len(oneCounter)):
        if (oneCounter[i] > (numLines / 2)):
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    gamma = ''.join(gamma)
    epsilon = ''.join(epsilon)
    print("gamma is "+gamma+", epsilon is "+epsilon)
    print("power consumption is " + str(int(gamma, base=2) * int(epsilon, base=2)))

def getNumZeroes():
    line = inputFile.readline().strip()
    numDigits = len(list(line))
    inputFile.seek(0)
    return numDigits

part1()