import random
def mainFn():
  iColor = pickAColor()
  penColor = pickAColor()
  img = makePicture(pickAFile())
  img2 = makePicture(pickAFile())
  world = makeEmptyPicture(getWidth(img),getHeight(img),iColor)
  turtle = Turtle(world)
  terry = cubeTurtle(world)
  jerry = circleTurtle(world)
  dropCircle(img2,world,jerry)
  randomBackground(turtle,world,penColor)
  shapeFn(terry,jerry,world,img)
  scaleImg(img,world,getWidth(img),0,4)
  
  
  
  explore(world)
  
def randomBackground(turtle,world,penColor):
  for i in range(0,1000):
    turtle.setPenColor(makeColor(penColor))
    turtle.setPenWidth(random.randint(1,5))
    turtle.forward(random.randint(1,100))
    turtle.turn(random.randint(20,70))

def shapeFn(terry,jerry,world,img):
  terry.penUp()
  terry.moveTo(random.randint(10,getWidth(img)/2),random.randint(10,getHeight(img)/2))
  terry.penDown()
  terry.drawCube()
  jerry.penUp()
  jerry.moveTo(50,201)
  jerry.penDown()
  jerry.circleFn()
  jerry.penUp()
  jerry.moveTo(random.randint(28,281),random.randint(28,281))
  jerry.penDown()
  jerry.circleFn()
  
def scaleImg(img,canvas,targetX,targetY,scaleArg):
  sourceX = 0
  for targetX in range(0, int(getWidth(img)/scaleArg)):
    sourceY = 0
    for targetY in range(0, int(getHeight(img)/scaleArg)):
      color = getColor(getPixel(img,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY = sourceY + scaleArg
    sourceX = sourceX + scaleArg 
     
def dropCircle(img2,world,jerry):
  jerry.circlePictFn(1,img2)
    
        
class cubeTurtle(Turtle):
  def drawCube(self,width=random.randint(100,590)):
    self.setPenWidth(10)
    for i in range(0,5):
      self.turnLeft()
      self.forward(width)
    
class circleTurtle(Turtle):
  def circleFn(self,width=random.randint(50,250)):
    self.setPenWidth(5)
    for i in range(0,360):
      self.penUp()
      self.forward(width)
      self.penDown()
      self.forward(1)
      self.penUp()
      self.turn(180)
      self.forward(width)
      self.turn(1)
  def circlePictFn(self,width,img2):
    self.setPenWidth(5)
    for i in range(0,360):
      self.penUp()
      self.forward(width)
      self.penDown()
      self.drop(img2)
      self.penUp()
      self.turn(180)
      self.forward(width)
      self.turn(1)
      
   

class randomTurtle(Turtle):
  def forward(self,num):
    Turtle.forward(self, int(300*random.random()))
  def turn(self,num):
    Turtle.turn(self, int(num*random.random()))