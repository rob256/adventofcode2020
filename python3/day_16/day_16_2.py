from typing import Dict, Tuple, List, Set
from collections import defaultdict

Rules = Dict[str, List[Tuple[int, int]]]


def solve():
    rules, my_ticket, nearby_tickets = parse_input('input.txt')
    valid_numbers = get_valid_numbers(rules)
    valid_nearby_tickets = filter_bad_tickets(nearby_tickets, valid_numbers)
    field_order = get_field_order(rules, [my_ticket] + valid_nearby_tickets)
    return_value = 1
    for field, index in field_order.items():
        if field.startswith('departure'):
            print(f'{field} = {my_ticket[index]}')
            return_value *= my_ticket[index]
    print(return_value)


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


def is_valid_ticket(ticket: List[int], valid_numbers: Set[int]) -> bool:
    for value in ticket:
        if value not in valid_numbers:
            return False
    return True


def filter_bad_tickets(nearby_tickets: List[List[int]], valid_numbers: Set[int]) -> int:
    tickets = []
    for ticket in nearby_tickets:
        if is_valid_ticket(ticket, valid_numbers):
            tickets.append(ticket)
    return tickets


def get_valid_numbers_for_rule(rule) -> Set[int]:
    valid_numbers = set()
    for rule_range in rule:
        valid_numbers |= set(range(rule_range[0], rule_range[1] + 1))
    return valid_numbers


def rule_fits_all_tickets(valid_numbers, tickets, index):
    for ticket in tickets:
        if ticket[index] not in valid_numbers:
            return False
    return True


def get_field_order(rules: Rules, tickets: List[List[int]]):
    possible_columns = defaultdict(list)
    ticket_columns = len(tickets[0])
    for rule, rule_ranges in rules.items():
        valid_numbers = get_valid_numbers_for_rule(rule_ranges)
        for i in range(ticket_columns):
            if rule_fits_all_tickets(valid_numbers, tickets, i):
                possible_columns[rule].append(i)
    print(possible_columns)
    found_columns = {}
    changed = True
    while changed:
        changed = False
        for rule, columns in possible_columns.items():
            if len(columns) == 1:
                changed = True
                found_columns[rule] = columns[0]
                found_value = columns[0]
                for rule, columns in possible_columns.items():
                    if found_value in columns:
                        columns.remove(found_value)
    return found_columns

                

if __name__ == "__main__":
    solve()