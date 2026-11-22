# 🔐 Simple Python Keylogger

### Educational Cybersecurity Project

A simple Python-based keyboard event monitoring project built for **cybersecurity education, Python practice, and controlled laboratory demonstrations**.

> ⚠️ **Educational & Authorized Use Only**
>
> This project must only be used on systems that you own or have explicit permission to monitor. Never use it for covert surveillance, credential theft, or unauthorized data collection.

---

## 📌 Overview

**Simple Python Keylogger** demonstrates how a Python application can listen for keyboard events and record them locally in a text file.

The project focuses on understanding:

* ⌨️ Keyboard event listeners
* 🔄 Callback-based programming
* 🕒 Timestamp generation
* 📝 Local text-file logging
* 🔑 Normal and special keyboard keys
* 🛡️ Privacy and security considerations

The program records ordinary characters and named special keys such as:

`Space` • `Enter` • `Backspace` • `Shift` • `Esc`

Each event is stored with a timestamp so that students can understand how keyboard events are detected and logged.

---

## ✨ Features

* 🐍 Built with Python
* ⌨️ Keyboard event monitoring using `pynput`
* 📝 Local event logging
* 🕒 Timestamp for every recorded event
* 🔑 Supports character and special keys
* 🖥️ Displays events in the terminal
* 📂 Automatically creates a session header
* ⏱️ Three-second startup countdown
* 🛑 Escape key stops the listener
* 📍 Displays the absolute path of the log file
* 🔤 UTF-8 encoded output
* 🌐 Cross-platform library support

---

## 🛠️ Technology Stack

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| **Python 3.8+** | Main programming language |
| **pynput**      | Keyboard event monitoring |
| **datetime**    | Timestamp generation      |
| **os**          | File path handling        |
| **Text File**   | Local event storage       |

---

## 📁 Project Structure

```text
PRODIGY_CS_04/
│
├── keylogger.py       # Main educational keylogger program
├── requirements.txt   # Python dependencies
├── keylog.txt         # Local test output
├── README.md          # Project documentation
└── .gitignore         # Prevents logs and virtual environments from being committed
```

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python **3.8 or newer**
* `pip`
* Terminal / Command Prompt
* An authorized test machine
* Permission to monitor keyboard events

Some operating systems may require additional permissions for keyboard monitoring.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/jeevicyber28/PRODIGY_CS_04.git
cd PRODIGY_CS_04
```

## 2. Create a Virtual Environment

Creating a virtual environment keeps the project's dependencies isolated.

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The project uses the `pynput` package for keyboard event handling.

---

# ▶️ Usage

Run the program from the project directory:

```bash
python keylogger.py
```

The application displays an educational-use warning and starts a short countdown.

After the countdown:

1. Type harmless test data.
2. Observe the keyboard events displayed in the terminal.
3. Press **Esc** to stop the listener.
4. Open `keylog.txt` to inspect the generated test log.

### Example Test Input

```text
hello123
```

> Never type real passwords, API keys, credit-card numbers, private messages, or other sensitive information during testing.

---

# 🖥️ Example Terminal Output

```text
============================================================
        SIMPLE KEYLOGGER - EDUCATIONAL PURPOSE ONLY
============================================================

[!] IMPORTANT: Ensure you have permission to run this program!

[+] Logging keystrokes to:
    /path/to/PRODIGY_CS_04/keylog.txt

[+] Press ESC to stop the keylogger

Starting in 3 seconds...

Key pressed: h
Key pressed: e
Key pressed: l
Key pressed: l
Key pressed: o
Special key pressed: space
Key pressed: 1
Key pressed: 2
Key pressed: 3

[!] Escape key pressed. Stopping keylogger...

[+] Logs saved to:
    /path/to/PRODIGY_CS_04/keylog.txt

[+] Keylogger stopped successfully!
```

---

# 📝 Example Log Format

```text
==================================================
Keylogger Session Started: 2026-01-01 10:30:00
==================================================

[2026-01-01 10:30:03] Key pressed: h
[2026-01-01 10:30:03] Key pressed: e
[2026-01-01 10:30:03] Key pressed: l
[2026-01-01 10:30:03] Key pressed: l
[2026-01-01 10:30:04] Key pressed: o
[2026-01-01 10:30:04] Special key pressed: space
[2026-01-01 10:30:05] Special key pressed: enter
```

---

# 🧠 How It Works

The program follows a simple event-driven workflow:

```text
Keyboard Input
      │
      ▼
pynput Listener
      │
      ▼
  on_press()
      │
      ├── Character Key
      │       └── Record Character
      │
      └── Special Key
              └── Record Key Name
      │
      ▼
Add Timestamp
      │
      ▼
Write to keylog.txt
      │
      ▼
Press ESC
      │
      ▼
Stop Listener
```

### Main Components

**`on_press()`**

Called whenever a keyboard key is pressed.

**Character handling**

Character keys are read using the key's character representation.

**Special-key handling**

Keys without a character representation are handled separately and recorded using readable names.

**`get_timestamp()`**

Generates timestamps using the format:

```text
YYYY-MM-DD HH:MM:SS
```

**`on_release()`**

Checks whether the released key is `Esc`.

When `Esc` is released, the listener stops.

**`main()`**

Controls the startup message, countdown, session initialization, listener execution, and shutdown.

---

# 🔧 Configuration

The output file is configured in `keylogger.py`:

```python
LOG_FILE = "keylog.txt"
```

For a controlled laboratory experiment, this can be changed to another test-only filename.

Avoid using locations that contain important, private, or synchronized data.

---

# 🧪 Safe Demonstration Procedure

For a classroom or cybersecurity lab demonstration:

1. Use a disposable virtual machine or dedicated test account.
2. Make sure the machine is authorized for the experiment.
3. Close applications containing confidential information.
4. Do **not** enter real passwords or sensitive information.
5. Enter only synthetic test data.
6. Observe the terminal output.
7. Press **Esc** to stop the program.
8. Inspect the generated log.
9. Delete the test log after the demonstration.
10. Deactivate the virtual environment.

---

# ⚠️ Security & Privacy Warning

A keylogger can potentially capture extremely sensitive information, including:

* Passwords
* Authentication codes
* Private messages
* Payment information
* API keys
* Personal information

Therefore:

> **Only run this project with explicit authorization.**

Never:

* ❌ Run it secretly
* ❌ Deploy it on another person's computer
* ❌ Collect credentials
* ❌ Upload private logs
* ❌ Add credential-stealing functionality
* ❌ Add remote data exfiltration
* ❌ Add persistence or stealth mechanisms
* ❌ Attempt to bypass operating-system security controls

---

# 🔒 Protecting the Repository

Do not commit generated keylogs or Python cache files to Git.

Recommended `.gitignore`:

```gitignore
# Keylogger output
keylog.txt
*.log

# Python
__pycache__/
*.pyc

# Virtual environment
.venv/

# IDE
.vscode/
.idea/
```

Always check your repository before pushing changes.

---

# ⚠️ Current Limitations

This project is intentionally simple and has several limitations:

* Local text-file storage only
* No log encryption
* No automatic log rotation
* No graphical interface
* No active-application identification
* Keyboard layouts may affect character output
* Operating-system permissions may prevent monitoring
* No remote collection
* No authentication or access-control layer
* Not designed for background or stealth execution
* Not suitable for shared or production computers

---

# 🛡️ Defensive Cybersecurity Learning

This project can also be used to understand how defenders identify suspicious input-monitoring activity.

Possible defensive exercises include:

* Examining running processes
* Checking file permissions
* Reviewing startup entries
* Identifying unusual Python processes
* Studying endpoint-security alerts
* Designing data-retention policies
* Creating incident-response procedures
* Understanding secure deletion
* Discussing consent and privacy requirements

---

# 💡 Safe Future Improvements

Possible improvements for a controlled educational version include:

* ✅ Visible start/stop indicator
* ✅ Explicit consent confirmation
* ✅ Synthetic test-data mode
* ✅ Automatic test-log deletion
* ✅ Dry-run mode
* ✅ Structured JSON output
* ✅ Unit tests
* ✅ Log-size limits
* ✅ Better permission-error messages
* ✅ OS-specific documentation
* ✅ Instructor/student laboratory checklist

These improvements should preserve the project's **transparent, authorized, and educational** purpose.

---

# 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'pynput'`

Activate your virtual environment and reinstall the dependency:

```bash
python -m pip install -r requirements.txt
```

---

### Permission or display errors on Linux

Make sure you are running the project inside an authorized graphical test session.

Check your desktop environment's input-monitoring permissions.

Do not bypass security controls on systems you do not own.

---

### Listener does not stop

Release the **Esc** key rather than only pressing it.

You can also stop an authorized test run with:

```text
Ctrl + C
```

---

### Log file cannot be found

The program displays the absolute path of the generated log file when it stops.

Use that path to locate the file.

---

### Characters are different from what was typed

Keyboard layouts, modifiers, and operating-system mappings can affect the values returned by `pynput`.

Test using a simple keyboard layout and document the environment used for the experiment.

---

# ✅ Testing Checklist

Before demonstrating the project, verify:

* [ ] Python is installed
* [ ] Virtual environment is active
* [ ] Dependencies install successfully
* [ ] Test machine is authorized
* [ ] No sensitive information will be entered
* [ ] Listener starts correctly
* [ ] Character keys appear in the terminal
* [ ] Special keys are displayed correctly
* [ ] Esc stops the listener
* [ ] Output contains timestamps
* [ ] Test data is deleted after use

---

# 🤝 Contributing

Contributions are welcome when they improve:

* Documentation
* Testing
* Accessibility
* Error handling
* Safe defensive-security learning

Please **do not** contribute features designed for:

* Stealth
* Persistence
* Credential theft
* Remote exfiltration
* Security-control evasion
* Unauthorized surveillance

### Contribution Steps

```text
1. Fork the repository
2. Create a feature branch
3. Make a focused change
4. Test it in an isolated environment
5. Update the documentation
6. Create a pull request
```

---

# 📜 License

No license file is currently included in this repository.

Until a license is added by the repository owner, the source should be treated as **all-rights-reserved**.

Permission should be obtained before redistributing or modifying the project.

The educational and authorized-use requirements remain applicable.

---

# 👨‍💻 Author

Created by **jeevicyber28** as part of a cybersecurity learning project.

**Repository:**
`PRODIGY_CS_04`

---

# 🙏 Acknowledgements

* **Python** — Programming language
* **pynput** — Keyboard event API
* **Cybersecurity learning community** — Responsible security experimentation

---

# ⚖️ Ethical & Legal Notice

This project is provided for:

* 🎓 Educational purposes
* 🔬 Authorized security testing
* 🛡️ Defensive cybersecurity research
* 🧪 Controlled laboratory demonstrations

You are responsible for complying with all applicable laws, organizational policies, privacy requirements, and consent requirements.

Unauthorized keyboard monitoring may violate privacy, computer-misuse, data-protection, employment, or criminal laws.

The author and contributors are not responsible for misuse, unauthorized monitoring, data loss, or legal consequences.

---

# ⭐ Final Note

> **Learn how event listeners and local logging work — don't use them to monitor people.**

A strong cybersecurity project demonstrates not only technical skills, but also an understanding of **privacy, authorization, responsible disclosure, and ethical security practices**.

**Keep experiments transparent, authorized, local, and reversible.** 🔐
