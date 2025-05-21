# Keylogger

This project is a **Python-based keylogger** designed for **learning and ethical research** purposes. It captures keyboard inputs, logs them in sentence format, records active window titles, and includes timestamps. It runs in the background and stops when the **ESC key** is pressed.

---

## Features

- Logs keystrokes in real-time
- Records inputs in **sentence format**
- Tracks and logs **active window titles**
- Adds **timestamps** for each sentence
- Stops safely with the **ESC** key
- Stores logs in a local file (`keylog.txt`)

---

## Learning Objectives

- Understand how keylogging works for endpoint monitoring
- Work with Python modules like `pynput` and `win32gui`
- Gain insights into user behavior and window focus
- Learn about ethical boundaries in cybersecurity

---

## What's Included

- `keylogger.py` – The main script to run the logger
- `keylog.txt` – Log file generated during execution
- `README.md` – Project overview and instructions

---

## Requirements

- Python 3.x
- Required modules:
  pip install pynput pywin32


---

## How to Run

1. Clone or download this repository:

   git clone https://github.com/your-username/keylogger-project
   
   cd keylogger-project

3. Run the keylogger:

   python keylogger.py


4. Type anything. The logger will:
   - Group your typing into sentences
   - Record the active window
   - Log with timestamps

5. Press `ESC` to stop the logger.

6. View logs in `keylog.txt`.

---

## Ethical Disclaimer

This tool is intended **only for educational and ethical testing** on systems you own or have permission to use.  
**Do not deploy on unauthorized devices**. Misuse may violate laws and ethical guidelines.

---

## Future Improvements 

- Auto-email the log file periodically
- Run in background on startup
- Add clipboard monitoring
- Cross-platform support (Linux/macOS)

---

## Author

**Tanazzah Shaikh**  
Cybersecurity Student & Enthusiast  
GitHub: [@tanazzahh](https://github.com/tanazzahh)

---
