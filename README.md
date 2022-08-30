# vive la resolution
<img width="70px" src="icon.ico"/>
Quick display resolution detect and switch

## to use

launch program the first time.

it will generate `res.dat` file with all possible resolutions for your main display.

edit this file with your favourite text editor and remove all lines except resolutions between which you wnat to switch.

launch program the second time.

## to build

install Python, make sure that python, pip and pip packages are in environment PATH.

launch `build.bat`

## notes

- app detects possible resolution for display and detects current resolution
- if file exists, it reads the list of resolutions nad searches for current
- if it is present, it switches to the next
- if it is not present or is last in the list, it switches to the first

## todo

- display frequency and stretch
- display number select, multidisplay
