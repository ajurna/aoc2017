import re
from collections import defaultdict

registers = defaultdict(int)
max_val = 0
with open('01.txt') as f:
    for line in f.readlines():
        command = re.match(r"(?P<target>\w+) (?P<incdec>inc|dec) (?P<amount>-?\d+) if (?P<c_reg>\w+) (?P<c_op>\S+) (?P<c_val>-?\d+)", line).groupdict()
        match command['c_op']:
            case '>':
                result = registers[command['c_reg']] > int(command['c_val'])
            case '<':
                result = registers[command['c_reg']] < int(command['c_val'])
            case '==':
                result = registers[command['c_reg']] == int(command['c_val'])
            case '!=':
                result = registers[command['c_reg']] != int(command['c_val'])
            case '>=':
                result = registers[command['c_reg']] >= int(command['c_val'])
            case '<=':
                result = registers[command['c_reg']] <= int(command['c_val'])
            case _:
                print("error")
                quit()
        if result:
            match command['incdec']:
                case 'inc':
                    registers[command['target']] += int(command['amount'])
                case 'dec':
                    registers[command['target']] -= int(command['amount'])
        max_val = max(max_val, max(registers.values()))
print("Part 1:", max(registers.values()))
print("Part 2:", max_val)
