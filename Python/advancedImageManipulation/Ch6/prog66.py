def mainFn():

  img = makePicture(r"C:\Users\B226-05\Desktop\fOne25pct.jpg")

  #mirrorVert(img)
  #mirrorHz(img)
  mirrorTop(img)
  explore(img)

def mirrorVert(img):
  mirrorPt = getWidth(img) * .5 #You must include anything under 1 and it must be int
  width = getWidth(img)
  
  for y in range(0,getHeight(img)):
    for x in range(0, mirrorPt):
      leftPxl = getPixel(img,x,y)
      rightPxl = getPixel(img,width - x - 1,y)
      color = getColor(leftPxl)
      setColor(rightPxl, color)
      
def mirrorHz(img):
  mirrorPt = getHeight(img) * .5 #You must include anything under 1 and it must be int
  height = getHeight(img)
  
  for y in range(0,mirrorPt):
    for x in range(0, getWidth(img)):
      topPxl = getPixel(img,x,y)
      bottomPxl = getPixel(img,x ,height - y - 1)
      color = getColor(topPxl)
      setColor(bottomPxl, color)
      
def mirrorTop(img):
  mirrorPt = getHeight(img) * .5
  height = getHeight(img)
  
  for x in range(0,getWidth(img)):
    for y in range(0, mirrorPt):
      topPxl= getPixel(img,x,y)
      bottomPxl = getPixel(img, x, height -y - 1)
      color = getColor(bottomPxl)
      setColor(topPxl,color)