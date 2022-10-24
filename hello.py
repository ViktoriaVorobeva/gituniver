import math
import random

def getRandomPositiveInteger(a, b) :
  if a < 0 and b < 0 :
     print("NaN")
     return

  lower = math.ceil(min(a, b))
  upper = math.floor(max(a, b))
  result = random.random() * (upper - lower + 1) + lower
  print(math.floor(result))
  return 

getRandomPositiveInteger(1,100)
