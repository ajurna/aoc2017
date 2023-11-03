from collections import defaultdict
from dataclasses import dataclass
from typing import NamedTuple, Union


@dataclass
class Instruction:
    op: str
    a: Union[int, str]
    b: Union[int, str] = ''

    def __post_init__(self):
        try:
            self.a = int(self.a)
        except ValueError:
            pass
        try:
            self.b = int(self.b)
        except ValueError:
            pass


class VM:
    def __init__(self, f: str):
        self.program = []
        with open(f) as f:
            for line in f.readlines():
                self.program.append(Instruction(*line.split()))
        self.pointer = 0
        self.registers = {
            "a":0,
            "b":0,
            "c":0,
            "d":0,
            "e":0,
            "f":0,
            "g":0,
            "h":0
        }
        self.mul_count = 0

    def get_val(self, val):
        if val in self.registers:
            return self.registers[val]
        return val

    def run(self):
        while self.pointer < len(self.program):
            inst = self.program[self.pointer]
            match inst.op:
                case 'set':
                    self.registers[inst.a] = self.registers.get(inst.b, inst.b)
                case 'sub':
                    self.registers[inst.a] -= self.registers.get(inst.b, inst.b)
                case 'mul':
                    self.mul_count += 1
                    self.registers[inst.a] *= self.registers.get(inst.b, inst.b)
                case 'jnz':
                    if self.get_val(inst.a) != 0:
                        self.pointer += inst.b
                        continue
            self.pointer += 1

class VM2(VM):
    def run(self):
        while self.pointer < 12:
            inst = self.program[self.pointer]
            match inst.op:
                case 'set':
                    self.registers[inst.a] = self.registers.get(inst.b, inst.b)
                case 'sub':
                    self.registers[inst.a] -= self.registers.get(inst.b, inst.b)
                case 'mul':
                    self.mul_count += 1
                    self.registers[inst.a] *= self.registers.get(inst.b, inst.b)
                case 'jnz':
                    if self.get_val(inst.a) != 0:
                        self.pointer += inst.b
                        continue
            self.pointer += 1
        nonprimes = 0
        for b in range(self.registers['b'], self.registers['c']+1, 17):
            if any(b % d == 0 for d in range(2, int(b**0.5))):
                nonprimes += 1
        return nonprimes


vm = VM('01.txt')
vm.run()
print("Part 1:", vm.mul_count)
vm = VM2('01.txt')
vm.registers['a'] = 1
print("Part 2:", vm.run())
