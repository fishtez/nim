# nimsum.py
# just starting with calculating nimsum


# let ++ be binary addition "without carry".
# num1 and num2 are each either 0 or 1.
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

# takes two non-negative integers, returns nimsum.
# we cannot just convert to binary and add because 
  # nimsum is binary addition "without carry".
def nimsum(pile1, pile2):
  # convert each to binary string, currently fills to width 8
  # TODO pad with 0s for monster numbers
  pile1_bin = format(pile1, '08b')
  pile2_bin = format(pile2, '08b')
  # currently assumes both binary strings are same length
  # instead, should iterate from right to left and
    # when one string ends, just fill the rest with zeros
  
  return None


def testies():
  print(binaryADD_nocarry(1,1))
  print(binaryADD_nocarry(1,0))
  print(binaryADD_nocarry(0,0))
  

testies()