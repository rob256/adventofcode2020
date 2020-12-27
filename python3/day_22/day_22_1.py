from queue import deque


def solve():
    player_1, player_2 = parse_input('input.txt')

    while player_1 and player_2:
        run_round(player_1, player_2)
        
    winner = player_1 or player_2
    
    score = calculate_score(winner)
    print(score)


def parse_input(input_file):
    players = {}
    players[0] = deque([])
    players[1] = deque([])

    with open(input_file) as f:
        lines = [line.strip() for line in f]
    
    player = 0

    for line in lines[1:]:
        if not line:
            continue
        if line.startswith('Player'):
            player = 1
        else:
            players[player].append(int(line))
    
    return players[0], players[1]


def run_round(player_1, player_2):
    p1 = player_1.popleft()
    p2 = player_2.popleft()

    if p1 > p2:
        player_1.append(p1)
        player_1.append(p2)
    else:
        player_2.append(p2)
        player_2.append(p1)


def calculate_score(winner):
    total_score = 0
    for i, card in enumerate(reversed(winner)):
        total_score += (i + 1) * card
    return total_score


if __name__ == "__main__":
    solve()