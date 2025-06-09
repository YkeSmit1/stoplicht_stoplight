input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    state = GREENLIGHT
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    state = REDLIGHT
    basic.showIcon(IconNames.No)
})
let REDLIGHT = 0
let GREENLIGHT = 0
let state = 0
state = 0
GREENLIGHT = 1
REDLIGHT = 2
radio.setGroup(1)
basic.forever(function on_forever() {
    radio.sendNumber(state)
})
