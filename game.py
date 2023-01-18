from copy import deepcopy
import random
import node
import math
import pygame
import sys

#player1 = 1
#player2 = -1

inf = math.inf
pit_A_rect = pygame.Rect(128, 550, 30, 30)
pit_B_rect = pygame.Rect(226, 550, 30, 30)
pit_C_rect = pygame.Rect(326, 550, 30, 30)
pit_D_rect = pygame.Rect(426, 550, 30, 30)
pit_E_rect = pygame.Rect(526, 550, 30, 30)
pit_F_rect = pygame.Rect(626, 550, 30, 30)
 

class play:
    def __init__(self,human_side, who_starts):
        self.human_side = human_side
        self.computer_side = -human_side
        self.player_turn = who_starts
        self.game = node.Game(self.computer_side, self.player_turn)
        if human_side == 1:
            self.human_fosses = {   97: "A",
                                    98: "B",
                                    99: "C",
                                   100: "D",
                                   101: "E",
                                   102: "F"
                                   }
            self.computer_fosses = {103: "G",
                                    104: "H",
                                    105: "I",
                                    106: "J",
                                    107: "K",
                                    108: "L"
                                    }
        else:
            self.computer_fosses = {97: "A",
                                    98: "B",
                                    99: "C",
                                   100: "D",
                                   101: "E",
                                   102: "F"
                                   }
            self.human_fosses = {   103: "G",
                                    104: "H",
                                    105: "I",
                                    106: "J",
                                    107: "K",
                                    108: "L"
                                    }
    
    def humanTurn(self,human):
        
        print('your turn')
        
        # #make a random move from the possible moves
        # random_move = random.choice(self.game.state.possibleMoves())
        # self.player_turn = self.game.state.doMove(random_move)
        # print("your move: " + str(random_move))
        # return random_move

        if not human:
            #cas de computer vs computer
            _, bestPit = self.MinMaxalphabeta2(self.game, self.player_turn, 8, -inf, inf)
            print("computer2's move: " + str(bestPit))
            self.player_turn = self.game.state.doMove(bestPit)
            return bestPit
        
        else:
            #listen to the keyboard and make the move
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        if pit_A_rect.collidepoint(pygame.mouse.get_pos()) or pit_B_rect.collidepoint(pygame.mouse.get_pos()) or pit_C_rect.collidepoint(pygame.mouse.get_pos()) or pit_D_rect.collidepoint(pygame.mouse.get_pos()) or pit_E_rect.collidepoint(pygame.mouse.get_pos()) or pit_F_rect.collidepoint(pygame.mouse.get_pos()):
                            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                        else:
                            pygame.mouse.set_cursor(*pygame.cursors.arrow)
                        # if the mouse is clicked on the pit then make the move
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pit_A_rect.collidepoint(pygame.mouse.get_pos()):
                            print("Your move: A")
                            self.player_turn = self.game.state.doMove("A")
                            return "A"
                        if pit_B_rect.collidepoint(pygame.mouse.get_pos()):
                            print("Your move: B")
                            self.player_turn = self.game.state.doMove("B")
                            return "B"
                        if pit_C_rect.collidepoint(pygame.mouse.get_pos()):
                            print("Your move: C")
                            self.player_turn = self.game.state.doMove("C")
                            return "C"
                        if pit_D_rect.collidepoint(pygame.mouse.get_pos()):
                            print("Your move: D")
                            self.player_turn = self.game.state.doMove("D")
                            return "D"
                        if pit_E_rect.collidepoint(pygame.mouse.get_pos()):
                            print("Your move: E")
                            self.player_turn = self.game.state.doMove("E")
                            return "E"
                        if pit_F_rect.collidepoint(pygame.mouse.get_pos()):
                            print("Your move: F")
                            self.player_turn = self.game.state.doMove("F")
                            return "F"
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key in self.human_fosses:
                            print(f"Your move: {self.human_fosses[event.key]}")
                            self.player_turn = self.game.state.doMove(self.human_fosses[event.key])
                            return self.human_fosses[event.key]
        
    def computerTurn(self):
        print('computer turn')
        # _,bestPit= self.NegaMaxAlphaBetaPruning(self.game, self.player_turn, 8, -inf, inf)
        # _,bestPit= self.MinMax(self.game, self.player_turn, 2)
        _, bestPit = self.MinMaxalphabeta(self.game, self.player_turn, 9, -inf, inf, None)
        print("Computer's move: " + str(bestPit))
        self.player_turn = self.game.state.doMove(bestPit)
        return bestPit


    def MinMaxalphabeta2(self, game, player_turn, depth, alpha, beta):
        if game.gameOver() or depth == 0:
            bestValue = game.evaluate2()
            bestPit = None
            if player_turn == self.computer_side:
                bestValue = -bestValue
            return bestValue, bestPit

        if player_turn == self.human_side:
            bestValue = float("-inf")
            bestPit = None
            for pit in game.state.possibleMoves():
                child_game = deepcopy(game)
                player_turn = child_game.state.doMove(pit)
                value, _ = self.MinMaxalphabeta2(child_game, player_turn, depth-1, alpha, beta)
                if value > bestValue:
                    bestValue = value
                    bestPit = pit
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    break
            return bestValue, bestPit

        else:
            bestValue = float("inf")
            bestPit = None
            for pit in game.state.possibleMoves():
                child_game = deepcopy(game)
                player_turn = child_game.state.doMove(pit)
                value, _ = self.MinMaxalphabeta2(child_game, player_turn, depth-1, alpha, beta)
                if value < bestValue:
                    bestValue = value
                    bestPit = pit
                beta = min(beta, bestValue)
                if beta <= alpha:
                    break
            return bestValue, bestPit
    

    def MinMaxalphabeta(self, game, player_turn, depth, alpha, beta, piit):
        if game.gameOver() or depth == 0:
            bestValue = game.evaluate(piit)
            bestPit = None
            if player_turn == self.human_side:
                bestValue = -bestValue
            return bestValue, bestPit

        if player_turn == self.computer_side:
            bestValue = float("-inf")
            bestPit = None
            for pit in game.state.possibleMoves():
                child_game = deepcopy(game)
                player_turn = child_game.state.doMove(pit)
                value, _ = self.MinMaxalphabeta(child_game, player_turn, depth-1, alpha, beta, pit)
                if value > bestValue:
                    bestValue = value
                    bestPit = pit
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    break
            return bestValue, bestPit

        else:
            bestValue = float("inf")
            bestPit = None
            for pit in game.state.possibleMoves():
                child_game = deepcopy(game)
                player_turn = child_game.state.doMove(pit)
                value, _ = self.MinMaxalphabeta(child_game, player_turn, depth-1, alpha, beta, pit)
                if value < bestValue:
                    bestValue = value
                    bestPit = pit
                beta = min(beta, bestValue)
                if beta <= alpha:
                    break
            return bestValue, bestPit



    def play(self,ishuman):
        # create a window
        pygame.init()
        # clock
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mancala")
        #draw the mancala board on the screen with the initial state
        self.game.draw(screen)
        pygame.display.update()
        clock.tick(200)
        
        # main loop
        cpt = 0
        running = True
        while running:
            if self.player_turn == self.computer_side and not self.game.gameOver():
                last_move = self.computerTurn()
                self.game.draw(screen, last_move)
                pygame.display.flip()
                if self.game.gameOver():
                    running = False
                self.game.draw(screen, last_move)
                pygame.display.flip()
                
            if self.player_turn == self.human_side and not self.game.gameOver():
                cpt += 1
                last_move = self.humanTurn(ishuman)
                self.game.draw(screen, last_move)
                pygame.display.flip()
                if self.game.gameOver():
                    running = False
                self.game.draw(screen, last_move)
                pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        
                        
        result, score = self.game.findWinner()
        
        if result == self.human_side:
            string1 = "Congratulations you have won !!!"
        elif result == self.computer_side:
            string1 ="Hard luck the computer have won"
        else:
            string1 ="A draw"
        string2 = f" with a score of {score} and {cpt} turns"

        self.game.draw(screen, True, string1, string2)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(200)
        
        running = True
        while running:
            for event in pygame.event.get():
                        
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                                       
if __name__ == "__main__":
    game = play(1, -1)  # le premier parametre: '1' pour dire human plays as 'player 1'  sinon '-1' 
                        # et le deuxieme parametre: '1' pour player 1 etre le premier qui joue sinon '-1'
                        
    game.play(False)    # Flase for computer vs computer 
                        # True for computer vs human
