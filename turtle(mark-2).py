import turtle as t
t.setup(800,600,200,200)

def draw_shape(sides):
    t.pensize(3)
    t.pencolor("black")
    for i in range(sides):
        t.right(360/sides)
        t.fd(200/sides)

x = -400
y = 200
for i in range(0,100):
    t.up()
    t.goto(x,y)
    t.down()
    draw_shape(i)
    x = x + 80
    print(x)
    if x > 400:
        x = x - 800
        y = y - 100
t.done()