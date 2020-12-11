import pgzrun

WIDTH = 1000
HEIGHT = 700
COLOUR = (0, 0, 250)
ball = Actor("ball")
paddle = Actor("paddle")
ball_x_speed = 5
ball_y_speed = 5
missed = False
score = 0

def draw():
    screen.fill(COLOUR)
    ball.draw()
    paddle.draw()
    draw_score()


def update():
    if not missed:
        animate_ball()


def animate_ball():
    ball.y += ball_y_speed
    ball.x += ball_x_speed
    check_boundaries()
    check_collision()
    check_paddle_miss()


def check_boundaries():
    global ball_x_speed, ball_y_speed
    if ball.right > WIDTH or ball.left < 0:
        ball_x_speed *= -1
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_y_speed *= -1


def on_mouse_move(pos):
    paddle.x = pos[0]
    if paddle.left < 0:
        paddle.left = 0
    elif paddle.right > WIDTH:
        paddle.right = WIDTH


def position_objects():
    paddle.bottom = HEIGHT
    paddle.left = 0


def check_collision():
    global ball_y_speed, score
    if ball.colliderect(paddle):
        ball_y_speed *= -1
        score += 100


def check_paddle_miss():
    global missed
    if ball.bottom > paddle.top + 5:
        missed = True


def draw_score():
    screen.draw.text("Score: "+str(score), (10,10), fontsize=30, color="white")
    if missed:
        position = ((WIDTH // 2)-100, HEIGHT // 2)
        screen.draw.text("OOPS!!! Missed it!!! ", position, fontsize=50, color="red")

position_objects()
pgzrun.go()