music.setVolume(150)
basic.forever(function () {
    serial.writeNumber(pins.analogReadPin(AnalogReadWritePin.P2))
    serial.writeLine("")
    basic.pause(100)
    music.ringTone(pins.analogReadPin(AnalogReadWritePin.P2))
})
