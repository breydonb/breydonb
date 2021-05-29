def mainFn():
  img = makePicture(r"C:\Users\B226-05\Desktop\gt25pct.jpg")
  canvas = makeEmptyPicture(getHeight(img),getWidth(img))
  
  funEdit(img)
  randomPxl(img)
  backgroundImg(img,canvas)
  grabLights(img,canvas)
  
  
  explore(canvas)
  
  writePictureTo(canvas,r"C:\Users\B226-05\Desktop\gt25pctchanged.jpg")
  
  
def grabLights(img,canvas):
  targetX = 0
  for sourceX in range(296, 437):
    targetY = 0
    for sourceY in range(100,137):
      color = getColor(getPixel(img,sourceX,sourceY))
      if not getRed(getPixel(img,sourceX,sourceY)) > 150:
        setColor(getPixel(canvas,sourceX,sourceY), color)
    targetY = targetY + 1
  targetX = targetX + 1
   
def backgroundImg(img,canvas):
  targetX = 0 
  for sourceX in range(0,getWidth(img)):
    targetY = 0
    for sourceY in range(0,getHeight(img)):
      color = getColor(getPixel(img,sourceX,sourceY))
      setColor(getPixel(canvas,sourceY,sourceX), color)
    targetY = targetY + 1
  targetX = targetX + 1
  
def funEdit(img):
  for x in range(436, 790):
    for y in range(0, getHeight(img)):
      pxl = getPixel(img,x,y)
      iRed = getRed(pxl)
      iGreen = getGreen(pxl)
      iBlue = getBlue(pxl)
      
      if iRed < 60 and iGreen < 60 and iBlue < 60:
        blueColor = makeColor(0,196,237)
        setColor(pxl, blueColor)
      
      elif 75 < iRed < 128 and 75 < iGreen < 128:
        orangeTint = makeColor(246, 168, 2)
        setColor(pxl, orangeTint)
        
      else:
        setColor(pxl, green)

def randomPxl(img):
    for x in range(0,getWidth(img)):
        for y in range(0, getHeight(img)):
          pxl = getPixel(img,x,y)
          iRed = getRed(pxl)
          iGreen = getGreen(pxl)
          iBlue = getBlue(pxl)
          
          grayScale = (iRed+iGreen+iBlue)/3
          grayScale = makeColor(grayScale)
          
          
