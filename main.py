## extracting colors using colorgram
# import colorgram
#
# rbg_list = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     rbg_list.append(new_tuple)
#
# print(rbg_list)


import turtle as t
import random as r
screen = t.Screen()
# since we're using rgb make sure the colormode is 255
screen.colormode(255)
tim = t.Turtle()

c_list = [(238, 254, 249), (23, 16, 94),(232, 43, 6), (153, 14, 30),
          (41, 181, 158), (127, 253, 206), (237, 71, 166),(209, 179, 208),
          (246, 218, 21), (40, 133, 242), (244, 247, 253), (246, 218, 5),
          (207, 148, 178), (126, 155, 204), (106, 189, 174), (224, 134, 117),
          (81, 87, 136),(150, 64, 75), (209, 87, 66), (49, 44, 100),
          (244, 168, 154), (175, 184, 222), (111, 9, 23), (179, 30, 10)]

tim.speed(0)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number = 101
for count in range(1, number):
    tim.dot(20, r.choice(c_list))
    tim.forward(50)
    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()




