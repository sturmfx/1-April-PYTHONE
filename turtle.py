import turtle
import random

c = turtle.Screen()
t = turtle.Turtle()
t.speed('slowest')


def draw_human(head, neck, torso, legs, hands):
    # рисование головы
    t.circle(head)
    # рисование шеи
    t.right(90)
    t.forward(neck)
    # рисование левой руки
    t.right(90)
    t.forward(hands)
    # рисование правой руки
    t.right(180)
    t.forward(hands * 2)
    # рисование торса
    t.right(180)
    t.forward(hands)
    t.right(270)
    t.forward(torso)
    # рисование левой ноги
    t.right(45)
    t.forward(legs)
    # рисование правой ноги
    t.right(180)
    t.forward(legs)
    t.right(90)
    t.forward(legs)
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
    draw_human(25, 25, 50,40,35)


c.onscreenclick(on_click)
c.mainloop()
