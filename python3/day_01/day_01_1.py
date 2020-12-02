def solve():
    with open('input.txt') as f:
        numbers = set([int(n) for n in f.readlines()])
    number_a, number_b = get_matching_pair(numbers, 2020)
    print(number_a * number_b)


def get_matching_pair(numbers, total):
    for number in numbers:
        target = total - number
        if target in numbers:
            return (number, target)
    raise ValueError('Matching pair not found.')


if __name__ == "__main__":
    solve()