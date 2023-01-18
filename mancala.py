import pygame
#player1 = 1
#player2 = -1

class MancalaBoard:

    def __init__(self, player_turn, computer_side):
        
        self.player2_fosses = ["L","K","J","I","H","G"]
        self.player1_fosses = ["A","B","C","D","E","F"]
        
        self.dictionnaire_fosse_suivante = {"A":"B", "B":"C", "C":"D", "D":"E", "E":"F", "F":"1", "1":"L", "L":"K", "K":"J", "J":"I", "I":"H", "H":"G", "G":"2", "2":"A"}
        self.dictionnaire_fosse_opposee = {"A":"G", "B":"H", "C":"I", "D":"J", "E":"K", "F":"L", "L":"F", "K":"E", "J":"D", "I":"C", "H":"B", "G":"A"}
        self.dictionnaire_fosse_distance_magasin = {"A":6, "B":5, "C":4, "D":3, "E":2, "F":1, "L":6, "K":5, "J":4, "I":3, "H":2, "G":1}

        self.board_dictionnaire = {"A": 4,
                                   "B": 4,
                                   "C": 4,
                                   "D": 4,
                                   "E": 4,
                                   "F": 4,
                                   "1": 0,
                                   "L": 4,
                                   "K": 4,
                                   "J": 4,
                                   "I": 4,
                                   "H": 4,
                                   "G": 4,
                                   "2": 0
                                   }

        self.player_turn = player_turn
        self.computer_side = computer_side
        
    def possibleMoves(self):
        list = []
        if self.player_turn == 1:
            for fose in self.player1_fosses:
                if self.board_dictionnaire[fose] > 0:
                    list.append(fose)
        else: 
            for fose in self.player2_fosses:
                if self.board_dictionnaire[fose] > 0:
                    list.append(fose)
                
        return list


    def doMove(self, fose):
        
        num_graines = self.board_dictionnaire[fose]
        self.board_dictionnaire[fose] = 0
        
        for i in range(num_graines):
            fose = self.dictionnaire_fosse_suivante[fose]
            if (self.player_turn == 1 and fose == "2") or (self.player_turn == -1 and fose == "1"):
                fose = self.dictionnaire_fosse_suivante[fose]
            self.board_dictionnaire[fose] += 1
            
        if self.board_dictionnaire[fose] == 1:
            
            if self.player_turn == 1:
                if fose in self.player1_fosses:
                    self.board_dictionnaire["1"] += self.board_dictionnaire[self.dictionnaire_fosse_opposee[fose]] + 1
                    self.board_dictionnaire[self.dictionnaire_fosse_opposee[fose]] = 0
                    self.board_dictionnaire[fose] = 0
            else:
                if fose in self.player2_fosses:
                    self.board_dictionnaire["2"] += self.board_dictionnaire[self.dictionnaire_fosse_opposee[fose]] + 1
                    self.board_dictionnaire[self.dictionnaire_fosse_opposee[fose]] = 0
                    self.board_dictionnaire[fose] = 0
            
            
        if fose != "1" and fose != "2":
            self.player_turn = -self.player_turn
            
        return self.player_turn
    
    def draw(self, screen, last_move="", gameOver = False, winner = "", score= ""):
        screen.fill('#B47A45')
        # draw the six round pits for player 1 in a row at the bottom of the screen and on it's right side draw the store with a rectangle form and the other six pits for player 2 in a row at the top of the screen and on it's left side draw the store with a rectangle form
        # draw the six round pits for player 1 in a row at the bottom of the screen
        pygame.draw.circle(screen, '#C4C0BD', (140, 500), 45)
        pygame.draw.circle(screen, '#C4C0BD', (240, 500), 45)
        pygame.draw.circle(screen, '#C4C0BD', (340, 500), 45)
        pygame.draw.circle(screen, '#C4C0BD', (440, 500), 45)
        pygame.draw.circle(screen, '#C4C0BD', (540, 500), 45)
        pygame.draw.circle(screen, '#C4C0BD', (640, 500), 45)
        # draw the store with a rectangle form with radius 45
        # pygame.draw.rect(screen, '#C4C0BD', (650, 200, 100, 200), 0, 45)

        pygame.draw.rect(screen, '#C4C0BD', (650, 200, 100, 200), 0, 45)
        # draw the six round pits for player 2 in a row at the top of the screen
        pygame.draw.circle(screen, '#C4C0BD', (140, 100), 45)
        pygame.draw.circle(screen, '#C4C0BD', (240, 100), 45)
        pygame.draw.circle(screen, '#C4C0BD', (340, 100), 45)
        pygame.draw.circle(screen, '#C4C0BD', (440, 100), 45)
        pygame.draw.circle(screen, '#C4C0BD', (540, 100), 45)
        pygame.draw.circle(screen, '#C4C0BD', (640, 100), 45)
        # draw the store with a rectangle form
        pygame.draw.rect(screen, '#C4C0BD', (50, 200, 100, 200), 0, 45)
        
        
        
        
            
        
        
        
        if last_move!="":
            match last_move:
                case "A":
                    pygame.draw.circle(screen, '#f99999', (140, 500), 45)
                case "B":
                    pygame.draw.circle(screen, '#f99999', (240, 500), 45)
                case "C":
                    pygame.draw.circle(screen, '#f99999', (340, 500), 45)
                case "D":
                    pygame.draw.circle(screen, '#f99999', (440, 500), 45)
                case "E":
                    pygame.draw.circle(screen, '#f99999', (540, 500), 45)
                case "F":
                    pygame.draw.circle(screen, '#f99999', (640, 500), 45)
                case "G":
                    pygame.draw.circle(screen, '#f99999', (140, 100), 45)
                case "H":
                    pygame.draw.circle(screen, '#f99999', (240, 100), 45)
                case "I":
                    pygame.draw.circle(screen, '#f99999', (340, 100), 45)
                case "J":
                    pygame.draw.circle(screen, '#f99999', (440, 100), 45)
                case "K":
                    pygame.draw.circle(screen, '#f99999', (540, 100), 45)
                case "L":
                    pygame.draw.circle(screen, '#f99999', (640, 100), 45)
                case _:
                    pass
        
        
        # Draw the number of seeds in each pit
        font = pygame.font.SysFont('Arial', 30)
        font2 = pygame.font.SysFont('Arial', 24)
        
        
        text = font.render(str(self.board_dictionnaire["A"]), True, '#000000')
        screen.blit(text, (135, 480))
        pit_A_rect = pygame.Rect(128, 550, 30, 30)
        pygame.draw.rect(screen, (137, 134, 133), pit_A_rect, 0, 10) # you can change the color as you want
        text = font2.render("A", True, '#000000')
        screen.blit(text, (135, 550))

        text = font.render(str(self.board_dictionnaire["B"]), True, '#000000')
        screen.blit(text, (235, 480))
        pit_B_rect = pygame.Rect(226, 550, 30, 30)
        pygame.draw.rect(screen, (137, 134, 133), pit_B_rect, 0, 10) # you can change the color as you want
        text = font2.render("B", True, '#000000')
        screen.blit(text, (235, 550))

        text = font.render(str(self.board_dictionnaire["C"]), True, '#000000')  
        screen.blit(text, (335, 480))
        pit_C_rect = pygame.Rect(326, 550, 30, 30)
        pygame.draw.rect(screen, (137, 134, 133), pit_C_rect, 0, 10) # you can change the color as you want
        text = font2.render("C", True, '#000000')
        screen.blit(text, (335, 550))

        text = font.render(str(self.board_dictionnaire["D"]), True, '#000000')
        screen.blit(text, (435, 480))
        pit_D_rect = pygame.Rect(426, 550, 30, 30)
        pygame.draw.rect(screen, (137, 134, 133), pit_D_rect, 0, 10) # you can change the color as you want
        text = font2.render("D", True, '#000000')
        screen.blit(text, (435, 550))
        
        text = font.render(str(self.board_dictionnaire["E"]), True, '#000000')
        screen.blit(text, (535, 480))
        pit_E_rect = pygame.Rect(526, 550, 30, 30)
        pygame.draw.rect(screen, (137, 134, 133), pit_E_rect, 0, 10) # you can change the color as you want
        text = font2.render("E", True, '#000000')
        screen.blit(text, (535, 550))
    
        text = font.render(str(self.board_dictionnaire["F"]), True, '#000000')
        screen.blit(text, (635, 480))
        pit_F_rect = pygame.Rect(626, 550, 30, 30)
        pygame.draw.rect(screen, (137, 134, 133), pit_F_rect, 0, 10) # you can change the color as you want
        text = font2.render("F", True, '#000000')
        screen.blit(text, (635, 550))
        
        text = font.render(str(self.board_dictionnaire["1"]), True, '#000000')
        screen.blit(text, (690, 260))
        text = font2.render("Magasin 1", True, '#000000')
        screen.blit(text, (660, 400))
        
        text = font.render(str(self.board_dictionnaire["L"]), True, '#000000')
        screen.blit(text, (635, 80))
        text = font2.render("L", True, '#000000')
        screen.blit(text, (635, 20))

        text = font.render(str(self.board_dictionnaire["K"]), True, '#000000')
        screen.blit(text, (535, 80))
        text = font2.render("K", True, '#000000')
        screen.blit(text, (535, 20))
        
        text = font.render(str(self.board_dictionnaire["J"]), True, '#000000')
        screen.blit(text, (435, 80))
        text = font2.render("J", True, '#000000')
        screen.blit(text, (435, 20))
    
        text = font.render(str(self.board_dictionnaire["I"]), True, '#000000')
        screen.blit(text, (335, 80))
        text = font2.render("I", True, '#000000')
        screen.blit(text, (335, 20))

        text = font.render(str(self.board_dictionnaire["H"]), True, '#000000')
        screen.blit(text, (235, 80))
        text = font2.render("H", True, '#000000')
        screen.blit(text, (235, 20))
        
        text = font.render(str(self.board_dictionnaire["G"]), True, '#000000')
        screen.blit(text, (135, 80))
        text = font2.render("G", True, '#000000')
        screen.blit(text, (135, 20))
        
        text = font.render(str(self.board_dictionnaire["2"]), True, '#000000')
        screen.blit(text, (90, 260))
        text = font2.render("Magasin 2", True, '#000000')
        screen.blit(text, (60, 400))

        # draw the player turn
        if not gameOver:
            font = pygame.font.SysFont('Arial', 40)
            if self.player_turn == 1:
                text = font.render("Player 1's turn", True, '#000000')
            else:
                text = font.render("Player 2's turn", True, '#000000')
            screen.blit(text, (265, 265))
        else:
            font = pygame.font.SysFont('Arial', 40)
            text = font.render("Game Over", True, '#000000')
            screen.blit(text, (300, 200))
            font = pygame.font.SysFont('Arial', 30)
            text = font.render(winner, True, '#000000')
            screen.blit(text, (225, 265))
            
            text = font.render(score, True, '#000000')
            screen.blit(text, (225, 305))

        

        

            






