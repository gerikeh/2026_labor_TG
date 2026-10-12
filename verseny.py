# autoverseny
import turtle


class Auto(turtle.Turtle):
    def __init__(self, szin, x, y, sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.speed(15)
        self.goto(x, y)
        self.sebesseg = sebesseg

    def indit(self):
        self.forward(self.sebesseg)


ablak = turtle.Screen()
ablak.title("Autoverseny")
ablak.bgcolor("black")

a1 = Auto(szin="red", x=-400, y=0, sebesseg=10)
a2 = Auto(szin="green", x=-400, y=-100, sebesseg=10)

ablak.listen()

ablak.onkey(turtle.bye, key="Escape")
ablak.onkey(a1.indit, key="d")
ablak.onkey(a2.indit, key="k")

turtle.mainloop()