#!/usr/bin/env python3

# Bibliotheken laden
from gpiozero import OutputDevice, LED, Button
from time import sleep

keypad_rows = [14, 15, 18, 23]
keypad_columns = [24, 25, 7, 8]

row_leds = [LED(pin) for pin in keypad_rows]
col_buttons = [Button(pin) for pin in keypad_columns]
matrix_keys = [['1', '2', '3', 'A'],
		['4', '5', '6', 'B'],
		['7', '8', '9', 'C'],
		['*', '0', '#', 'D']]

not_pressed_keys = set([])

row1 = set([0, 1, 2, 3])

def scankeys():  
	for row, row_led in enumerate(row_leds):
		row_leds[row].on()
		for col, col_button in enumerate(col_buttons):
			if col_button.is_pressed:
				not_pressed_keys.add(row)
				if(len(not_pressed_keys) == 3):
					pressed_row = set(row1) - set(not_pressed_keys)
					print('Pressed: ', matrix_keys[sum(pressed_row)][col])
					pressed_key = matrix_keys[sum(pressed_row)][col]
					pressed_row.clear()
					not_pressed_keys.clear()
					if(pressed_key == '1'):
						enableStepper1()
					elif(pressed_key == '2'):
						enableStepper2()
					elif(pressed_key == '3'):
						enableStepper3()
					elif(pressed_key == '4'):
						enableStepper4()
					elif(pressed_key == '5'):
						enableStepper5()
					elif(pressed_key == '6'):
						enableStepper6()
					elif(pressed_key == '7'):
						enableStepper7()
					elif(pressed_key == '8'):
						enableStepper8()
					sleep(1)
					#runStepper(num_rotations)
					disableAll()
					sleep(0.5)
		row_leds[row].off()

# Initialisierung von GPIO17 als LED (Ausgang)
relayarray1 = OutputDevice(17)
relayarray2 = OutputDevice(27)
relayarray3 = OutputDevice(22)
relayarray4 = OutputDevice(10)
relayarray5 = OutputDevice(9)
relayarray6 = OutputDevice(11)
relayarray7 = OutputDevice(5)
relayarray8 = OutputDevice(6)

# GPIO-Pins festlegen
enable_pin = 26
puls_pin = 19
direction_pin = 13

# GPIO-Objekte erstellen
enable = OutputDevice(enable_pin)
puls = OutputDevice(puls_pin)
direction = OutputDevice(direction_pin)

steps_per_rotation = 1600  # Schritte pro Umdrehung

relayarray1.on()
relayarray2.on()
relayarray3.on()
relayarray4.on()
relayarray5.on()
relayarray6.on()
relayarray7.on()
relayarray8.on()

def disableAll():
	relayarray1.on()
	relayarray2.on()
	relayarray3.on()
	relayarray4.on()
	relayarray5.on()
	relayarray6.on()
	relayarray7.on()
	relayarray8.on()

def enableStepper1():
    disableAll()
    relayarray1.off()

def enableStepper2():
    disableAll()
    relayarray2.off()

def enableStepper3():
    disableAll()
    relayarray3.off()

def enableStepper4():
    disableAll()
    relayarray4.off()

def enableStepper5():
    disableAll()
    relayarray5.off()

def enableStepper6():
    disableAll()
    relayarray6.off()

def enableStepper7():
    disableAll()
    relayarray7.off()

def enableStepper8():
    disableAll()
    relayarray8.off()

def runStepper(num_rotations):
	sleep(0.5)
	for _ in range(num_rotations * steps_per_rotation):
		puls.on()
		sleep(0.0005)
		puls.off()
		sleep(0.0005)
	sleep(0.5)

def error():
	#todo blink or something
	print('error')

direction.on()
num_rotations = 2

while(True):
	try:
		scankeys()

	except KeyboardInterrupt:
		sys.exit()
