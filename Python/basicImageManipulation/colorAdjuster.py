#Breydon Brennan
#9/20/19
#Img Editing

def mainFn(rMulti,gMulti, bMulti): #rMulti is the multiplier for red
  imgP = "C:\\Users\\B226-05\\Desktop\\mclaren25pct.jpg"
  img = makePicture(imgP)
  #firstColorFn(img,rMulti, gMulti, bMulti)
  #grayFn(img)
  #bwFn(img, 260) #enter 0-765
  bwrFn(img)
  explore(img)
  #writePictureTo(img, r"C:\Users\B226-05\Desktop\test\weird.jpg")
  
def bwrFn(img):
  for i in getPixels(img):
    theRed=getRed(i)
    theGreen=getGreen(i)
    theBlue=getBlue(i)
    colValue=(theRed+theGreen+theBlue) #0-765
    
    if colValue < 375 and theRed < 108:
      setColor(i, black)
      
    elif 376 < colValue < 400:
      setColor(i, red)
      
    else:
      setColor(i, white)

#####################first black and white fn###########################
def bwFn(img, bwMulti):
  for i in getPixels(img):
    theRed=getRed(i)
    theGreen=getGreen(i)
    theBlue=getBlue(i)
    colValue=(theRed+theGreen+theBlue)
    
    if colValue < bwMulti:
      setColor(i, black)
      
    else:
      setColor(i, white)

def grayFn(img):  #send made image into fn
  for i in getPixels(img): #getPixels() formats the image
    theRed=getRed(i)
    theGreen=getGreen(i)
    theBlue=getBlue(i)
    catGray=(theRed+theGreen+theBlue)/3
    theGray=makeColor(catGray,catGray,catGray)
    setColor(i,theGray)

         
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