from collections import Counter


def solve():
    food_list_to_allergens, food_set, allergens_set, food_count = parse_input('input.txt')

    possible_matches = {}

    for food in list(food_set):
        possible_matches[food] = set(allergens_set)
    
    print(f'possible_matches: {possible_matches}')

    for food_list, allergens in food_list_to_allergens:
        print(f'food_list: {food_list}')
        # for food in food_list:
        #     if food in possible_matches:
        #         possible_matches[food] &= allergens
        #     else:
        #         possible_matches[food] = allergens
        missing_food = food_set - set(food_list)
        for food in missing_food:
            possible_matches[food] -= allergens
        print(f'possible_matches: {possible_matches}')
    
    checked = set()

    changed = True
    while changed:
        changed = False
        for k, v in possible_matches.items():
            if len(v) == 1 and k not in checked:
                checked.add(k)
                for k2, v2 in possible_matches.items():
                    if k2 == k:
                        continue
                    if list(v)[0] in v2:
                        possible_matches[k2] -= v
                        changed = True
    
    print(f'possible_matches: {possible_matches}')

    answer = 0
    for k, v in possible_matches.items():
        if len(v) == 0:
            answer += food_count[k]
    
    print(answer)


def parse_input(input_file):
    food_list_to_allergens = []
    food_set = set()
    allergens_set = set()
    food_count = Counter()
    with open(input_file) as f:
        lines = [line.strip() for line in f]
    
    for line in lines:
        food_string, allergens_string = line.split(' (contains ')
        allergens_string = allergens_string.rstrip(')')
        food_list = food_string.split()
        allergens_list = allergens_string.split(', ')
        food_list_to_allergens.append((food_list, set(allergens_list)))
        food_set |= set(food_list)
        allergens_set |= set(allergens_list)
        for food in food_list:
            food_count[food] += 1
    
    return food_list_to_allergens, food_set, allergens_set, food_count


if __name__ == "__main__":
    solve()