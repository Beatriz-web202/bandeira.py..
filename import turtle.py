import turtle


screen = turtle.Screen()
screen.title("Bandeira do Paquistão")
screen.bgcolor("white")
screen.setup(width=800, height=500)

t = turtle.Turtle()
t.speed(10)
t.penup()

# Função para desenhar um retângulo
def draw_rectangle(color, x, y, width, height):
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()

# Função para desenhar a lua crescente 
def draw_crescent(x, y, radius):
    t.goto(x, y - radius)
    t.setheading(113)
    t.color("white")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Círculo menor 
    t.goto(x + 20, y - radius + 10) 
    t.color("green")
    t.begin_fill()
    t.circle(radius- 2)
    t.end_fill()

# Função para desenhar uma estrela 
def draw_star(x, y, size, color):
    t.goto(x, y)
    t.setheading(20)
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    
    #ciculo estrela 
    t.goto(x + 18, y  -5)  
    t.color("white")
    t.begin_fill()
    t.circle(6)
    t.end_fill()


# Fundo verde
draw_rectangle("green", -200, 100, 400, -200)

# Faixa branca
draw_rectangle("white", -200, 100, 80, -200)

# Lua crescente 
draw_crescent(100, 70, 60)

# Estrela 
draw_star(50, 6, 30, "white")


t.hideturtle()
screen.mainloop()