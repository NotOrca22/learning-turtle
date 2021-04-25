import turtle

class Rectangle():
  def __init__(self, length, width, pencolor, fillcolor):
    self.length = length
    self.width = width
    self.pencolor = pencolor
    self.fillcolor = fillcolor

  def draw(self, x, y):
    t = turtle.Pen()
    t.penup()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.pendown()
    t.pencolor(self.pencolor)
    t.fillcolor(self.fillcolor)
    t.begin_fill()
    t.forward(self.length)
    t.left(90)
    t.forward(self.width)
    t.left(90)
    t.forward(self.length)
    t.left(90)
    t.forward(self.width)
    t.left(90)
    t.end_fill()


if __name__ == "__main__":
  rect = Rectangle(90,90,(1,1,0), (0,0,0.5))
  rect.draw(20,20)
  turtle.mainloop()
