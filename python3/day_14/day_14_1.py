from typing import Dict, Tuple
import re


def solve():
    current_mask = None
    memory = {}

    with open('input.txt') as f:
        for line in f:
            if line.startswith('mask = '):
                current_mask = get_mask(line)
            else:
                address, value = parse_mem_line(line)
                memory[address] = apply_mask(value, current_mask)
    
    print(sum(memory.values()))


def get_mask(line: str) -> Dict[int, int]:
    mask = {}
    mask_string = line.split()[2]
    for i, bit in enumerate(reversed(mask_string)):
        if bit in ['0', '1']:
            mask[i] = int(bit)
    return mask


def parse_mem_line(line: str) -> Tuple[int, int]:
    m = re.match('mem\[([0-9]+)\] = (.*)', line)
    return int(m.group(1)), int(m.group(2))


def apply_mask(value: int, mask: Dict[int, int]) -> int:
    for position, new_value in mask.items():
        value = change_bit(value, position, new_value)
    return value


def change_bit(value: int, index: int, new_value: int) -> int:
    mask = 1 << index
    value &= ~mask
    if new_value:
        value |= mask
    return value


if __name__ == "__main__":
    solve()