import numpy
import logging

FILE_NAME = "2023/4/day4.txt"
FORMAT = "%(asctime)s | %(levelname)s | %(message)s"

# logging.basicConfig(level=logging.DEBUG,format=FORMAT)
logging.basicConfig(level=logging.INFO,format=FORMAT)

def acquireInput(fileName: str):
  with open(fileName,"r") as inputFile:
    logging.debug("File Accessed Successfully")
    return [line[:-1] for line in inputFile.readlines()]

def solve1(inputData: list[str])->int:
  points = {0:0,1:1,2:2,3:4,4:8,5:16,6:32,7:64,8:128,9:256,10:512}
  tally = 0
  for card in inputData:
    info = [x for x in card.split() if x!='']
    index = int(info[1][:-1])
    nums = info[2:12]
    wins = info[13:]
    matches = len(['' for x in nums if x in wins])
    cardpts = points[matches]
    tally+=cardpts
  return tally

def solve2(inputData: list[str])->int:
  points = {0:0,1:1,2:2,3:4,4:8,5:16,6:32,7:64,8:128,9:256,10:512}
  card_num = [1]*len(inputData)
  for card in inputData:
    info = [x for x in card.split() if x!='']
    index = int(info[1][:-1])
    nums = info[2:12]
    wins = info[13:]
    matches = len(['' for x in nums if x in wins])
    # print(index,matches)
    for x in range(index,min(len(inputData),index+matches)):
      card_num[x]+=card_num[index-1]
  return sum(card_num)

if __name__ =="__main__":
  problemInput = acquireInput(FILE_NAME)
  logging.info(f"Part 1 : {solve1(problemInput)}")
  logging.info(f"Part 2 : {solve2(problemInput)}")



# with open("2023/4/day4.txt","r") as f:
#   data = f.readlines()
#   points = {0:0,1:1,2:2,3:4,4:8,5:16,6:32,7:64,8:128,9:256,10:512}
#   card_num = [1]*len(data)
#   tally = 0
#   for card in data:
#     info = [x for x in card.split() if x!='']
#     index = int(info[1][:-1])
#     nums = info[2:12]
#     wins = info[13:]
#     matches = len(['' for x in nums if x in wins])
#     # print(index,matches)
#     for x in range(index,min(len(data),index+matches)):
#       card_num[x]+=card_num[index-1]
#     cardpts = points[matches]
#     tally+=cardpts
#   print(tally)
#   print(sum(card_num))




