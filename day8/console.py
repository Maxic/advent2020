class Console:
    def __init__(self, program):
        self.pointer = 0
        self.accumulator = 0
        self.program = program
        self.pointer_passed = []
        self.corrupted = False

    def run(self):

        while True:

            # Check stop condition
            if self.pointer == self.program.__len__():
                break

            instruction = self.program[self.pointer][0]
            value = self.program[self.pointer][1]

            # Check if program is corrupted
            if self.pointer in self.pointer_passed:
                self.corrupted = True
                break
            else:
                self.pointer_passed.append(self.pointer)

            if instruction == 'nop':
                self.pointer += 1

            if instruction == 'acc':
                if value[0] == '+':
                    self.accumulator += int(value[1:])
                if value[0] == '-':
                    self.accumulator -= int(value[1:])
                self.pointer += 1

            if instruction == 'jmp':
                if value[0] == '+':
                    self.pointer += int(value[1:])
                if value[0] == '-':
                    self.pointer -= int(value[1:])


