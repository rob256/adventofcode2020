

def solve(text_input):
    starting_input = list(map(int, text_input.split(',')))

    last_seen = {}
    counter = 0
    previous_number = None
    for i in range(30000000):
        if i < len(starting_input):
            number = starting_input[i]
        else:
            if previous_number in last_seen:
                number = i - last_seen[previous_number] - 1
            else:
                number = 0
        if previous_number is not None:
            last_seen[previous_number] = i - 1
        previous_number = number
    return number


if __name__ == "__main__":
    # print(solve('0,3,6'))
    # print(solve('1,3,2'))
    # print(solve('2,1,3'))
    print(solve('5,1,9,18,13,8,0'))