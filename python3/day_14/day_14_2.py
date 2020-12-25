from typing import Dict, Tuple, Iterable, List
import re
from itertools import product

Mask = List[int]


def solve():
    static_mask = None
    variable_mask = None
    memory = {}

    with open('input.txt') as f:
        for line in f:
            if line.startswith('mask = '):
                static_mask, variable_mask = get_masks(line)
            else:
                address, value = parse_mem_line(line)
                addresses = get_addresses(address, static_mask, variable_mask)
                for address in addresses:
                    memory[address] = value
    
    print(sum(memory.values()))


def get_masks(line: str) -> Tuple[Mask, Mask]:
    static_mask = []
    variable_mask = []
    mask_string = line.split()[2]
    for i, bit in enumerate(reversed(mask_string)):
        if bit in ['1']:
            static_mask.append(i)
        elif bit == 'X':
            variable_mask.append(i)
    return static_mask, variable_mask


def parse_mem_line(line: str) -> Tuple[int, int]:
    m = re.match('mem\[([0-9]+)\] = (.*)', line)
    return int(m.group(1)), int(m.group(2))


def change_bit(value: int, index: int, new_value: int) -> int:
    mask = 1 << index
    value &= ~mask
    if new_value:
        value |= mask
    return value


def apply_mask(value: int, mask: Dict[int, int]) -> int:
    for position, new_value in mask.items():
        value = change_bit(value, position, new_value)
    return value


def get_permutations(mask: Mask) -> Iterable[Dict[int, int]]:
    for flags in product([0, 1], repeat=len(mask)):
        mask_dict = {}
        for i, flag in enumerate(flags):
            mask_dict[mask[i]] = flag
        yield mask_dict


def get_addresses(address: int, static_mask: Mask, variable_mask:Mask) -> List[int]:
    addresses = []
    for index in static_mask:
        address = change_bit(address, index, 1)

    if not variable_mask:
        return [address]
    
    for mask_dict in get_permutations(variable_mask):
        addresses.append(apply_mask(address, mask_dict))

    return addresses


if __name__ == "__main__":
    solve()