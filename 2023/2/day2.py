from cv2 import solve
import numpy
import logging

FILE_NAME = "2023/2/day2.txt"
FORMAT = "%(asctime)s | %(levelname)s | %(message)s"

# logging.basicConfig(level=logging.DEBUG,format=FORMAT)
logging.basicConfig(level=logging.INFO,format=FORMAT)

def acquireInput(fileName: str):
  with open(fileName,"r") as inputFile:
    logging.debug("File Accessed Successfully")
    return [line[:-1] for line in inputFile.readlines()]

def solve1(inputData: list[str])->int:
  gameSum = 0
  maxBalls = { "red" : 12 , "blue" : 14 , "green" : 13 }
  for game in inputData:
    game_num , game_data = game.split(":")

    game_num = int(game_num.split()[1])
    game_data = [[colorset.split()[::-1] for colorset in game_round.split(",")] for game_round in game_data.split(";")]

    logging.debug(f"{game_num} : {game_data}")

    for round in game_data:
      for color,num in round:
        if [1 for c in ['red','blue','green'] if color==c and maxBalls[c]<int(num)]:
          break
      else: continue
      break
    else:
      gameSum += game_num
  return gameSum

def solve2(inputData: list[str])->int:
  power = 0
  for game in inputData:
    game_num , game_data = game.split(":")

    game_num = int(game_num.split()[1])
    game_data = [[colorset.split()[::-1] for colorset in game_round.split(",")] for game_round in game_data.split(";")]

    r,g,b = 0,0,0
    for round in game_data:
      for color,num in round:
        if r<int(num) and color=="red":
          r = int(num)
        if g<int(num) and color=="green":
          g = int(num)
        if b<int(num) and color=="blue":
          b = int(num)
    power+=r*g*b
  return power

if __name__ == "__main__":
  problemInput = acquireInput(FILE_NAME)
  logging.info(f"Part 1 : {solve1(problemInput)}")
  logging.info(f"Part 2 : {solve2(problemInput)}")





#part 1 of the game
# with open("2023/2/day2.txt","r") as f:
#   s=[]
#   power=0
#   for x in f.readlines():
#     first_level_split = x.split(":")
#     gameno = int(first_level_split[0].split()[1])
#     #makes a list
#     second_split = [[element.split()[::-1] for element in part.split(",")] 
#                     for part in first_level_split[1].split(";")]
#     gamevalid = 1
#     for round in second_split:
#       for color in round:
#         if color[0]=='red' and int(color[1])>12:
#           gamevalid = 0
#           break
#         if color[0]=='blue' and int(color[1])>14:
#           gamevalid = 0
#           break
#         if color[0]=='green' and int(color[1])>13:
#           gamevalid = 0
#           break
#       if gamevalid==0:
#         break
#     else:
#       s.append(gameno)

#     maxes = [0,0,0]
#     for round in second_split:
#       for color in round:
#         if color[0]=='red' and int(color[1]) > maxes[0]:
#           maxes[0] = int(color[1])
#         if color[0]=='blue' and int(color[1]) > maxes[1]:
#           maxes[1] = int(color[1])
#         if color[0]=='green' and int(color[1]) > maxes[2]:
#           maxes[2] = int(color[1])
#     power+=numpy.prod(maxes)
          


#   print(sum(s))       
#   print(power)  