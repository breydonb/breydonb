def main():
    boyName = str(input("Boy Name:\t"))
    girlName = str(input("Girl Name:\t"))

    try:
        boyResult = testMethod(boyName, "sample.txt")
        girlResult = testMethod(boyName, "sample.txt")
        if boyResult:
            print("Boy name "+boyName+" found!")
        else:
            print("Boy name "+boyName+" not found!")
            
        if girlResult:
            print("Girl name "+girlName+" found!")
        else:
            print("Girl name"+girlName+" not found!")
        ask = str(input("Try Again (Y/N)?: \t"))
        while ask == 'y':
            

    except IOError:
        print("IO Error")
    except IndexError:
        print("Index Error")


def testMethod(name, fileName):
    file = open(fileName)
    for i in file:
        x = str(i).strip()
        if x == name:
            return True
    return False
main()