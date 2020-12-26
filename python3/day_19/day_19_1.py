import re
from itertools import product
from typing import Dict, List, Tuple


def solve():
    rules, messages = parse_input('input.txt')
    allowed_messages = set(get_allowed_messages(rules, 0))
    # print(allowed_messages)

    count = 0
    for message in messages:
        if message in allowed_messages:
            count += 1
    
    print(count)


def get_allowed_messages(rules, rule, cache={}):
    # print(f'Finding rule: {rule}')
    if rule in cache:
        # print('returning cache')
        return cache[rule]
    
    if rules[rule] in ['"a"', '"b"']:
        cache[rule] = [rules[rule].replace('"', '')]
        return cache[rule]
        

    messages = []

    rule_parts = rules[rule].split(' | ')
    
    print(f'{rule}: {rule_parts}')

    for rule_part in rule_parts:
        rule_messages = []
        rule_ints = [int(x) for x in rule_part.split()]
        # print(f'rule ints: {rule_ints}')
        for rule_int in rule_ints:
            # a = get_allowed_messages(rules, rule_int)
            # print(f'a: {a}')
            rule_messages.append(get_allowed_messages(rules, rule_int))
        # print(f'x {rule}: {rule_messages}')
        messages.extend([''.join(x) for x in product(*rule_messages)])
    
    cache[rule] = messages
    return cache[rule]


def parse_input(input_file: str) -> Tuple[Dict[int, str], List[str]]:
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    
    rules = {}
    messages = []
    
    for line in lines:
        if ':' in line:
            rule_number, rule = line.split(': ')
            rule_number = int(rule_number)
            rules[rule_number] = rule
        elif line:
            messages.append(line)
    
    return rules, messages


    

if __name__ == "__main__":
    solve()