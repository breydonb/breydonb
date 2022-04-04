import random

def main():
    x = int(input("What is the number of numbers you want to generate?"))
    method = randomGenerator(x)
    concatElements = ""
    print("List of random numbers is: "+ str(method))
    for i in method:
        concatElements = concatElements + str(i)
    print("The concatenated list with "+str(x)+ " element(s) is: "+concatElements)


def randomGenerator(x):
    list = []
    for i in range(0,x):
        randomInteger = random.randint(1,9)
        list.insert(i,randomInteger)
        
    return list

main()