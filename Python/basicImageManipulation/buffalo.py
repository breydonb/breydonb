#Breydon Brennan
#9/20/19
#Img Editing

def mainFn(rMulti,gMulti, bMulti): #rMulti is the multiplier for red
  #imgP = pickAFile()
  #print imgP
  imgP = 'C:\\Users\\B226-05\\Desktop\\buffalos.jpg'
  img = makePicture(imgP)
  #firstColorFn(img,rMulti, gMulti, bMulti)
  firstBackFn(img)
  #colorEdit(img, gMulti)
  #dayTwoFn(img,rMulti,gMulti,bMulti)
  #negateFn(img)
  #writePictureTo(img, "C:\\Users\\B226-05\\Desktop\\transformed\\default.jpg") #unrem when result is :)
  explore(img)
   
#first img edit

def firstColorFn(img,rMulti, gMulti, bMulti):  #send made image into fn
  for i in getPixels(img): #getPixels() formats the image
    theRed=getRed(i)
    theGreen=getGreen(i)
    theBlue=getBlue(i)
    
    setRed(i, theRed*rMulti)
    setGreen(i, theGreen*gMulti)
    setBlue(i, theBlue*bMulti)

#####First Buffalo Back Color Function#####

def firstBackFn(img):
  
  for i in getPixels(img):
    theRed=getRed(i)
    theGreen=getGreen(i)
    theBlue=getBlue(i)
  
    if 140 < theRed < 160 and 100 < theGreen < 120 and 60 < theBlue < 90 :
      liteBlue = makeColor(0,255,255)
      setColor(i, liteBlue)
    
    elif 115 < theRed <= 140 and 70 < theGreen <= 100 and 50 < theBlue < 60:
      darkerBlue = makeColor(0,200,255)
      setColor(i, darkerBlue)
      
    elif 80 < theRed < 100 and 50 <= theGreen < 70 and 30 < theBlue <= 50:
      darkerBlue = makeColor(0,200,255)
      setColor(i, darkerBlue)  
      
    elif 50 < theRed < 70 and 30 < theGreen < 50 and 20 < theBlue < 30:
      darkerBlue = makeColor(0,200,255)
      setColor(i, darkerBlue)
    
    elif 30 < theRed < 50 and 10 < theGreen < 30 and 20 < theBlue < 40:
      darkerBlue = makeColor(0,200,255)
      setColor(i, darkerBlue)
    
    elif 10 < theRed < 30 and 10 < theGreen < 30 and 20 < theBlue < 40:
      darkerBlue = makeColor(0,200,255)
      setColor(i, darkerBlue)
      
    elif 2 < theRed < 10 and 2 < theGreen < 10 and 2 < theBlue < 10:
      darkerBlue = makeColor(0,200,255)
      setColor(i, darkerBlue)
def negateFn(img):
  for i in getPixels(img):
    theRed=255-getRed(i)
    setRed(i,theRed)
    theGreen=255-getGreen(i)
    setGreen(i, theGreen)
    theBlue=255-getBlue(i)
    setBlue(i, theBlue)
         
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
