import random
from time import sleep
def mainFn():
  world = makeWorld()
  turtle1 = makeTurtle(world)
  chaseFn(world,turtle1) #This is random every time

def chaseTurtle(turtle1,turtle2,turtle3,turtle4):
  for i in [turtle1,turtle2,turtle3,turtle4]:
    num = randint(1,4)
    if num == 1:
      turtle1.turnToFace(turtle2)
      turtle1.forward(8)
      sleep(.001)
   
    if num == 2:
      turtle2.turnToFace(turtle3)
      turtle2.forward(24)
      sleep(.001)
      
    if num == 3:
      turtle3.turnToFace(turtle4)
      turtle3.forward(random.randint(1,20))
      sleep(.001)
      
    if num == 4:
      turtle4.turnToFace(turtle1)
      turtle4.forward(random.randint(12,20))
      sleep(.001)
      
      
def chaseFn(world,turtle1):
  turtle2 = makeTurtle(world)
  turtle3 = makeTurtle(world)
  turtle4 = makeTurtle(world)
  
  randomInt = randint(1,255)
  
  turtle1.penUp()
  turtle1.moveTo(randomInt, randomInt*2)
  turtle1.penDown()
  
  
  
  turtle2.penUp()
  turtle2.moveTo(int(randomInt/7),randomInt)
  turtle2.penDown()
  
  
  turtle3.penUp()
  turtle3.moveTo(randomInt,int(randomInt*.6541))
  turtle3.penDown()
  
  
  turtle4.penUp()
  turtle4.moveTo(800,randomInt)
  turtle4.penDown()
  
  
  for i in range(0,1700):
    chaseTurtle(turtle1,turtle2,turtle3,turtle4)
    
    
