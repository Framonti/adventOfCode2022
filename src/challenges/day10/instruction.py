class Instruction:
    def __init__(self, raw_instruction: str):
        if raw_instruction.startswith('noop'):
            self.instruction = 'noop'
        else:
            self.instruction = 'add'
            split_instruction = raw_instruction.split(' ')
            self.value = int(split_instruction[1])

