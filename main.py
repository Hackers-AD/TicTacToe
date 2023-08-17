import random
from itertools import permutations

class TicTacToe:
    def __init__(self):
        self.game_sequences = ((1,2,3), (1,4,7), (1,5,9), (2,5,8), (3,6,9), (4,5,6), (7,8,9), (3,5,7))
        self.player_choices = []
        self.computer_choices = []
    def initialize(self):
        print("Choose number from 1 to 9 in your turn.\n")
        for i in range(3):
            for j in range(3):
                print("__", end="\t")
            print("\n")
        self.play_turn()

    def update_display(self):
        for i in range(1, 10):
            if i in self.player_choices + self.computer_choices:
                if i in self.player_choices:
                    print("X", end="\t")
                else:
                    print("O", end="\t")
            else:
                print("__", end="\t")

            if i % 3 == 0:
                print("\n")
    def play_turn(self):
        while True:
            choice = None
            try:
                choice = int(input("\nYour turn: "))
            except Exception as e:
                print("\nIncorrect choice.")
            if choice is not None:
                if not (choice < 1 or choice > 9):
                    if choice not in self.player_choices:
                        if choice not in self.computer_choices:
                            self.player_choices.append(choice)
                            self.update_display()
                            is_game_over = self.game_over()
                            if is_game_over: break

                            print("\nComputer turn: computer is playing... \n")
                            while True:
                                sel_position = random.randint(1, 9)
                                if sel_position not in self.computer_choices + self.player_choices:
                                    self.computer_choices.append(sel_position)
                                    break
                            self.update_display()
                            is_game_over = self.game_over()
                            if is_game_over: break
                        else:
                            print("The position is already chosen by computer.")
                    else:
                        print("The position is already chosen by you.")
                else:
                    print("The chosen number is out of range. Please choose between 1 and 9 inclusive.")

    def game_over(self):
        player_choices_perm = None
        computer_choices_perm = None

        if len(self.player_choices) >= 3:
            player_choices_perm = permutations(self.player_choices, 3)

        if len(self.computer_choices) >=3:
            computer_choices_perm = permutations(self.computer_choices, 3)

        if player_choices_perm:
            for choice in player_choices_perm:
                if choice in self.game_sequences:
                    print("Congratulations! you won the game!!")
                    print(f"\nGaming Sequence = {choice}")
                    return True

        if computer_choices_perm:
            for choice in computer_choices_perm:
                if choice in self.game_sequences:
                    print("Sorry! you lose the game.")
                    return True

        if len(self.player_choices + self.computer_choices) == 9:
            print("Woh! the game is equalizer.")
            return True

        return False

game = TicTacToe()
game.initialize()