import random
import turtle

a = turtle.Turtle()
a.shape("turtle")
a.speed()
a.penup()

# b = turtle.Turtle()
# b.shape("turtle")
# b.speed()
# b.penup()

score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-350, 250)
score_display.write(f"Счет: {score}", font=("Arial", 16, "normal"))


def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Счет: {score}", font=("Arial", 16, "normal"))


window = turtle.Screen()
window.title("shape")
window.bgcolor("white")
window.setup(width=800, height=600, startx=None, starty=None)

apple = turtle.Turtle()
apple.shape("circle")
apple.penup()
apple.speed(-1)
apple.color("red")

toulet = turtle.Turtle()
toulet.shape("circle")
toulet.penup()
toulet.color("red")
def go_toulet():
    x = random.randint(-390, 390)
    y = random.randint(-290, 290)
    toulet.goto(x, y)

go_toulet()

#
# z = turtle.Turtle()
# z.shape("square")
# z.penup()
# z.color("brown")
# def go_z():
#     x = random.randint(-390, 390)
#     y = random.randint(-290, 290)
#     go_z().goto(x, y)






timer = 30
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(200, 200)
timer_display.write(f"Время {timer}", font=("Arial", 16, "normal"))


def update_timer():
    global timer
    if timer > 0:
        timer -= 1
        timer_display.clear()
        timer_display.write(f"Время {timer}", font=("Arial", 16, "normal"))
        window.ontimer(update_timer, 1000)

    else:
        timer_display.clear()
        timer_display.goto(-200, 0)
        timer_display.write("GAME OVER", font=("Arial", 50, "normal"))
        window.bye()



def go_apple():
    x = random.randint(-390, 390)
    y = random.randint(-290, 290)
    apple.goto(x, y)


def move_forward():
    a.forward(10)
    check_poss()


def move_backward():
    a.backward(10)
    check_poss()


def move_right():
    a.right(90)
    check_poss()


def move_left():
    a.left(90)
    check_poss()



#
# def move_forward():
#     b.forward(10)
#     check_poss()
#
#
# def move_backward():
#     b.backward(10)
#     check_poss()
#
#
# def move_right():
#     b.right(90)
#     check_poss()
#
#
# def move_left():
#     b.left(90)
#     check_poss()

# # def time_pluse():
# #     global timer
#     if a.distance(apple) < 20:
#         timer += 10
#         timer_display.clear()
#         timer_display.write(f"Время {timer}", font=("Arial", 16, "normal"))
#         window.ontimer(update_timer, 1000)
def check_poss():
    # global timer
    # if a.distance(apple) < 20:
    #      timer += 10
    #      timer_display.clear()
    #      timer_display.write(f"Время {timer}", font=("Arial", 16, "normal"))
    #      window.ontimer(update_timer, 1000)
    #      go_apple()
    if a.distance(toulet) < 20:
        window.bye()
        update_score()


def move():
    a.forward(1)
    window.ontimer(move, 1)
    move()


update_timer()


window.listen()
window.onkeypress(move_forward, "w")
window.onkeypress(move_backward, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")
window.onkeypress(go_apple, "space")



#
# window.listen(b)
# window.onkeypress(move_forward, "u")
# window.onkeypress(move_backward, "j")
# window.onkeypress(move_right, "k")
# window.onkeypress(move_left, "h")


go_apple()

window.mainloop()

