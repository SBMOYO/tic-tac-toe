class Player:
    def __init__(self, player_name, player_symbol):
        self.player_name = player_name
        self.player_symbol = player_symbol 

    def get_name(self):
        return self.player_name
    
    def get_symbol(self):
        return self.player_symbol
    


""" player_1 = Player("Sungano", "X")
player_2 = Player("lyn", "O")

print(player_2.get_name())
print(player_2.get_symbol()) """
