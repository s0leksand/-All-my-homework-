import random


class Board:
    def __init__(self):
        self.board_selections = [["⃞️" for _ in range(10)] for _ in range(10)]
        self.letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.boats_location = set()

    def draw_board(self):
        print("    1   2   3   4   5   6   7   8   9   10")

        for i in range(len(self.board_selections)):
            print(self.letters_list[i], end="\t")
            for j in range(len(self.board_selections[0])):
                print(self.board_selections[i][j], end="\t")
            print()


def boat_check(y, x, boat_location_check):
    for i in range(3):
        boat_location_check.add(f'{[y - 1, x - 1 + i]}')
        boat_location_check.add(f'{[y, x + 1 - i]}')
        boat_location_check.add(f'{[y + 1, x - 1 + i]}')
    return boat_location_check