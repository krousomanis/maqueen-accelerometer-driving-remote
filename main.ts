radio.setGroup(89)
basic.showIcon(IconNames.Diamond)
basic.forever(function () {
    radio.sendValue("mgx", input.acceleration(Dimension.X))
    radio.sendValue("mgy", input.acceleration(Dimension.Y))
})
