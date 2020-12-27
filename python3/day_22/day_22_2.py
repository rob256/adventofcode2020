from queue import deque


GAME_ID = 0


def solve():
    player_1, player_2 = parse_input('input.txt')

    winner, winner_number = play_game(player_1, player_2)

    
    score = calculate_score(winner)
    print(score)


def play_game(player_1, player_2, cache={}):
    global GAME_ID
    GAME_ID = GAME_ID + 1
    game_id = GAME_ID

    p1_max = max(player_1)
    p2_max = max(player_2)

    if game_id != 1:
        if p1_max > p2_max:
            return [], 1
        # elif p2_max > p1_max:
        #     return [], 2

    rounds_cache1 = set()
    rounds_cache2 = set()

    game_tuple = (tuple(player_1), tuple(player_2))
    if game_tuple in cache:
        # print(f'returning cache: {game_tuple}')
        return cache[game_tuple]

    # print(f'Playing game {game_id}: {player_1} vs {player_2}')
    
    while player_1 and player_2:
        run_round(player_1, player_2, game_id=game_id, previous_rounds1=rounds_cache1, previous_rounds2=rounds_cache2)
    
    if player_1:
        winner_number = 1
    else:
        winner_number = 2
    
    winner = player_1 or player_2

    cache[game_tuple] = (winner, winner_number)

    # print(f'Winner: {winner_number}')
    return winner, winner_number


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


def run_round(player_1, player_2, game_id=0, previous_rounds1=None, previous_rounds2=None):
    p1_tuple = tuple(player_1)
    p2_tuple = tuple(player_2)

    p1 = player_1.popleft()
    p2 = player_2.popleft()

    if p1_tuple in previous_rounds1 or p2_tuple in previous_rounds2:
        # print('Previously seen, winner 1')
        winner_number = 1

    elif p1 <= len(player_1) and p2 <= len(player_2):
        _, winner_number = play_game(deque(list(player_1)[:p1]), deque(list(player_2)[:p2]))
    elif p1 > p2:
        winner_number = 1
    else:
        winner_number = 2
    
    previous_rounds1.add(p1_tuple)
    previous_rounds2.add(p2_tuple)
    
    if winner_number == 1:
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
    # print(calculate_score([36, 12, 23, 7, 49, 47, 38, 10, 46, 28, 18, 6, 35, 3, 33, 26, 32, 20, 48, 34, 40, 8, 30, 15, 14, 2, 45, 24, 41, 21, 50, 42, 31, 25, 39, 22, 37, 29, 19, 5, 16, 1, 44, 9, 27, 4, 43, 17, 13, 11]))