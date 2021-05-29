from time import sleep
import random
def mainFn():
  world = makeWorld(1000,1000)
  sean = Turtle(world)  #You must use the class to put the turtle into the world we create
  sean.setPenWidth(5)
  for i in range(2500):
    sean.setPenColor(makeColor(random.randint(2,255),random.randint(2,255),random.randint(2,255)))
    sean.setPenWidth(random.randint(10,25))
    sean.forward(int(60*random.random()))
    sean.turn(int(90*random.random()))
    sleep(.001)
    
class randomTurtle(Turtle):
  def forward(self,num):
    Turtle.forward(self, int(300*random.random()))
  def turn(self,num):
    Turtle.turn(self, int(num*random.random()))