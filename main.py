def on_button_pressed_a():
    global state
    state = GREENLIGHT
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global state
    state = REDLIGHT
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

REDLIGHT = 0
GREENLIGHT = 0
state = 0
state = 0
GREENLIGHT = 1
REDLIGHT = 2
radio.set_group(1)

def on_forever():
    radio.send_number(state)
basic.forever(on_forever)
