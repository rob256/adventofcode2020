def solve():
    all_entries = {}
    valid_entries = 0
    with open('input.txt') as f:
        for line in f.readlines():
            print(f'{line}')
            if line.strip() == "":
                if len(all_entries) > 7 or len(all_entries) == 7 and "cid" not in all_entries:
                    valid_entries += 1
                all_entries = {}
            else:
                for pair in line.split():
                    k, v = pair.split(':')
                    all_entries[k] = v
    print(valid_entries)


if __name__ == "__main__":
    solve()