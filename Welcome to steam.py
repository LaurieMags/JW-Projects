from sense_hat import SenseHat
sense = SEnseHat()

sense.show_message("Welcome to Joe Walker STEAM Night!")
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = (255, 255, 0)
b = (0, 0, 0)

crescent_moon = [ 
    b, b, y, y, y, y, b, b,
    b, y, y, y, b, b, b, b,
    y, y, y, b, b, b, b, b, 
    y, y, b, b, b, b, b, b,
    y, y, b, b, b, b, b, b,
    y, y, y, b, b, b, b, b,
    b, y, y, y, b, b, b, b,
    b, b, y, y, y, y, b, b,
]

    sense.set_pixels(crescent_moon)
