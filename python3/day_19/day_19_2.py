import re
from itertools import product
from typing import Dict, List, Tuple


def solve():
    rules, messages = parse_input('input.txt')
    message_regex = get_regex(rules, "0")
    match_count = 0
    for message in messages:
        if re.fullmatch(message_regex, message):
            match_count += 1
    print(match_count)


def get_regex(rules, rule):

    if rule in ['"a"', '"b"']:
        return rule.replace('"', '')
    
    if rule == '8':
        return '(' + get_regex(rules, '42') + ')+'
    
    if rule == '11':
        return '(' + '|'.join(get_regex(rules, '42') * n + get_regex(rules, '31') * n for n in range(1, 10)) + ')'

    rule_string = rules[rule]
    rule_parts = rule_string.split(' | ')

    rule_part_regexes = []

    for rule_part in rule_parts:
        rule_part_regex = ''
        for rule_number in rule_part.split():
            rule_part_regex += get_regex(rules, rule_number)
        rule_part_regexes.append(rule_part_regex)
        
    return '(' + '|'.join(rule_part_regexes) + ')'


def parse_input(input_file: str) -> Tuple[Dict[int, str], List[str]]:
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    
    rules = {}
    messages = []
    
    for line in lines:
        if ':' in line:
            rule_number, rule = line.split(': ')
            rules[rule_number] = rule
        elif line:
            messages.append(line)
    
    return rules, messages


if __name__ == "__main__":
    solve()