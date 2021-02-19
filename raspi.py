from sense_emu import SenseHat
sense=SenseHat()


def setup():
    sense.show_message("Ready")


def turn_on():
    sense.show_message("on")
    print ('led turned on >>>')


def turn_off():
    sense.show_message("off")
    print ('led turned off >>>')


def destroy():
    pass
