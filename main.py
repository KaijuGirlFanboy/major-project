def twornLeft():
    global movement
    basic.show_arrow(ArrowNames.EAST)
    motion.turn_left(60)
    basic.pause(300)
    motion.stop()
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    movement = False

def on_received_number(receivedNumber):
    if receivedNumber == 0 and movement == False:
        moveForwards()
    elif receivedNumber == 0 and movement == True:
        brake()
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif receivedNumber == 1:
        twornLeft()
    elif receivedNumber == 2:
        twornRight()
    elif receivedNumber == 3:
        moveBack()
radio.on_received_number(on_received_number)

def on_logo_long_pressed():
    radio.send_number(3)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def moveForwards():
    global movement
    basic.show_arrow(ArrowNames.SOUTH)
    movement = True
    motion.drive(43, 55)
def twornRight():
    global movement
    basic.show_arrow(ArrowNames.WEST)
    motion.turn_right(40)
    basic.pause(300)
    motion.stop()
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    movement = False

def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def moveBack():
    global movement
    music.set_volume(255)
    motion.stop()
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(200)
    motion.drive(-32, -28)
    music.play(music.string_playable("G - G - G - G - ", 300),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    motion.stop()
    music.stop_all_sounds()
    movement = False

def on_button_pressed_ab():
    radio.send_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    playTokyo()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def brake():
    global leftWheel, rightWheel, movement
    leftWheel = 40
    rightWheel = 55
    basic.show_icon(IconNames.ASLEEP)
    for index in range(10):
        motion.drive(leftWheel, rightWheel)
        rightWheel += -5.5
        leftWheel += -4
        basic.pause(40)
    motion.stop()
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    movement = False

def on_logo_touched():
    global timer
    timer += 1
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def playTokyo():
    music.set_volume(255)
    music.play(music.string_playable("B A G A G F A C5 ", 212),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    basic.pause(5000)
    music.stop_all_sounds()
timer = 0
rightWheel = 0
leftWheel = 0
movement = False
radio.set_group(21)

def on_forever():
    while movement == True:
        if sonar.check_sonar() < 15:
            moveBack()
basic.forever(on_forever)

def on_forever2():
    global timer
    basic.pause(1000)
    timer = 0
basic.forever(on_forever2)

def on_forever3():
    if timer == 3:
        radio.send_string("Tokyo")
        playTokyo()
basic.forever(on_forever3)
