from pygame import *
from random import randint
win_width = 700
win_height = 500
display.set_caption("")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

speed_x = 3
speed_y = 3

while game:

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.x += speed_y

    if sprite.collide_rect(racket1, ball)
    or sprite.collide_rect(racket2, ball):
        speed_x*= -1



speed_x = 3
speed_y = 3

while game:

        ball.rect.x += speed_x
        ball.rect.x += speed_y

    if ball.rect.y > win_height-50
    or ball.rect.y < 0:
        speed_y*= -1




font = font.Font(None,35)
lose = font1.render()

