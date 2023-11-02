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
    def __init__(self, f: str, p: int = 0):
        self.program = []
        with open(f) as f:
            for line in f.readlines():
                self.program.append(Instruction(*line.split()))
        self.pointer = 0
        self.last_sound = 0
        self.registers = defaultdict(int)
        self.registers["p"] = p
        self.queue = []
        self.output = []
        self.sent_count = 0

    def get_val(self, val):
        if val in self.registers:
            return self.registers[val]
        return val

    def run(self, part1: bool = False):
        while self.pointer < len(self.program):
            inst = self.program[self.pointer]
            match inst.op:
                case 'snd':
                    if part1:
                        self.last_sound = self.get_val(inst.a)
                    else:
                        self.sent_count += 1
                        self.output.append(self.get_val(inst.a))
                case 'set':
                    self.registers[inst.a] = self.get_val(inst.b)
                case 'add':
                    self.registers[inst.a] += self.get_val(inst.b)
                case 'mul':
                    self.registers[inst.a] *= self.get_val(inst.b)
                case 'mod':
                    self.registers[inst.a] %= self.get_val(inst.b)
                case 'rcv':
                    if part1:
                        if self.get_val(inst.b) != 0:
                            print("Part 1:", self.last_sound)
                            return
                    else:
                        if len(self.queue) > 0:
                            self.registers[inst.a] = self.queue.pop(0)
                        else:
                            return
                case 'jgz':
                    if self.get_val(inst.a) > 0:
                        self.pointer += self.get_val(inst.b)
                        continue
            self.pointer += 1


vm = VM('01.txt')
vm.run(part1=True)

vm0 = VM('01.txt', p=0)
vm1 = VM('01.txt', p=1)
vm0.output = vm1.queue
vm1.output = vm0.queue
vm0.run()
vm1.run()
while vm1.queue or vm0.queue:
    vm0.run()
    vm1.run()
print("Part 2:", vm1.sent_count)