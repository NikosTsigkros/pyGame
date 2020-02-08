import arcade

# create screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "pyGame")
arcade.set_background_color(arcade.color.BLACK)

# reset the screen - start draw -----------------------------
arcade.start_render()

# BODY
ballX = SCREEN_WIDTH/2
ballY = SCREEN_HEIGHT/2
ballSize = SCREEN_WIDTH * 2/10
arcade.draw_circle_filled(ballX, ballY, ballSize, arcade.color.YELLOW)

# LEFT EYE
eyeX = ballX - (1/10) * ballX
eyeY = ballY + (1/10) * ballX
eyeSize = ballSize * 2/10
arcade.draw_circle_filled(eyeX, eyeY, eyeSize, arcade.color.BLACK)

# RIGHT EYE
eyeX = ballX + (1/10) * ballX
eyeY = ballY + (1/10) * ballX
eyeSize = ballSize * 2/10
arcade.draw_circle_filled(eyeX, eyeY, eyeSize, arcade.color.BLACK)

# MOUTH
mouthX = ballX
mouthY = ballY - 20
mouthWidth = 30
mouthHeight = 20
startMouth = 190
endMouth = 350
arcade.draw_arc_filled(mouthX, mouthY, mouthWidth,
                       mouthHeight, arcade.color.RED, startMouth, endMouth, 10)

# end draw --------------------------------------------------
arcade.finish_render()

# run
arcade.run()
