from sys import stdin

def match(new_player_list):
    new_list = []
    loser = -1
    for match in zip(*[iter(new_player_list)]*2):
        winner = max(match)
        loser = min(match)
        new_list.append(winner)

    return loser, new_list

if __name__ == "__main__":

    n = int(input())
    original_player_list = list(map(int, input().split()))

    new_player_list = original_player_list[:]
    loser = 0

    while len(new_player_list) != 1:
        loser, new_player_list = match(new_player_list)

    print(original_player_list.index(loser) + 1)
