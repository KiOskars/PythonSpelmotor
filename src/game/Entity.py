from src.game import  *

class Entity(InitializerIf, Turtle):
    def __init__(self, name, shape, angle, size, x, y, color):
        super(Entity, self).__init__(name, "Entity är vårt spelobjekt som populerar spelvärden")
        self.__setattr__('speed', 100)

        Turtle.__init__(self)
        self._speed = 0
        self.shape(shape)
        self.tiltangle(angle)
        self.turtlesize(size)
        self.setposition(x, y)
        self.fillcolor(color)
        self.color(color)

    def move(self, x, y):
        self.setposition(self.xcor() + x, self.ycor() + y)

    def moveRight(self):
        self.move(self.__getattribute__('speed'), 0)
    def moveLeft(self):
        self.move(-self.__getattribute__('speed'), 0)
    def moveUp(self):
        self.move(0, self.__getattribute__('speed'))
    def moveDown(self):
        self.move(0, -self.__getattribute__('speed'))

    def defineKeys(self, turtleScreen: TurtleScreen):
        #turtleScreen.listen()
        turtleScreen.onkeypress(self.moveRight, "Right")
        turtleScreen.onkeypress(self.moveLeft, "Left")
        turtleScreen.onkeypress(self.moveUp, "Up")
        turtleScreen.onkeypress(self.moveDown, "Down")