# nimsum.py
# just starting with calculating nimsum

# binary addition "without carry"
# num1 and num2 are each either 0 or 1
# 0 ++ 0 = 1 ++ 1 = 0
# 0 ++ 1 = 1 
# TODO add error check for not 0 or 1
#   what behavior do I want upon invalid arg?
def binaryADD_nocarry(num1, num2):
  result = (num1 + num2) % 2
  if result != 0:
    return 1
  else:
    return 0
  

# takes two integers, returns nimsum
def nimsum(pile1, pile2):
	
	return
	
def testies():
  print(binaryADD_nocarry(1,1))
  print(binaryADD_nocarry(1,0))
  print(binaryADD_nocarry(0,0))