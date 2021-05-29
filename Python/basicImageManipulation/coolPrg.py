def mainFn():

  imgP = r"C:\Users\B226-05\Desktop\vette25pct.jpg"
  img = makePicture(imgP)
  bwrFn(img)
  explore(img)
  writePictureTo(img,r"C:\Users\B226-05\Desktop\test2\5th.jpg")

def bwrFn(img):
  width = getWidth(img)
  height = getHeight(img)
  
  for i in getPixels(img):
    if height*.25 <= getY(i) <= height*.75:
      iRed = getRed(i)
      iGreen = getGreen(i)
      iBlue = getBlue(i)
      
      if iRed <= 60 or iGreen <= 72 or iBlue <= 72: #We can change these intervals and our logic of and/or to fine tune our image
        setColor(i,black)
      elif 61 <= iRed <= 125 or 73 <= iGreen <= 125 or 72 <= iBlue <= 125:
        setColor(i,green)
      else: #this is a failsafe, easier than typing out another elif
        setColor(i,white) 
    if height*.32 <= getY(i) <= height*.50 or 209 < getX(i) < 703 :
      iRed = getRed(i)
      iGreen = getGreen(i)
      iBlue = getBlue(i)
      
      grayScale = ((iRed+iGreen+iBlue)/3)
      grayScale = makeColor(grayScale, grayScale, grayScale)
      setColor(i, grayScale)
    
    
    if getRed(i) <= 255 and 0 <= getX(i) <= 255 and height*.25 <= getY(i):
      iRed = 255- getRed(i)
      iGreen = 255 - getGreen(i)
      iBlue = 255- getBlue(i)
      
      negate = makeColor(iRed, iGreen, iBlue)
      setColor(i, negate)
      
    if width*.5 <= getX(i) <= width*.8 and width*.5 <= getY(i)<= width*.8:
      light = makeColor((iRed*1),(iGreen*1.75),(iBlue*1.5))
      setColor(i,light)
    
    if getX(i) > width*.8 or getY(i) > height*.7:
      iRed = getRed(i)
      iGreen = getGreen(i)
      iBlue = getBlue(i)
      
      light = makeColor((iRed*1),(iGreen*1.75),(iBlue*1.5))
      color = getColor(i)
      setColor(i,light)
       
      