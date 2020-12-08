from collections import defaultdict
from typing import Set, Tuple, Dict, List, Optional


def solve():
    bag_owners = defaultdict(set)

    with open('input.txt') as f:
        for line in f:
            outside_bag, inside_bags = parse_line(line)
            for bag in inside_bags:
                bag_owners[bag].add(outside_bag)
        
    possible_bags = get_possible_outside_bags(bag_owners, 'shiny gold')
    print(possible_bags)
    print(len(possible_bags))


def parse_line(line: str) -> Tuple[str, List[str]]:
    line = line.rstrip('.\n')
    line_split = line.split(" bags contain ")
    outside_bag = line_split[0]
    inside_bags = []
    for inside_bag_str in line_split[1].split(", "):
        if inside_bag_str == "no other bags":
            break
        inside_bags.append(get_bag_name_from_str(inside_bag_str))
    return outside_bag, inside_bags


def get_bag_name_from_str(bag_str: str) -> str:
    return " ".join(bag_str.split()[1:3])


def get_possible_outside_bags(bag_owners: Dict[str, Set[str]], inside_bag: str):
    bags = _get_possible_outside_bags(bag_owners, inside_bag)
    bags -= {inside_bag}
    return bags
    

def _get_possible_outside_bags(bag_owners: Dict[str, Set[str]], inside_bag: str, found_bags: Optional[Set[str]] = None) -> Set[str]:
    if not found_bags:
        found_bags = set()
    if inside_bag in found_bags:
        return
    found_bags.add(inside_bag)
    outside_bags = bag_owners.get(inside_bag, set())
    for bag in outside_bags:
        _get_possible_outside_bags(bag_owners, bag, found_bags)
    return found_bags


if __name__ == "__main__":
    solve()