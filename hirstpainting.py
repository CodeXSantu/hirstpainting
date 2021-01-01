import turtle as turtle_module
import random

# import colorgram

# rgb_colors = []

# colors = colorgram.extract('img.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)


# print(rgb_colors)


color_list = [(247, 250, 253), (227, 227, 225), (249, 252, 251), (248, 212, 93), (55, 99, 155), (149, 70, 98), (232, 137, 61), (244, 238, 242), (108, 174, 211), (118, 82, 58), (201, 146, 177), (199, 77, 110), (146, 134, 71), (229, 90, 59), (140, 192, 139), (73, 102, 89), (67, 162, 92), (6, 165, 179), (227, 161, 184), (166, 195, 219), (115, 126, 142), (11, 68, 129), (189, 17, 29), (4, 58, 112), (231, 173, 162), (172, 203, 177), (164, 199, 215), (169, 27, 24), (76, 58, 43), (86, 60, 39)]
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.ht()

tim.setheading(225)
tim.forward(150)
tim.setheading(0)


for dot_count in range(1,101):
    tim.dot(10,random.choice(color_list))
    tim.forward(25)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(25)
        tim.setheading(180)
        tim.forward(250)
        tim.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()