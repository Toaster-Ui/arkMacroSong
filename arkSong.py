import keyboard
import time

print("STARTING!")
time.sleep(5)

# Global Variables
threePlays = ["apple", "banana", "cherry"]

# Crazy Fast is the one that is literally crazy fast, it goes budna bunna bun bun nunu nun.
def crazyFast():
    for x in threePlays:
        keyboard.press_and_release('5')
        time.sleep(.1)
        keyboard.press_and_release('4')
        time.sleep(.1)
        keyboard.press_and_release('3')
        time.sleep(.1)
        keyboard.press_and_release('1')
        time.sleep(.1)
        keyboard.press_and_release('5')
        time.sleep(.1)
        keyboard.press_and_release('4')
        time.sleep(.1)
        keyboard.press_and_release('3')
        time.sleep(.1)
        keyboard.press_and_release('1')
        time.sleep(.1)

        # Bum Bum Bum
        keyboard.press_and_release('5')
        time.sleep(.1)
        keyboard.press_and_release('5')
        time.sleep(.1)
        keyboard.press_and_release('5')
        time.sleep(.1)
        keyboard.press_and_release('5')
        time.sleep(.1)

# Start
crazyFast()





