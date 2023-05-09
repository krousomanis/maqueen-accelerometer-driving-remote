radio.set_group(89)
basic.show_icon(IconNames.DIAMOND)

def on_forever():
    radio.send_value("mgx", input.acceleration(Dimension.X))
    radio.send_value("mgy", input.acceleration(Dimension.Y))
basic.forever(on_forever)
