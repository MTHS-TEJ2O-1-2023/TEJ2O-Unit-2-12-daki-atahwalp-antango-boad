/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Daki A.B
 * Created on: Oct 2023
 * This program turns neopixels red if sonar measures distance less than 10cm, and turns neopixels green if sonar measures more than 10cm
*/

// variables
let distanceFromObject: number = 0

// on startup
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// measuring distance with sonar
input.onButtonPressed(Button.A, function () {
  basic.clearScreen()
  distanceFromObject = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P2,
    PingUnit.Centimeters
)
  basic.showNumber(distanceFromObject)
  basic.showString('cm')
  basic.showIcon(IconNames.Happy)
})
