import logging

FILE_NAME = "2023/1/day1.txt"
FORMAT = "%(asctime)s | %(levelname)s | %(message)s"

# logging.basicConfig(level=logging.DEBUG,format=FORMAT)
logging.basicConfig(level=logging.INFO,format=FORMAT)


#file handling takes input
def acquireInput(fileName: str):
  with open(fileName,"r") as inputFile:
    logging.debug("File Accessed Successfully ")
    return [line[:-1] for line in inputFile.readlines()]


#solves first part using concatenation
def solve1(inputData: list[str])->int:
  nums_collection = [int([a for a in x if a.isnumeric()][0] + [a for a in x if a.isnumeric()][-1]) for x in inputData]
  return sum(nums_collection)


#converts the numbers into its number name wrapped around the number on both sides, then calls solve1
def solve2(inputData: list[str])->int:
  numbermap = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
  for i in range(len(inputData)):
    for numname in numbermap:
      inputData[i] = (numname+numbermap[numname]+numname).join(inputData[i].split(numname))
  return solve1(inputData)

if __name__ =="__main__":
  problemInput = acquireInput(FILE_NAME)
  logging.info(f"Ans 1 : {solve1(problemInput)}")
  logging.info(f"Ans 2 : {solve2(problemInput)}")