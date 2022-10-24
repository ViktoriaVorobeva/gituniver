import math
import random
#Функция, возвращающая случайное целое число из заданного диапазона (оба значения включительно)
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
