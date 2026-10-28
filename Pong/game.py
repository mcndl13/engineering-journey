from time import sleep

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from settings import HEIGHT, WIDTH


STARTING_POSITIONS = [((-WIDTH // 2) + 25, 0), ((WIDTH // 2) - 25, 0)]


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.left_paddle = Paddle(STARTING_POSITIONS[0])
        self.right_paddle = Paddle(STARTING_POSITIONS[1])
        self.ball = Ball(WIDTH, HEIGHT)
        self.scoreboard = ScoreBoard()
        self.is_running = False
        self._bind_controls()

    def _bind_controls(self):
        self.screen.listen()
        self.screen.onkeypress(self.left_paddle.up, key="w")
        self.screen.onkeyrelease(self.left_paddle.release_up, key="w")
        self.screen.onkeypress(self.left_paddle.down, key="s")
        self.screen.onkeyrelease(self.left_paddle.release_down, key="s")
        self.screen.onkeypress(self.right_paddle.up, key="Up")
        self.screen.onkeyrelease(self.right_paddle.release_up, key="Up")
        self.screen.onkeypress(self.right_paddle.down, key="Down")
        self.screen.onkeyrelease(self.right_paddle.release_down, key="Down")

    def run(self):
        self.is_running = True
        while self.is_running:
            sleep(0.1)
            self.screen.update()
            self.ball.move()
            self._move_paddles()
            self._handle_wall_collision()
            self._handle_paddle_collision()
            self._handle_scoring()

            if self.scoreboard.l_score >= 10 or self.scoreboard.r_score >= 10:
                self.scoreboard.game_over()
                self.is_running = False

    def _move_paddles(self):
        if self.left_paddle.moving_up:
            self.left_paddle.up()
        if self.left_paddle.moving_down:
            self.left_paddle.down()
        if self.right_paddle.moving_up:
            self.right_paddle.up()
        if self.right_paddle.moving_down:
            self.right_paddle.down()

    def _handle_wall_collision(self):
        if (self.ball.ycor() + 15 >= HEIGHT // 2
                or self.ball.ycor() - 15 <= -HEIGHT // 2):
            self.ball.bounce_y()

    def _handle_paddle_collision(self):
        if (self.ball.move_x < 0 and self.ball.distance(self.left_paddle) < 25
                and abs(self.ball.ycor() - self.left_paddle.ycor()) <= 50):
            self.ball.bounce_x()

        if (self.ball.move_x > 0 and self.ball.distance(self.right_paddle) < 25
                and abs(self.ball.ycor() - self.right_paddle.ycor()) <= 50):
            self.ball.bounce_x()

    def _handle_scoring(self):
        if self.ball.xcor() < -WIDTH // 2:
            self.scoreboard.point(self.right_paddle.player)
            self._reset_ball_after_point()

        if self.ball.xcor() > WIDTH // 2:
            self.scoreboard.point(self.left_paddle.player)
            self._reset_ball_after_point()

    def _reset_ball_after_point(self):
        self.ball.reset_position()
        self.screen.update()
        sleep(2)
        self.ball.bounce_x()

    def reset(self):
        self.scoreboard.l_score = 0
        self.scoreboard.r_score = 0
        self.scoreboard.update_score()
        self.left_paddle.goto(STARTING_POSITIONS[0])
        self.right_paddle.goto(STARTING_POSITIONS[1])
        self.left_paddle.release_up()
        self.left_paddle.release_down()
        self.right_paddle.release_up()
        self.right_paddle.release_down()
        self.ball.reset_position()
        self.screen.update()
