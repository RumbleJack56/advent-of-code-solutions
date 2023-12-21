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