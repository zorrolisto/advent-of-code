f = open("data.txt", "r") 
lines = f.readlines()

# TEST
"""lines = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]"""
 
incrementsFirstPart = 0
for idx, line in enumerate(lines):
    if idx == 0:
        continue
    if int(line) > int(lines[idx - 1]):
        incrementsFirstPart+=1
print("Increments first part: ", incrementsFirstPart)

 
incrementsSecondPart = 0
for idx, line in enumerate(lines):
    if idx > len(lines) - 4:
        break
    firstThreeSum = int(line) + int(lines[idx + 1]) + int(lines[idx + 2])
    secondThreeSum = int(lines[idx + 1]) + int(lines[idx + 2]) + int(lines[idx + 3])
    #print('firstThreeSum', firstThreeSum, 'secondThreeSum', secondThreeSum )
    if secondThreeSum > firstThreeSum:
        incrementsSecondPart +=1
print("Increments second part: ", incrementsSecondPart)