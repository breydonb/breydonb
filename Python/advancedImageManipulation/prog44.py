#Breydon Brennan
#10-7-19
#
def mainFn():
  #imgP = pickAFile
  imgP = r"C:\Users\B226-05\Desktop\buffalos.jpg" 
  img = makePicture(imgP)
  pxl = getPixels(img)
  colorChangeFn(img,0,(len(pxl)/4),"Red", 3,2,2) #Red, green, and blue multiplier
  explore(img)
  
def colorChangeFn(img, startPx, endPx, whatColor, pctRed,pctGreen,pctBlue): 
  pxl = getPixels(img)
  theWidth = getWidth(img)
  for i in range(startPx, endPx):
    onePxl = pxl[i]
    if whatColor == "Red" and getX(onePxl) < theWidth*.25:
      iRed = getRed(onePxl)
      setRed(onePxl, iRed*pctRed)
    elif whatColor == "Green":
      iGreen = getGreen(onePxl)
      setGreen(onePxl, iGreen*pctGreen)
    elif whatColor == "Blue":
      iBlue = getBlue(onePxl)
      setBlue(onePxl, iBlue*pctBlue)