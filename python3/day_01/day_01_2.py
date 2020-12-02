def solve():
    with open('input.txt') as f:
        numbers = set([int(n) for n in f.readlines()])
    number_a, number_b, number_c = get_matching_triple(numbers, 2020)
    print(number_a * number_b * number_c)


def get_matching_triple(numbers, total):
    total_pairs = {a + b: (a, b) for a in numbers for b in numbers}
    for number in numbers:
        target = total - number
        if target in total_pairs:
            return (number, *total_pairs[target])
    raise ValueError('Matching triple not found.')


if __name__ == "__main__":
    solve()