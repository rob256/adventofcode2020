from typing import List, Tuple, Dict


class DuplicateInstructionException(Exception):
    pass


class MyMassiveMegaMachine:
    def __init__(self, input_instructions_file):
        self.instructions = self._parse_instructions(input_instructions_file)
        self.current_value = 0
        self.instruction_index = 0
        self.processed_instructions = set()
    
    @staticmethod
    def _parse_instructions(input_instructions_file) -> List[Tuple[str, int]]:
        instructions = []
        with open(input_instructions_file) as f:
            for line in f:
                instruction, arg = line.split()
                instructions.append((instruction, int(arg)))
        return instructions
    
    def has_next(self):
        return self.instruction_index < len(self.instructions)

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
    
    def run_until_exit(self) -> bool:
        try:
            while True:
                if self.has_next():
                    self.next()
                else:
                    return True
        except DuplicateInstructionException:
            return False

    def get_instruction_replacements(self, instructions_to_replace: List[str], replace_map: Dict[str, str]) -> Tuple[int, str, int]:
        for instruction_to_replace in instructions_to_replace:
            for i, (instruction, value) in enumerate(self.instructions):
                if instruction == instruction_to_replace:
                    yield i, replace_map[instruction], value


def solve():
    instruction_replace_map = {
        'nop': 'jmp',
        'jmp': 'nop',
    }

    default_machine = MyMassiveMegaMachine('input.txt')

    for instruction_index, replace_to, value in default_machine.get_instruction_replacements(['nop', 'jmp'], instruction_replace_map):
        machine = MyMassiveMegaMachine('input.txt')
        machine.instructions[instruction_index] = (replace_to, value)
        finished_successfully = machine.run_until_exit()
        if finished_successfully:
            break
        
    print(machine.current_value)


if __name__ == "__main__":
    solve()