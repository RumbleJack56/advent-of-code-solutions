from fileinput import filename
import logging

FILE_NAME = "2023/3/day3.txt"
FORMAT = "%(asctime)s | %(levelname)s | %(message)s"

# logging.basicConfig(level=logging.DEBUG,format=FORMAT)
logging.basicConfig(level=logging.INFO,format=FORMAT)

def acquireInput(fileName: str):
  with open(fileName,"r") as inputFile:
    logging.debug("File Accessed Successfully")
    return inputFile.read()

def solve1(inputData: str)->int:
  total = 0
  numbegin = 1
  numend = 0
  for i in range(len(inputData)):
    if inputData[i].isnumeric() and numbegin < numend:
      numbegin = i
    if inputData[i-1].isnumeric() and not inputData[i].isnumeric():
      numend = i
      numup = [inputData[numbegin-142:numend-140] if numbegin>140 else "....."]
      num = inputData[numbegin-1:numend+1]
      numdown = [inputData[numbegin+140:numend+142] if numend+140<len(inputData) else "....."]

      # print (numup , num, numdown)

      symbols = numup[0]+numdown[0]+num[0]+num[-1]
      symbols = [x for x in symbols if x not in list(".\n0123456789")]   
      # print(num[1:-1], symbols)    
      if len(symbols)!=0:
        total+=int(num[1:-1])
  return total

def solve2(inputData: str)->int:
  numstart = 0
  numend = 0
  num = 0
  numcollection = []
  starindex= []
  for i,x in enumerate(inputData):
    if x.isnumeric():
      num=10*num+int(x)
      if not inputData[i-1].isnumeric():
        numstart=i
      if not inputData[i+1].isnumeric():
        numend=i
        numcollection.append([num,numstart,numend])
        num=0
  for a,b,c in numcollection:
    for x in range(b-1,c+2):
      if x>141 and inputData[x-141]=="*":
        starindex.append([a,x-141])
      if x<len(inputData)-141 and inputData[x+141]=="*":
        starindex.append([a,x+141])
      if inputData[x]=="*":
        starindex.append([a,x])

  stardict = {}
  for a,b in starindex:
    if b in stardict:
      stardict[b].append(a)
    else:
      stardict[b] = [a]
  val = [x[0]*x[1] for x in stardict.values() if len(x)==2]
  return sum(val)

if __name__ == "__main__":
  problemData = acquireInput(FILE_NAME)
  logging.info(f"Part 1 : {solve1(problemData)}")
  logging.info(f"Part 2 : {solve2(problemData)}")

#140 width


