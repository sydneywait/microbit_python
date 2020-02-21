from microbit import *

while True:
    if button_b.is_pressed() and button_a.is_pressed():
        display.show('C')
    elif button_a.is_pressed():
        display.show('A')
    elif button_b.is_pressed():
        display.show('B')
    else:
        display.show(Image.SAD)

display.clear()
