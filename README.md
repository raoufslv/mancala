# mancala
Mancala implemented in python, interface with pygame, with some heuristics, computer vs computer, or computer vs human

Execute the 'game.py' to see the interface 
you can manipulate in the parameteres in main to change between player 1 and player 2  as well as 'computer vs computer' or  'computer vs human'

i also leaved some comments to understand the code.


the rules of the game are:

  - at first both players has six pits and one store each, in each pit the have four seeds.

  - The first player chooses a pit on their side of the board and takes all the seeds from it.
  
  - In a counterclockwise direction, the player drops one stone in each pit until they have no seeds left in their hand.
  
  - The player can drop a seed into any pit on the board (including their own store) except the opponent's store.
  
  - If the last seed dropped lands in the player's store, that player gets an extra turn.
  
  - If the last seed dropped lands in an empty pit on the player's side, that seed and all the seeds in the opposite pit (on the opponent's side) go to the player and are     placed in their store.
  
  - When a player has no seeds left in all their pits, the game ends and the opponent takes any remaining seeds and places them in their own store.
  
  - The player with the most seeds in their store wins.
