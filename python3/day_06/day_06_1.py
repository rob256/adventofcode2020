def solve():

    count_sum = 0

    yes_answers = set()

    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                count_sum += len(yes_answers)
                yes_answers = set()
                print(count_sum)
            else:
                yes_answers |= set(line)
    print(count_sum)


if __name__ == "__main__":
    solve()