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


