with open('01.txt') as f:
    data = f.read().strip()

total = 0
for i in range(len(data)-1):
    if data[i] == data[i+1]:
        total += int(data[i])
if data[0] == data[-1]:
    total += int(data[0])
print("Part 1:", total)

total = 0
for i in range(len(data)):
    if data[i] == data[(i + len(data)//2) % len(data)]:
        total += int(data[i])
print("Part 2:", total)