def mainFn():
  #we used static directories for this program to increase the speed of debugging
  #imgP = pickAFile();
  img = makePicture(imgP)
  lightStar(img)
  circleBlack(img)
  ellipseBlue(img)
  rectangleGray(img)
  lightQt(img)
  explore(img)
  
def lightStar(img):
  width = getWidth(img)
  height = getHeight(img)
  for i in getPixels(img):
    iRed = getRed(i)
    iGreen = getGreen(i)
    iBlue = getBlue(i)
    if 192 <= iRed <= 230 and 181 <= iGreen <= 224 and 202 <= iBlue <= 240: #I fine tuned this algorithm to get the star green
      setColor(i,green)
    elif 214 <= iRed <= 255 and 165 <= iGreen <= 216 and 188 <= iBlue <= 228:
      setColor(i, red)
      
def circleBlack(img):
  for i in getPixels(img):
    iRed = getRed(i)
    iGreen = getGreen(i)
    iBlue = getBlue(i)
    
    if 165 <= iRed <= 251 and 15 <= iGreen <= 39 and 25 <= iBlue <= 52:
      setColor(i,black)

      
def ellipseBlue(img):
  for i in getPixels(img):
    iRed = getRed(i)
    iGreen = getGreen(i)
    iBlue = getBlue(i)
    
    if 181 <= iRed <= 255 and 115 <= iGreen <= 175 and 25 <= iBlue <= 85:
      setColor(i,blue)

def rectangleGray(img):
  for i in getPixels(img):
    iRed = getRed(i)
    iGreen = getGreen(i)
    iBlue = getBlue(i)
    
    if 145 <= iRed <= 170 and 212 <= iGreen <= 224 and 225 <= iBlue <= 242:
      setColor(i, gray)
      
def lightQt(img):

  width = getWidth(img)
  height = getHeight(img)

  for i in getPixels(img):
    
    if getX(i) <= .5*width and getY(i) <= .5*height:
      
      color=getColor(i)
      makeLighter(color)
  
  