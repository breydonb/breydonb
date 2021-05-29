#Breydon Brennan
#10-11-19
#Midterm Exam

def mainFn(sPath): #sPath is my cmdArg for the file path. ###Check your slashes so Jython doesn't mistake it as escape characters###
  #I used C:\Users\B226-05\Desktop\buffalos.jpg as my reference
  imgP = pickAFile() 
  
  img = makePicture(imgP)
  negateFn(img)
  bwrFn(img)
  explore(img)
  
  writePictureTo(img, sPath)
  
def negateFn(img): 
  width = getWidth(img)
  height = getHeight(img)
  for i in getPixels(img):
    if not getX(i) <= width*.25 and not getX(i) >= width*.75: #I first test for the x position to be within my parameters, then my height
      if getY(i) <= height*.25 or getY(i) >= height*.75:
        iRed = 255 - getRed(i)
        iGreen = 255 - getGreen(i)
        iBlue = 255 - getBlue(i)
        newColor = makeColor(iRed,iGreen,iBlue)
        setColor(i, newColor)
      
      
def bwrFn(img):
  width = getWidth(img)
  height = getHeight(img)
  for i in getPixels(img):
    if height*.25 <= getY(i) <= height*.75:
      iRed = getRed(i)
      iGreen = getGreen(i)
      iBlue = getBlue(i)
      
      if iRed <= 120 or iGreen <= 120 or iBlue <= 120: #We can change these intervals and our logic of and/or to fine tune our image
        setColor(i,black)
      elif 121 <= iRed <= 175 or 121 <= iGreen <= 175 or 121 <= iBlue <= 175:
        setColor(i,red)
      else: #this is a failsafe, easier than typing out another elif
        setColor(i, white)