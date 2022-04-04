from audioop import reverse
import random

def main():
    x = int(input("What are the number of elements you want in your list?:\t"))
    numList = createList(x)

    numberAnalysis(numList)

def numberAnalysis(numList):
    print(numList.sort(reverse = True))

def createList(x):
    numList = []
    for i in range(0,x):
        numList.append(random.randint(-500,500))
    return numList

main()