from typing import Dict, Tuple, List, Set

Rules = Dict[str, List[Tuple[int, int]]]


def solve():
    rules, my_ticket, nearby_tickets = parse_input('input.txt')
    valid_numbers = get_valid_numbers(rules)
    error_rate = get_error_rate(valid_numbers, nearby_tickets)
    print(error_rate)


def parse_input(input_file: str) -> Tuple[Rules, List[int], List[List[int]]]:
    rules = {}
    my_ticket = None
    nearby_tickets = []
    with open(input_file) as f:
        for line in f:
            if not line.strip():
                continue
            if line.startswith('your ticket:'):
                break
            rule_name, rules_string = line.split(': ')
            rule1_string, rule2_string = rules_string.split(' or ')
            rule1 = rule1_string.split('-')
            rule2 = rule2_string.split('-')
            rules[rule_name] = [(int(rule1[0]), int(rule1[1])), (int(rule2[0]), int(rule2[1]))]
        for line in f:
            if not line.strip():
                continue
            if line.startswith('nearby tickets:'):
                break
            my_ticket = list(map(int, line.split(',')))
        for line in f:
            if not line.strip():
                continue
            nearby_tickets.append(list(map(int, line.split(','))))
    return rules, my_ticket, nearby_tickets
            

def get_valid_numbers(rules: Rules) -> Set[int]:
    valid_numbers = set()
    for rule_ranges in rules.values():
        for rule_range in rule_ranges:
            valid_numbers |= set(range(rule_range[0], rule_range[1] + 1))
    return valid_numbers


def get_error_rate(valid_numbers: Set[int], nearby_tickets: List[List[int]]) -> int:
    error_rate = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if value not in valid_numbers:
                error_rate += value
    return error_rate


if __name__ == "__main__":
    solve()