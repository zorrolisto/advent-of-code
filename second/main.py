f = open("data.txt", "r") 
lines = f.readlines()

# TEST
"""lines = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]"""

depth = 0
position = 0
for line in lines:
    values = line.split(' ')
    if values[0] == 'forward':
        position += int(values[1])
    if values[0] == 'down':
        depth += int(values[1])
    if values[0] == 'up':
        depth -= int(values[1])
print("first part")
print("depth:", depth, "position:", position, "result:", depth*position)

depth = 0
position = 0
aim = 0
for line in lines:
    values = line.split(' ')
    if values[0] == 'forward':
        position += int(values[1])
        depth += int(values[1])*aim
    if values[0] == 'down':
        aim += int(values[1])
    if values[0] == 'up':
        aim -= int(values[1])
print("second part")
print("depth:", depth, "position:", position, "result:", depth*position)