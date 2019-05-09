# I have added few comments, feel free to delete them after making the changes. I would recommend not having spaces in the filename! 

from sense_hat import SenseHat
# SEnseHat() should be SenseHat() the "e" should be lowercase
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

# this part was indented too much, it doesn't need to be indented! 
sense.set_pixels(crescent_moon)
