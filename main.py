music.set_volume(150)

def on_forever():
    serial.write_number(pins.analog_read_pin(AnalogReadWritePin.P2))
    serial.write_line("")
    basic.pause(10)
    music.ring_tone(pins.analog_read_pin(AnalogReadWritePin.P2))
basic.forever(on_forever)
