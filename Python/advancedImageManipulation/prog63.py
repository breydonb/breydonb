#Breydon Brennan
#10/23/19
#Embeded for loop

def mainFn():
  img = makePicture(r"C:\Users\B226-05\Desktop\gt25pct.jpg")
  firstLoop(img,.5,.75,.25,1) #4 args are between 0 and 1 in this order xStart,xEnd,yStart,yEnd
  secondLoop(img)
  thirdLoop(img)
  fourthLoop(img)
  fifthLoop(img)
  explore(img)
  
def firstLoop(img,xStart,xEnd,yStart, yEnd):
  for x in range(getWidth(img)*xStart, getWidth(img)*xEnd):
    for y in range(getHeight(img)*yStart,getHeight(img)*yEnd):
      pxl = getPixel(img,x,y)
      theColorVal = (getRed(pxl)+getGreen(pxl)+getBlue(pxl))
      if theColorVal <= 200:
        setColor(pxl, black)
      elif 201 <= theColorVal <=600:
        setColor(pxl, red)
      else:
        setColor(pxl, white)
        
def secondLoop(img):
  for x in range(0, getWidth(img)):
    for y in range(getHeight(img)*.60,getHeight(img)*.85):
      pxl = getPixel(img,x,y)
      iRed = 255-getRed(pxl)
      iGreen = 255-getGreen(pxl)
      iBlue = 255-getBlue(pxl)
      
      negate= makeColor(iRed,iGreen,iBlue)
      setColor(pxl,negate)
      
def thirdLoop(img):
  for x in range(getWidth(img)*.35,getWidth(img)*.75):
    for y in range(getHeight(img)*.25, getHeight(img)*.75):
      pxl = getPixel(img,x,y)
      blueImg = makeColor(getRed(pxl)*.25,0, getBlue(pxl)*1.7)
      setColor(pxl,blueImg)
      
def fourthLoop(img):
  for x in range(getWidth(img)*.25,getWidth(img)*.67):
    for y in range(getHeight(img)*.67, getHeight(img)):
      pxl = getPixel(img,x,y)
      colorGreen = makeColor(getRed(pxl)*.25, getGreen(pxl)*1.5, getBlue(pxl)*.5)
      setColor(pxl,colorGreen)
      
def fifthLoop(img):
  for x in range(getWidth(img)*.5, getWidth(img)*.8):
    for y in range(getHeight(img)*.5,getHeight(img)*.65):
      pxl = getPixel(img,x,y)
      iRed = 255-getRed(pxl)
      iGreen = 255-getGreen(pxl)
      iBlue = 255-getBlue(pxl)
      
      negate= makeColor(iRed,iGreen,iBlue)
      setColor(pxl,negate)