import random

def mainFn():
  world = makeEmptyPicture(500,500)
  turtle = circleTurtle(world)
  turtle.circleFn()
  
  turtle1= cubeTurtle(world)
  turtle1.drawCube()
  turtle1.moveTo(310,224)
  turtle1.penUp()
  turtle1.moveTo(350,252)
  turtle1.penDown()
  turtle1.moveTo(409,224)
  turtle1.drawCube()
  turtle1.moveTo(350,252)
  turtle1.moveTo(249,251)
  turtle1.penUp()
  turtle1.moveTo(151,350)
  turtle1.penDown()
  turtle1.moveTo(200,323)
  turtle1.moveTo(309,323)
  explore(world)
  
class circleTurtle(Turtle):
  def circleFn(self,width=random.randint(50,250)):
    self.setPenWidth(6)
    for i in range(0,360):
      self.penUp()
      self.forward(width)
      self.penDown()
      self.forward(1)
      self.penUp()
      self.turn(180)
      self.forward(width)
      self.turn(1)
  
class cubeTurtle(Turtle):
  def drawCube(self,width=100):
    self.setPenWidth(3)
    for i in range(0,4):
      self.turnLeft()
      self.forward(width)
