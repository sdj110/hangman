from Player import Player
from Phrase import Phrase
from random import randint


class MainGame:
    def __init__(self):
        self.player_dict = dict()
        self.num_players = 2
        self.current_player = 0


    #region PLAYER
    def create_players(self):
        for i in range(self.num_players):
            prompt = "Player {} enter your name: ".format(i+1)
            name = input(prompt)
            player = Player(name)
            self.phrase = None
            self.player_dict[i+1] = player

    def get_player(self, key):
        if key not in self.player_dict:
            print("ERROR: Invalid Player Key")
        else:
            return self.player_dict[key]
    
    ## The player currently guessing at the phrase
    def guessing_player(self):
        return self.player_dict[self.current_player]
    
    ## The player who set the current phrase
    def phrase_player(self):
        if self.current_player == 1:
            return self.player_dict[2]
        else:
            return self.player_dict[1]

    def swap_current_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
    #endregion

    #region PHRASE
    def set_phrase(self, phrase):
        self.phrase = Phrase(phrase)

    def get_phrase(self):
        return self.phrase
    #endregion

    def main_loop(self):
        
        close = False
        game_over = False
        round_over = False
        while not close:
            ## create players
            self.create_players()

            ## choose random player to start
            self.current_player = randint(1, self.num_players)

            ## start round 1
            round_num = 1
            while not game_over:
                ## set phrase
                prompt = "{} enter a phrase: ".format(self.phrase_player().get_name())
                phrase = input(prompt)
                self.set_phrase(phrase)

                








            


            
        



if __name__ == '__main__':
    mainGame = MainGame()
    mainGame.main_loop()