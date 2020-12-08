from collections import defaultdict
from typing import Set, Tuple, Dict, List, Optional


def solve():
    bag_children = defaultdict(list)

    with open('input.txt') as f:
        for line in f:
            outside_bag, inside_bags = parse_line(line)
            bag_children[outside_bag] = inside_bags
    
    bag_count = count_inside_bags(bag_children, 'shiny gold')
    print(bag_count - 1)


def parse_line(line: str) -> Tuple[str, List[str]]:
    line = line.rstrip('.\n')
    line_split = line.split(" bags contain ")
    outside_bag = line_split[0]
    inside_bags = []
    for inside_bag_str in line_split[1].split(", "):
        if inside_bag_str == "no other bags":
            break
        inside_bags.append(get_bag_name_and_count(inside_bag_str))
    return outside_bag, inside_bags


def get_bag_name_and_count(bag_str: str) -> Tuple[int, str]:
    bag_str_parts = bag_str.split()
    return int(bag_str_parts[0]), " ".join(bag_str.split()[1:3])


def count_inside_bags(bag_children: Dict[str, List[str]], outside_bag: str) -> int:
    total_count = 0
    for bag_count, bag in bag_children.get(outside_bag, []):
        total_count = total_count + (bag_count * count_inside_bags(bag_children, bag))
    return total_count + 1

    
if __name__ == "__main__":
    solve()