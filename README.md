# nim

In the game of Nim, a winning move can be determined by computing the nimsum of the piles in the game.
If the nimsum of the initial piles does not equal 0, then player1 can guarantee a win,
  else, nimsum == 0 and player2 has a winning strategy.
  
Nimsum is equivalent to a bitwise XOR of the piles in the game.

more about nim: https://en.wikipedia.org/wiki/Nim
