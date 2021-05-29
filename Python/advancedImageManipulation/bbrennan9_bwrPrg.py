#Breydon Brennan
#Open Lab Problem 10-4-19
#This program asks you to pick a file and then makes the picture black,white, and red depending on parameters set in the logic statements

def mainFn(path):
  imgP = pickAFile()
  img = makePicture(imgP)
  bwrFn(img)
  explore(img)
  #writePictureTo(img, path) #Unrem if you want to write a good result to the path cmd arg
  
def bwrFn(img):
  for i in getPixels(img):
    iRed = getRed(i)
    iGreen  = getGreen(i)
    iBlue = getBlue(i)
    
	#Here is our logic, this can be edited if you want to change what pixels are black,white, or red

    if iRed < 100 and iGreen < 100 and iBlue < 100:
      setColor(i, black)
    
    elif 100 < iRed < 150 or 100 < iGreen < 150 or 100 < iBlue < 150:
      setColor(i, red)
      
    elif 150 < iRed <= 255 and 150 < iGreen <= 255 and 150 < iBlue <= 255:
      setColor(i, white)
      
    else:
      setColor(i,white)