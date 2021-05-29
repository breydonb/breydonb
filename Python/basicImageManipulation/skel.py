#Breydon Brennan
#9/20/19
#Img Editing

def mainFn(rMulti,gMulti, bMulti): #rMulti is the multiplier for red
  #imgP = pickAFile()
  #print imgP
  imgP = "C:\\Users\\B226-05\\Desktop\\mclaren25pct.jpg"
  img = makePicture(imgP)
  firstColorFn(img,rMulti, gMulti, bMulti)
  #colorEdit(img, gMulti)
  #dayTwoFn(img,rMulti,gMulti,bMulti)
  #negateFn(img)
  #writePictureTo(img, "C:\\Users\\B226-05\\Desktop\\transformed\\default.jpg") #unrem when result is :)
  explore(img)
   

def negateFn(img):
  for i in getPixels(img):
    theRed=255-getRed(i)
    setRed(i,theRed)
    theGreen=255-getGreen(i)
    setGreen(i, theGreen)
    theBlue=255-getBlue(i)
    setBlue(i, theBlue)
         
#first img edit

def firstColorFn(img,rMulti, gMulti, bMulti):  #send made image into fn
  for i in getPixels(img): #getPixels() formats the image
    theRed=getRed(i)
    theGreen=getGreen(i)
    theBlue=getBlue(i)
    
    setRed(i, theRed*rMulti)
    setGreen(i, theGreen*gMulti)
    setBlue(i, theBlue*bMulti)

#Using if in image editing

def colorEdit(img, gMulti):  #send made image into fn
  for i in getPixels(img): #getPixels() formats the image
    
    theRed=getRed(i)
    theGreen=getGreen(i)
    theBlue=getBlue(i)
    
    if theRed < 100:
      setRed(i, 255)
      #setColor(i,yellow)
    elif theGreen < 100:
      setGreen(i, theGreen*gMulti)
    elif theBlue> 100:
      setBlue(i, 255)
      
###########Code changes all 3 colors by multiplier & dividing the canvas##############
def dayTwoFn(img,rMulti,gMulti,bMulti):
  width=getWidth(img)
  height=getHeight(img)
  #note: getPixels() is what makes the array
  for i in getPixels(img):
    if getX(i) < .5*width:            
      theRed=getRed(i)
      setRed(i,theRed*rMulti)
      theGreen=getGreen(i)
      setGreen(i, theGreen*gMulti)
      theBlue=getBlue(i)
      setBlue(i, theBlue*bMulti)
    elif getY(i) < .5*height:
      theRed=getRed(i)
      setRed(i,theRed*rMulti)
      #theGreen=getGreen(i)
      #setGreen(i, theGreen*gMulti)
      theBlue=getBlue(i)
      setBlue(i, theBlue*bMulti)
