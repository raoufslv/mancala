import mancala

#player1 = 1
#player2 = -1


class Game:
    def __init__(self, computer_side, player_turn):
        self.state = mancala.MancalaBoard(player_turn, computer_side)
        self.computer_side = computer_side

    def gameOver(self):
        boolean = True
        for fose in self.state.player1_fosses:
            if self.state.board_dictionnaire[fose] > 0:
                boolean = False
                break
        if boolean:
            for fose in self.state.player2_fosses:
                self.state.board_dictionnaire["2"] += self.state.board_dictionnaire[fose]
                self.state.board_dictionnaire[fose] = 0
            return True
        else:
            boolean = True
            for fose in self.state.player2_fosses:
                if self.state.board_dictionnaire[fose] > 0:
                    boolean = False
                    break
            if boolean:
                for fose in self.state.player1_fosses:
                    self.state.board_dictionnaire["1"] += self.state.board_dictionnaire[fose]
                    self.state.board_dictionnaire[fose] = 0
                return True
            else:
                return False

    def findWinner(self):
        if self.state.board_dictionnaire["1"] > self.state.board_dictionnaire["2"]:
            return 1, self.state.board_dictionnaire["1"]
        elif self.state.board_dictionnaire["1"] < self.state.board_dictionnaire["2"]:
            return -1, self.state.board_dictionnaire["2"]
        else:
            return 0, self.state.board_dictionnaire["1"]

    
    def draw(self, screen, last_move="", gameOver=False, winner="", score=""):
        self.state.draw(screen, last_move, gameOver, winner, score)

    def evaluate(self, piit):
        c = 0
        if self.computer_side == -1:
            c += self.state.board_dictionnaire["2"] - \
                self.state.board_dictionnaire["1"]
        else:
            c += self.state.board_dictionnaire["1"] - \
                self.state.board_dictionnaire["2"]
        return 2*c + self.heuristic_Collector_Plus() - self.heuristic_Collector_Minus() + 3*self.heuristic_check_opposite(piit) + 4*self.heuristic_check_Play_Again(piit)
    
    def evaluate2(self):
        c = 0
        if self.computer_side == 1:
            c += self.state.board_dictionnaire["2"] - \
                self.state.board_dictionnaire["1"]
        else:
            c += self.state.board_dictionnaire["1"] - \
                self.state.board_dictionnaire["2"]
                
        return c- self.heuristic_Collector_Plus() + self.heuristic_Collector_Minus()
    
    # make the opponent have more 0
    def heuristic_Collector_Plus(self):
        # return the number of empty fosses on the human side
        c = 0
        if self.computer_side == -1:
            for fose in self.state.player1_fosses:
                if self.state.board_dictionnaire[fose] == 0:
                    c += 1
        else:
            for fose in self.state.player2_fosses:
                if self.state.board_dictionnaire[fose] == 0:
                    c += 1
        if c == 7:  # if all he fosses are empty on the human side then the computer collects all the seeds on the computer side
            # return the number of seeds on each fose on the computer side
            z = 0
            if self.computer_side == 1:
                for fose in self.state.player2_fosses:
                    z += self.state.board_dictionnaire[fose]
            else:
                for fose in self.state.player1_fosses:
                    z += self.state.board_dictionnaire[fose]
            return z
        else:
            return 0

    #try to have less zeros
    def heuristic_Collector_Minus(self):
        # return the number of empty fosses on the human side
        c = 0
        if self.computer_side == 1:
            for fose in self.state.player1_fosses:
                if self.state.board_dictionnaire[fose] == 0:
                    c += 1
        else:
            for fose in self.state.player2_fosses:
                if self.state.board_dictionnaire[fose] == 0:
                    c += 1
        if c == 7:  # if all he fosses are empty on the human side then the computer collects all the seeds on the computer side
            # return the number of seeds on each fose on the computer side
            z = 0
            if self.computer_side == -1:
                for fose in self.state.player2_fosses:
                    z += self.state.board_dictionnaire[fose]
            else:
                for fose in self.state.player1_fosses:
                    z += self.state.board_dictionnaire[fose]
            return z
        else:
            return 0

    # if can play again
    def heuristic_check_Play_Again(self, piit):
        # check if there is a possible move that leads to make the computer play again
        c = 0
        if self.state.player_turn == self.computer_side:
            # see if the last seed of the move will be in the computer's store
            # if the number of seeds in the move is equal to the distance between the fose and the store then the last seed will be in the store
            if self.state.board_dictionnaire[piit] == self.state.dictionnaire_fosse_distance_magasin[piit]:
                c += 1
        return c
    
    # if fose make u take opposite fose
    def heuristic_check_opposite(self, piit):
        # check if there is a possible move that the last sead will be in an empty fosse of computer's side
        c = 0
        fose = None
        if self.state.player_turn == self.computer_side:
            for i in range(self.state.board_dictionnaire[piit]):
                fose = self.state.dictionnaire_fosse_suivante[piit]

            if self.computer_side == 1 and fose in self.state.player1_fosses or self.computer_side == -1 and fose in self.state.player2_fosses:
                if self.state.board_dictionnaire[fose] == 0:
                    if self.state.board_dictionnaire[self.state.dictionnaire_fosse_opposee[fose]]+1 > c:
                        c = self.state.board_dictionnaire[self.state.dictionnaire_fosse_opposee[fose]]+1
                        
        return c




    # number of fosses that make u play again
    def heuristic_Check_number_Play_Again(self):
        # check if there is a possible move that leads to make the computer play again
        c = 0
        if self.state.player_turn == self.computer_side:
            moves = self.state.possibleMoves()
            for move in moves:
                # see if the last seed of the move will be in the computer's store
                # if the number of seeds in the move is equal to the distance between the fose and the store then the last seed will be in the store
                if self.state.board_dictionnaire[move] == self.state.dictionnaire_fosse_distance_magasin[move]:
                    c += 1
        return c

    # number of fosses that make u take opposite fose
    def heuristic_check_number_opposite(self):
        # check if there is a possible move that the last sead will be in an empty fosse of computer's side
        c = 0
        if self.state.player_turn == self.computer_side:
            moves = self.state.possibleMoves()
            for move in moves:
                for i in range(self.state.board_dictionnaire[move]):
                    fose = self.state.dictionnaire_fosse_suivante[move]

                if self.computer_side == 1 and fose in self.state.player1_fosses or self.computer_side == -1 and fose in self.state.player2_fosses:
                    if self.state.board_dictionnaire[fose] == 0:
                        if self.state.board_dictionnaire[self.state.dictionnaire_fosse_opposee[fose]]+1 > c:
                            c = self.state.board_dictionnaire[self.state.dictionnaire_fosse_opposee[fose]]+1

        return c


    # for the second computer (computer vs computer)
    def heuristic_Check_number_Play_Again2(self):
        # check if there is a possible move that leads to make the computer play again
        c = 0
        if self.state.player_turn == -self.computer_side:
            moves = self.state.possibleMoves()
            for move in moves:
                # see if the last seed of the move will be in the computer's store
                # if the number of seeds in the move is equal to the distance between the fose and the store then the last seed will be in the store
                if self.state.board_dictionnaire[move] == self.state.dictionnaire_fosse_distance_magasin[move]:
                    c += 1
        return c

    def heuristic_check_number_opposite2(self):
        # check if there is a possible move that the last sead will be in an empty fosse of computer's side
        c = 0
        if self.state.player_turn == -self.computer_side:
            moves = self.state.possibleMoves()
            for move in moves:
                for i in range(self.state.board_dictionnaire[move]):
                    fose = self.state.dictionnaire_fosse_suivante[move]

                if self.computer_side == -1 and fose in self.state.player1_fosses or self.computer_side == 1 and fose in self.state.player2_fosses:
                    if self.state.board_dictionnaire[fose] == 0:
                        if self.state.board_dictionnaire[self.state.dictionnaire_fosse_opposee[fose]]+1 > c:
                            c = self.state.board_dictionnaire[self.state.dictionnaire_fosse_opposee[fose]]+1

        return c

