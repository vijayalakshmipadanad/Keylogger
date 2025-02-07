import keyboard

typed_text = ""  # Variable to store typed characters

def on_press_log(event):
    global typed_text  # Access the global variable
    key = event.name  # Get the pressed key

    # Print the name of the key pressed
    print(f"Key pressed: {key}")

    # Handle special cases like space, backspace, and enter
    if key == "space":
        typed_text += " "  # Add a space
    elif key == "backspace":
        typed_text = typed_text[:-1]  # Remove last character
    elif key == "enter":
        print("\n")  # Move to a new line
        typed_text = ""  # Clear after Enter
    elif len(key) == 1:  # Ensure it's a single character (avoiding shift, ctrl, etc.)
        typed_text += key  # Append key to the text

    # Print the current accumulated text dynamically
    print( + typed_text, end="", flush=True)

keyboard.on_press(on_press_log)
keyboard.wait()