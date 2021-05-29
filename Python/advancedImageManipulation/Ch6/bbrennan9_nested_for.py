def mainFn():
  img = makePicture(pickAFile())
  
  #mirrorFn(img)
  bwrFn(img)       #This will select 
  
  explore(img)
  
def mirrorFn(img):
  mirrorPt = getHeight(img) *.5
  height = getHeight(img)
  
  for x in range(0, getWidth(img)):
    for y in range(0, mirrorPt):
      leftPxl = getPixel(img,x,y)
      rightPxl= getPixel(img,x, height - y - 1)
      color = getColor(leftPxl)
      setColor(rightPxl, color)
      
def bwrFn(img):
  for x in range(getWidth(img)*.25, getWidth(img)*.75):
    for y in range(getHeight(img)*.25, getHeight(img)*.75):
      pxl = getPixel(img,x,y)
      iRed = getRed(pxl)
      iGreen = getGreen(pxl)
      iBlue =  getBlue(pxl)
      color = makeColor(iRed,iGreen,iBlue)
      
      if color < 150:
        setColor(pxl, black)
      elif 150 < color < 200:
        setColor(pxl, red)
      