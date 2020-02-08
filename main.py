import arcade

# create screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "pyGame")
arcade.set_background_color(arcade.color.BLACK)


def draw_face(mainX, mainY):
    # BODY
    ballX = mainX
    ballY = mainY
    ballSize = SCREEN_WIDTH * (2/10)
    arcade.draw_circle_filled(ballX, ballY, ballSize, arcade.color.YELLOW)

    # LEFT EYE
    eyeX = ballX - ballX * (1/10)
    eyeY = ballY + ballY * (1/10)
    eyeSize = ballSize * (2/10)
    arcade.draw_circle_filled(eyeX, eyeY, eyeSize, arcade.color.BLACK)

    # LEFT EYE (small)
    eye2X = eyeX + eyeX * (3/100)
    eye2Y = eyeY
    eye2Size = eyeSize * (1/3)
    arcade.draw_circle_filled(eye2X, eye2Y, eye2Size, arcade.color.WHITE)

    # RIGHT EYE
    eyeX = ballX + ballX * (1/10)
    eyeY = ballY + ballY * (1/10)
    eyeSize = ballSize * (2/10)
    arcade.draw_circle_filled(eyeX, eyeY, eyeSize, arcade.color.BLACK)

    # RIGHT EYE (small)
    eye2X = eyeX + eyeX * (3/100)
    eye2Y = eyeY
    eye2Size = eyeSize * (1/3)
    arcade.draw_circle_filled(eye2X, eye2Y, eye2Size, arcade.color.WHITE)

    # MOUTH
    mouthX = ballX
    mouthY = ballY - (1/10) * ballY
    mouthWidth = ballSize + ballSize * (1/10)
    mouthHeight = mouthWidth * (1/3)
    arcade.draw_ellipse_filled(mouthX, mouthY, mouthWidth,
                               mouthHeight, arcade.color.RED)


def main():
    arcade.start_render()
    # reset the screen - start draw -----------------------------

    draw_face(50, 50)

    # end draw --------------------------------------------------
    arcade.finish_render()

    # run
    arcade.run()


if __name__ == "__main__":
    main()
