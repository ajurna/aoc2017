from dataclasses import dataclass, field
from typing import Set


@dataclass
class TuringMachine:
    tape: Set = field(default_factory=set)
    cursor: int = 0
    steps: int = 12261543
    next_state = 'a'

    def run(self):
        states = {
            'a': self.state_a,
            'b': self.state_b,
            'c': self.state_c,
            'd': self.state_d,
            'e': self.state_e,
            'f': self.state_f
        }
        for _ in range(self.steps):
            states[self.next_state]()

    def state_a(self):
        if self.cursor in self.tape:
            """
            - Write the value 0.
            - Move one slot to the left.
            - Continue with state C.
            """
            self.tape.remove(self.cursor)
            self.cursor -= 1
            self.next_state = 'c'
        else:
            """
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state B.
            """
            self.tape.add(self.cursor)
            self.cursor += 1
            self.next_state = 'b'

    def state_b(self):
        if self.cursor in self.tape:
            """
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state C.
            """
            self.cursor += 1
            self.next_state = 'c'
        else:
            """
            - Write the value 1.
            - Move one slot to the left.
            - Continue with state A.
            """
            self.tape.add(self.cursor)
            self.cursor -= 1
            self.next_state = 'a'

    def state_c(self):
        if self.cursor in self.tape:
            """
            - Write the value 0.
            - Move one slot to the left.
            - Continue with state D.
            """
            self.tape.remove(self.cursor)
            self.cursor -= 1
            self.next_state = 'd'
        else:
            """
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state A.
            """
            self.tape.add(self.cursor)
            self.cursor += 1
            self.next_state = 'a'

    def state_d(self):
        if self.cursor in self.tape:
            """
            - Write the value 1.
            - Move one slot to the left.
            - Continue with state C.
            """
            self.tape.add(self.cursor)
            self.cursor -= 1
            self.next_state = 'c'
        else:
            """
            - Write the value 1.
            - Move one slot to the left.
            - Continue with state E.
            """
            self.tape.add(self.cursor)
            self.cursor -= 1
            self.next_state = 'e'

    def state_e(self):
        if self.cursor in self.tape:
            """
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state A.
            """
            self.tape.add(self.cursor)
            self.cursor += 1
            self.next_state = 'a'
        else:
            """
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state F.
            """
            self.tape.add(self.cursor)
            self.cursor += 1
            self.next_state = 'f'

    def state_f(self):
        if self.cursor in self.tape:
            """
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state E.
            """
            self.tape.add(self.cursor)
            self.cursor += 1
            self.next_state = 'e'
        else:
            """
            - Write the value 1.
            - Move one slot to the right.
            - Continue with state A.
            """
            self.tape.add(self.cursor)
            self.cursor += 1
            self.next_state = 'a'


tm = TuringMachine()
tm.run()
print("Part 1:", len(tm.tape))