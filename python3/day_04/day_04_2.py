
import re


def solve():
    all_entries = {}
    valid_entries = 0
    with open('input.txt') as f:
        for line in f.readlines():
            if line.strip() == "":
                if len(all_entries) > 7 or len(all_entries) == 7 and "cid" not in all_entries:
                    if all_keys_valid(all_entries):
                        valid_entries += 1
                        print(f"valid: {all_entries}")
                    else:
                        print(f"Not valid: {all_entries}")
                all_entries = {}
            else:
                for pair in line.split():
                    k, v = pair.split(':')
                    all_entries[k] = v
    print(valid_entries)


def all_keys_valid(all_keys: dict) -> bool:
    for k, v in all_keys.items():
        if not is_valid(k, v):
            print(f"Not valid {k} = {v}")
            # print("False")
            return False
    return True


def is_valid(key, value):
    # print(f"Checking {key} = {value}")
    if key == "byr":
        value = int(value)
        return 1920 <= value and value <= 2002
    elif key == "iyr":
        value = int(value)
        return 2010 <= value and value <= 2020
    elif key == "eyr":
        value = int(value)
        return 2020 <= value and value <= 2030
    elif key == "hgt":
        if not re.match(r"^[0-9]+cm$", value) and not re.match(r"^[0-9]+in$", value):
            return False
        if value[-2:] == "cm":
            value = int(value[:-2])
            return 150 <= value and value <= 193
        elif value[-2:] == "in":
            value = int(value[:-2])
            return 59 <= value and value <= 76
    elif key == "hcl":
        return re.match(r"^#[0-9a-f]{6}$", value)
    elif key == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif key == "pid":
        return re.match(r"^[0-9]{9}$", value)
    elif key == "cid":
        return True
    return False


if __name__ == "__main__":
    solve()