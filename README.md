# Prodigy InfoTech - Cyber Security Internship

Official consolidated project repository for the **Prodigy InfoTech Cyber Security Internship** completed by **Jeeviraj V** ([@jeevicyber28](https://github.com/jeevicyber28)).

This repository consolidates all 4 practical internship tasks into a structured, unified portfolio covering classical cryptography, image encryption, authentication security, and ethical keystroke logging.

---

## 📋 Task Index & Portfolio Overview

| Task | Directory | Script | Core Concepts | Status |
|---|---|---|---|---|
| **Task 01** | [`Task_01_Caesar_Cipher/`](Task_01_Caesar_Cipher/) | `caesar_cipher.py` | Classical Cryptography, Modular Arithmetic, Substitution Ciphers | Completed |
| **Task 02** | [`Task_02_Pixel_Manipulation/`](Task_02_Pixel_Manipulation/) | `main.py` | Image Cryptography, Pixel Byte Swapping, XOR Encryption | Completed |
| **Task 03** | [`Task_03_Password_Complexity_Checker/`](Task_03_Password_Complexity_Checker/) | `password_checker.py` | Authentication Security, Regex Pattern Matching, Entropy Analysis | Completed |
| **Task 04** | [`Task_04_Simple_Keylogger/`](Task_04_Simple_Keylogger/) | `keylogger.py` | Keystroke Telemetry, Pynput Event Listeners, Ethical Security Auditing | Completed |

---

## 📂 Repository Architecture

```text
PRODIGY_CS/
├── README.md
├── Task_01_Caesar_Cipher/
│   ├── caesar_cipher.py              # Interactive encryption & decryption CLI
│   ├── README.md                     # In-depth Caesar cipher documentation
│   └── LICENSE                       # MIT License
├── Task_02_Pixel_Manipulation/
│   ├── main.py                       # Image pixel encryption/decryption engine
│   ├── encrypted.png                 # Sample encrypted image output
│   ├── decrypted.png                 # Restored decrypted image verification
│   └── README.md                     # Mathematical explanation of pixel operations
├── Task_03_Password_Complexity_Checker/
│   ├── password_checker.py           # Password strength evaluator & scoring logic
│   └── README.md                     # Password security guidelines & criteria
└── Task_04_Simple_Keylogger/
    ├── keylogger.py                  # Educational keystroke logging listener
    ├── keylog.txt                    # Sample captured keystrokes log
    ├── requirements.txt              # pynput dependency specification
    └── README.md                     # Ethical usage & security disclosure
```

---

## 🛠️ Task Summaries & Execution

### 1. Task 01: Caesar Cipher
- **Overview:** Educational Python implementation of the classical Caesar substitution cipher.
- **Features:** Custom shift value, wrap-around modular arithmetic (`% 26`), preservation of case, numbers, and punctuation.
- **Run Command:**
  ```bash
  python Task_01_Caesar_Cipher/caesar_cipher.py
  ```

---

### 2. Task 02: Pixel Manipulation for Image Encryption
- **Overview:** Custom image encryption tool that manipulates pixel values using mathematical operations (XOR & byte transposition).
- **Features:** Encrypts standard image files (`PNG`, `JPG`) into an unreadable scrambled form and cleanly reverses the operation back to the original image using a secret numeric key.
- **Run Command:**
  ```bash
  python Task_02_Pixel_Manipulation/main.py
  ```

---

### 3. Task 03: Password Complexity Checker
- **Overview:** Security utility that evaluates the strength of a user-supplied password based on established NIST and OWASP standards.
- **Features:** Checks length (minimum 8/12 characters), uppercase/lowercase letters, digits, and special characters. Provides feedback on weak patterns and score ratings (*Weak*, *Moderate*, *Strong*, *Very Strong*).
- **Run Command:**
  ```bash
  python Task_03_Password_Complexity_Checker/password_checker.py
  ```

---

### 4. Task 04: Simple Keylogger
- **Overview:** Educational keystroke logging utility designed for penetration testing and endpoint monitoring awareness.
- **Features:** Captures user keystrokes in real time using the `pynput` library and persists them into a structured log file (`keylog.txt`).
- **Ethical Disclaimer:** Developed strictly for authorized educational research and defensive endpoint telemetry analysis.
- **Run Command:**
  ```bash
  pip install -r Task_04_Simple_Keylogger/requirements.txt
  python Task_04_Simple_Keylogger/keylogger.py
  ```

---

## 👤 Author & Credentials

- **Intern:** Jeeviraj V
- **Organization:** Prodigy InfoTech
- **Domain:** Cyber Security
- **GitHub:** [https://github.com/jeevicyber28](https://github.com/jeevicyber28)
- **Repository:** [https://github.com/jeevicyber28/PRODIGY_CS](https://github.com/jeevicyber28/PRODIGY_CS)
