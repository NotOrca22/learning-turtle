import turtle

class Circle():
  def __init__(self, pencolor, fillcolor):
    self.pencolor = pencolor
    self.fillcolor = fillcolor

  def draw(self, x, y, radius):
    t = turtle.Pen()
    t.penup()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.pendown()
    t.pencolor(self.pencolor)
    t.fillcolor(self.fillcolor)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


if __name__ == "__main__":
    circle = Circle((1,0,0), (0,0,1))
    circle.draw(0,0,50)
    turtle.mainloop()
