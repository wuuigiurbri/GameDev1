import random
import pgzrun



WIDTH, HEIGHT = 1080, 520
WIN_SCORE = 10
PADDLE_SPEED = 6

game_over = False
winner = ""

player = Rect(0, 0, 10, 100)
player.center = (WIDTH - 100, HEIGHT / 2)

opponent = Rect(0, 0, 10, 100)
opponent.center = (100, HEIGHT / 2)

ball = Rect(0, 0, 20, 20)
ball.center = (WIDTH / 2, HEIGHT / 2)

x_speed, y_speed = 1, 1
player_score, opponent_score = 0, 0


def reset_ball():
    global x_speed, y_speed
    ball.center = (WIDTH / 2, HEIGHT / 2)
    x_speed = random.choice([1, -1])
    y_speed = random.choice([1, -1])


def reset_game():
    global game_over, winner, player_score, opponent_score, x_speed, y_speed
    game_over = False
    winner = ""
    player_score = 0
    opponent_score = 0
    reset_ball()


def check_for_winner():
    global game_over, winner
    if player_score >= WIN_SCORE:
        game_over = True
        winner = "Player"
    elif opponent_score >= WIN_SCORE:
        game_over = True
        winner = "Opponent"


def update():
    global x_speed, y_speed, player_score, opponent_score

    if game_over:
        if keyboard.r:
            reset_game()
        return

    if keyboard.w and opponent.top > 0:
        opponent.y -= PADDLE_SPEED
    if keyboard.s and opponent.bottom < HEIGHT:
        opponent.y += PADDLE_SPEED
    if keyboard.up and player.top > 0:
        player.y -= PADDLE_SPEED
    if keyboard.down and player.bottom < HEIGHT:
        player.y += PADDLE_SPEED

    if ball.top <= 0:
        ball.y = 0
        y_speed = abs(y_speed)
    if ball.bottom >= HEIGHT:
        ball.y = HEIGHT - ball.height
        y_speed = -abs(y_speed)

    if ball.left <= 0:
        player_score += 1
        check_for_winner()
        if not game_over:
            reset_ball()
    elif ball.right >= WIDTH:
        opponent_score += 1
        check_for_winner()
        if not game_over:
            reset_ball()

    if ball.colliderect(player):
        ball.x = player.left - ball.width
        x_speed = -abs(x_speed)
    elif ball.colliderect(opponent):
        ball.x = opponent.right
        x_speed = abs(x_speed)

    ball.x += x_speed * 2
    ball.y += y_speed * 2


def draw():
    screen.fill("black")

    for y in range(0, HEIGHT, 20):
        screen.draw.filled_rect(Rect(WIDTH / 2 - 2, y, 4, 12), "white")

    screen.draw.filled_rect(player, "white")
    screen.draw.filled_rect(opponent, "white")
    screen.draw.filled_circle((ball.centerx, ball.centery), 10, "white")
    screen.draw.text(str(player_score), (WIDTH / 2 + 80, 50), color="white", fontsize=60)
    screen.draw.text(str(opponent_score), (WIDTH / 2 - 80, 50), color="white", fontsize=60)

    if game_over:
        screen.draw.text(f"{winner} wins!", (WIDTH / 2 - 150, HEIGHT / 2 - 60), color="white", fontsize=60)
        screen.draw.text("Press R to play again", (WIDTH / 2 - 220, HEIGHT / 2 + 30), color="white", fontsize=30)


pgzrun.go()