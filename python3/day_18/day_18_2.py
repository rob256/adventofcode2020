import re


def solve(expression, skip_checks=False) -> int:
    print(f'exp: {expression}')
    if not skip_checks:
        while '(' in expression:
            m = re.match('.*\(([^()]+)\).*', expression)
            sub_expression = m.group(1)
            sub_value = solve(sub_expression)
            expression = expression.replace(f'({sub_expression})', str(sub_value))
        while '+' in expression:
            m = re.findall('[0-9]+ \+ [0-9]+', expression)
            sub_expression = m[0]
            sub_value = solve(sub_expression, skip_checks=True)
            print(f'a: {expression}')
            expression = expression.replace(f'{sub_expression}', str(sub_value), 1)
            print(f'b: {expression}')
    parts = expression.split()
    value = int(parts[0])
    i = 1
    while i < len(parts):
        op = parts[i]
        number = int(parts[i + 1])
        i += 2
        if op == '+':
            value += number
        elif op == '*':
            value *= number
    return value


def solve_input():
    expressions = []
    with open('input.txt') as f:
        for line in f:
            expressions.append(line.strip())
    
    total = 0
    for expression in expressions:
        total += solve(expression)
    
    print(total)
        


if __name__ == "__main__":
    print(solve('2 * 3 + (4 * 5)'))
    print(solve('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
    print(solve('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
    print(solve('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))
    solve_input()