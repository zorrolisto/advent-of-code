f = open("data.txt", "r") 
lines = f.readlines()

# TEST
"""lines = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]"""

numberOfLines = len(lines)
arrayForNumbers = [0 for i in lines[0]]
arrayForNumbers.pop()
for line in lines:
    for idx, bit in enumerate(line):
        if str(bit) == "1":
            arrayForNumbers[idx] += 1
#print("arrayForNumbers", arrayForNumbers)

gammaRate = []
epsilonRate = []
for sumTotal in arrayForNumbers:
    if sumTotal > numberOfLines/2:
        gammaRate.append('1')
        epsilonRate.append('0')
    if sumTotal < numberOfLines/2:
        gammaRate.append('0')
        epsilonRate.append('1')


gammaRateNum = int(''.join(gammaRate), 2)
epsilonRateNum = int(''.join(epsilonRate), 2)

#print("gammaRateNum", gammaRateNum)
#print("epsilonRateNum", epsilonRateNum)
#print("Result: ", gammaRateNum*epsilonRateNum)



############################### SECOND PART ############################### 

numberOfLines = len(lines)
arrayForNumbers = [0 for i in lines[0]]
arrayForNumbers.pop()

linesFiltered = lines.copy()
for index, sumTotal in enumerate(arrayForNumbers):
    for line in linesFiltered:
        if str(line[index]) == "1":
            arrayForNumbers[index] += 1
    if arrayForNumbers[index] >= len(linesFiltered)/2:
        linesFiltered = list(filter(lambda l: l[index] == '1', linesFiltered))
    else:
        linesFiltered = list(filter(lambda l: l[index] == '0', linesFiltered))
    if len(linesFiltered) == 1:
        break;
oxygenGeneratorRating = int(''.join(linesFiltered), 2)
print("oxygenGeneratorRating", oxygenGeneratorRating )


arrayForNumbers = [0 for i in lines[0]]
arrayForNumbers.pop()
linesFiltered = lines.copy()
for index, sumTotal in enumerate(arrayForNumbers):
    for line in linesFiltered:
        if str(line[index]) == "1":
            arrayForNumbers[index] += 1
    if arrayForNumbers[index] >= len(linesFiltered)/2:
        linesFiltered = list(filter(lambda l: l[index] == '0', linesFiltered))
    else:
        linesFiltered = list(filter(lambda l: l[index] == '1', linesFiltered))
    if len(linesFiltered) == 1:
        break;
co2ScrubberRating = int(''.join(linesFiltered), 2)
print("co2ScrubberRating", co2ScrubberRating)

print("result", co2ScrubberRating*oxygenGeneratorRating)
