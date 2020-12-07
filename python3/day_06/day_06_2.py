from collections import Counter

def solve():

    count_sum = 0
    answer_count = 0

    yes_answers = []

    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                yes_counter = Counter(yes_answers)
                for k, v in yes_counter.items():
                    print(f"k: {k}")
                    print(f"v: {v}")
                    if v == answer_count:
                        count_sum += 1
                yes_answers = []
                answer_count = 0
                print(count_sum)
            else:
                yes_answers.extend(list(line))
                answer_count += 1
    print(count_sum)


if __name__ == "__main__":
    solve()