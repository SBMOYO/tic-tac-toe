class Board:
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player

    def draw_board(self):
        possible_positions = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        board_structure = """
         _______ _______ _______ 

        |   {}   |   {}   |   {}   |
         _______ _______ _______ 

        |   {}   |   {}   |   {}   |
         _______ _______ _______ 

        |   {}   |   {}   |   {}   |
         _______ _______ _______ 
        """

        
        result_string = board_structure.format(possible_positions[0], possible_positions[1],
                                               possible_positions[2], possible_positions[3],
                                               possible_positions[4], possible_positions[5],
                                               possible_positions[6], possible_positions[7],
                                               possible_positions[8])

        print(result_string)

    
board_instance = Board("John", "Mary")
board_instance.draw_board()
