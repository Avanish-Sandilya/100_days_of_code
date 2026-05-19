from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

# Making a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# Drawing dashed line
# for _ in range(50):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3,11):
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
