from player import Player
from units import Unit

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)

    def setup_game(self):
        # Example setup
        player1 = Player("Player1")
        player2 = Player("Player2")

        unit1 = Unit("Soldier1", 100, 10)
        unit2 = Unit("Soldier2", 120, 12)

        player1.add_unit(unit1)
        player2.add_unit(unit2)

        self.add_player(player1)
        self.add_player(player2)

    def start(self):
        # Simplified game loop
        current_round = 1
        while all(player.has_units_alive() for player in self.players):
            print(f"Round: {current_round}")
            for player in self.players:
                print(f"{player.name}'s turn")
                for unit in player.get_alive_units():
                    # Let each unit attack the first alive unit of the opponent
                    opponent = next(p for p in self.players if p != player)
                    target = opponent.get_alive_units()[0]  # Simplification: attack the first unit in the list
                    print(f"{unit} attacks {target}")
                    unit.attack(target)
                    if not target.is_alive():
                        print(f"{target} has fallen!")

            current_round += 1
            print()

        winner = next(player for player in self.players if player.has_units_alive())
        print(f"The winner is {winner.name}!")
