import turtle
turtle.reset()
turtle.shape('turtle')
def rectangle(r):
    for i in range(4):
        turtle.forward(r)
        turtle.left(90)
rectangle(30)
turtle.up()        
turtle.goto(-10,-10)
turtle.down()
rectangle(50)
turtle.up()
turtle.goto(-20,-20)
turtle.down()
rectangle(70)
turtle.up()
turtle.goto(-30,-30)
turtle.down()
rectangle(90)
turtle.up()        
turtle.goto(-40,-40)
turtle.down()
rectangle(110)
turtle.up()
turtle.goto(-50,-50)
turtle.down()
rectangle(130)
turtle.up()
turtle.goto(-60,-60)
turtle.down()
rectangle(150)
turtle.up()
turtle.goto(-70,-70)
turtle.down()
rectangle(170)
turtle.up()
turtle.goto(-80,-80)
turtle.down()
rectangle(190)
turtle.up()
turtle.goto(-90,-90)
turtle.down()
rectangle(210)
turtle.Screen.exitonclick()
turtle.Screen.mainloop()
