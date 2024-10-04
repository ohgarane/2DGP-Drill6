from pico2d import *
import random
import math

pointX = random.randint(0, 800)
pointY = random.randint(0, 600)

open_canvas(800, 600)
character = load_image('animation_sheet.png')
ground = load_image('TUK_GROUND_FULL.png')
hand = load_image('hand_arrow.png')

running = True
frame = 0
characterX, characterY = 400, 300
speed = 2
direction = 1

while running:
    dx = pointX - characterX
    dy = pointY - characterY
    distance = math.sqrt(dx ** 2 + dy ** 2)

    if distance > 0:
        move_x = speed * (dx / distance)
        move_y = speed * (dy / distance)

        characterX += move_x
        characterY += move_y

        if move_x > 0:
            direction = 1
        elif move_x < 0:
            direction = -1

    if distance < 5:
        pointX = random.randint(0, 800)
        pointY = random.randint(0, 600)

    clear_canvas()

    ground.draw(400, 300, 800, 600)
    hand.draw(pointX, pointY)

    if direction == 1:
        character.clip_draw(frame * 100, 100, 100, 100, characterX, characterY)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, characterX, characterY)

    update_canvas()
    frame = (frame + 1) % 8

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

    delay(0.01)

close_canvas()
