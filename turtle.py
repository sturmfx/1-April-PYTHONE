import turtle
import random

c = turtle.Screen()
t = turtle.Turtle()
t.speed('slowest')


def draw_human():
    # рисование головы
    t.circle(25)
    # рисование шеи
    t.right(90)
    t.forward(25)
    # рисование левой руки
    t.right(90)
    t.forward(35)
    # рисование правой руки
    t.right(180)
    t.forward(70)
    # рисование торса
    t.right(180)
    t.forward(35)
    t.right(270)
    t.forward(50)
    # рисование левой ноги
    t.right(45)
    t.forward(40)
    # рисование правой ноги
    t.right(180)
    t.forward(40)
    t.right(90)
    t.forward(40)
    # возвращаем напраление черепашки направо
    t.left(45)


def forest():
    t.left(90)
    t.forward(50)
    t.left(135)
    t.forward(50)
    t.right(180)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(180)
    t.forward(50)
    t.left(135)
    t.forward(25)
    t.right(45)
    t.forward(50)
    t.right(180)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(180)
    t.forward(50)



def on_click(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    forest()


c.onscreenclick(on_click)
c.mainloop()
