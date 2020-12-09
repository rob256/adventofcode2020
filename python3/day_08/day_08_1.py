class DuplicateInstructionException(Exception):
    pass


class MyMassiveMegaMachine:
    def __init__(self, input_instructions_file):
        self.instructions = self._parse_instructions(input_instructions_file)
        self.current_value = 0
        self.instruction_index = 0
        self.processed_instructions = set()
    
    @staticmethod
    def _parse_instructions(input_instructions_file):
        instructions = []
        with open(input_instructions_file) as f:
            for line in f:
                instruction, arg = line.split()
                instructions.append((instruction, int(arg)))
        return instructions

    def next(self):
        if self.instruction_index in self.processed_instructions:
            raise DuplicateInstructionException()
        
        self.processed_instructions.add(self.instruction_index)

        instruction, value = self.instructions[self.instruction_index]
        self.process(instruction, value)
    
    def process(self, instruction, value):
        if instruction == "nop":
            self.instruction_index += 1
        elif instruction == "acc":
            self.current_value += value
            self.instruction_index += 1
        elif instruction == "jmp":
            self.instruction_index += value
        else:
            raise ValueError(f"Instruction {instruction} not recognised.")
    
    def run_until_exit(self):
        try:
            while True:
                self.next()
        except DuplicateInstructionException:
            pass


def solve():
    machine = MyMassiveMegaMachine('input.txt')
    machine.run_until_exit()
    print(machine.current_value)


if __name__ == "__main__":
    solve()