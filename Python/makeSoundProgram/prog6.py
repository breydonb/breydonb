#Breydon Brennan
#mainFn("[fileLocation]")
#see prog6 pg. 38
def mainFn(filePath):
  playSound(filePath)
#################################################
def playSound(filePath):
  play(makeSound(filePath))
#################################################
def viewImg(imgFilePath):
  explore(makePicture(imgFilePath))