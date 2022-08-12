import turtle

def draw_sqrt():

    # for creating a screen
    window = turtle.Screen()

    # for setting the background color of that screen
    window.bgcolor('blue')

    # creating an object named john of turtle class
    john = turtle.Turtle()

    # giving shape to object
    john.shape('turtle')

    # giving color to object
    john.color('red')

    # giving speed to joh
    john.speed(1)

    # now for making a square we are moving the object
    john.forward(100)
    john.right(90)
    john.forward(100)
    john.right(90)
    john.forward(100)
    john.right(90)
    john.forward(100)

    andy = turtle.Turtle()
    andy.shape('arrow')
    andy.circle(100)
    # for closing the window in click
    window.exitonclick()


draw_sqrt()
