import os
import time

INPUT_FILE = "/Users/tomastovey/Documents/telegram-voice-bot/commands.txt"
CURSOR_FILE = "/Users/tomastovey/Documents/telegram-voice-bot/cursor_commands.txt"

def read_file():
    with open(INPUT_FILE, "r") as f:
        return f.read().strip()

def clear_file():
    with open(INPUT_FILE, "w") as f:
        f.write("")

last_text = ""

print("👀 Watching for new voice commands...")

while True:
    if os.path.exists(INPUT_FILE):
        current_text = read_file()
        if current_text and current_text != last_text:
            try:
                print(f"📨 Writing to Cursor: {current_text}")
                with open(CURSOR_FILE, "w") as f:
                    f.write(current_text)
                last_text = current_text
                clear_file()
            except Exception as e:
                print(f"❌ Error: {e}")
    time.sleep(1)

