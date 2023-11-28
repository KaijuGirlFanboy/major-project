function twornLeft () {
    basic.showArrow(ArrowNames.East)
    motion.turnLeft(60)
    basic.pause(300)
    motion.stop()
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    movement = false
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0 && movement == false) {
        moveForwards()
    } else if (receivedNumber == 0 && movement == true) {
        brake()
    } else if (receivedNumber == 1) {
        twornLeft()
    } else if (receivedNumber == 2) {
        twornRight()
    } else if (receivedNumber == 3) {
        moveBack()
    }
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    radio.sendNumber(3)
})
function moveForwards () {
    basic.showArrow(ArrowNames.South)
    movement = true
    motion.drive(45, 52)
}
function twornRight () {
    basic.showArrow(ArrowNames.West)
    motion.turnRight(40)
    basic.pause(300)
    motion.stop()
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    movement = false
}
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
})
function moveBack () {
    music.setVolume(255)
    motion.stop()
    basic.showArrow(ArrowNames.North)
    basic.pause(200)
    motion.drive(-32, -28)
    music.play(music.stringPlayable("G - G - G - G - ", 300), music.PlaybackMode.LoopingInBackground)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    motion.stop()
    music.stopAllSounds()
    movement = false
}
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(0)
})
radio.onReceivedString(function (receivedString) {
    playTokyo()
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
})
function brake () {
    leftWheel = 40
    rightWheel = 55
    basic.showIcon(IconNames.Asleep)
    for (let index = 0; index < 10; index++) {
        motion.drive(leftWheel, rightWheel)
        rightWheel += -5.5
        leftWheel += -4
        basic.pause(40)
    }
    motion.stop()
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    movement = false
}
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    timer += 1
})
function playTokyo () {
    music.setVolume(255)
    music.play(music.stringPlayable("B A G A G F A C5 ", 212), music.PlaybackMode.LoopingInBackground)
    basic.pause(5000)
    music.stopAllSounds()
}
let timer = 0
let rightWheel = 0
let leftWheel = 0
let movement = false
radio.setGroup(21)
basic.forever(function () {
    if (timer == 3) {
        radio.sendString("Tokyo")
        playTokyo()
    }
})
basic.forever(function () {
    basic.pause(1000)
    timer = 0
})
basic.forever(function () {
    while (movement == true) {
        if (sonar.checkSonar() < 15) {
            moveBack()
        }
    }
})
