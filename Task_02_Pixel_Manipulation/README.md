# 🖼️ Image Encryption & Decryption Tool

A simple and educational **Python-based image encryption and decryption tool** that uses pixel manipulation to transform image data.

The project demonstrates how image pixels can be modified using a numerical key and restored using the reverse operation.

> ⚠️ **Educational Project:** This implementation is designed for learning image processing and basic encryption concepts. It is **not suitable for protecting sensitive images or real-world confidential data**.

---

## ✨ Features

* 🔐 Encrypt images using pixel manipulation
* 🔓 Decrypt encrypted images
* 🖼️ Supports PNG images
* 🎨 Processes RGB images
* 🌈 Handles RGBA images with transparency
* 🔢 Accepts a user-defined numerical key
* 🔄 Uses reversible pixel transformations
* 💾 Automatically saves encrypted and decrypted images
* 💻 Simple command-line interface
* 🐍 Built with Python
* 📦 Uses the Pillow image-processing library

---

## 🧠 How It Works

The program modifies the RGB values of every pixel using a numerical encryption key.

For encryption:

```text
New RGB Value = (Original RGB Value + Key) % 256
```

For decryption:

```text
Original RGB Value = (Encrypted RGB Value - Key) % 256
```

The modulo operation keeps every RGB value within the valid range:

```text
0 - 255
```

### Example

Suppose a pixel has:

```text
R = 100
G = 150
B = 200
```

With a key of `50`:

```text
R = (100 + 50) % 256 = 150
G = (150 + 50) % 256 = 200
B = (200 + 50) % 256 = 250
```

The encrypted pixel becomes:

```text
(150, 200, 250)
```

During decryption, the key is subtracted to restore the original values.

---

## 🛠️ Technology Stack

| Technology  | Purpose              |
| ----------- | -------------------- |
| Python 3.8+ | Programming language |
| Pillow      | Image processing     |
| Git         | Version control      |
| GitHub      | Source-code hosting  |

---

## 📁 Project Structure

```text
PRODIGY_CS_02/
│
├── main.py
├── encrypted.png
├── decrypted.png
└── README.md
```

---

## 📋 Requirements

* Python **3.8 or newer**
* Pillow
* Git (optional)

Install Pillow using:

```bash
pip install Pillow
```

If your system uses `python3`:

```bash
python3 -m pip install Pillow
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/jeevicyber28/PRODIGY_CS_02.git
```

Move into the project directory:

```bash
cd PRODIGY_CS_02
```

Install the required dependency:

```bash
pip install Pillow
```

---

## ▶️ Running the Program

Run the program:

```bash
python main.py
```

The program displays:

```text
1. Encrypt
2. Decrypt
```

Enter your choice:

```text
Enter choice: 1
```

Then provide the image path:

```text
Enter image path: input.png
```

Finally, enter a numerical key:

```text
Enter key (number): 50
```

---

## 🔐 Encrypting an Image

Select:

```text
1. Encrypt
```

Example:

```text
Enter choice: 1
Enter image path: input.png
Enter key (number): 50
```

The program processes each pixel and creates:

```text
encrypted.png
```

The encrypted image contains modified RGB values based on the selected key.

---

## 🔓 Decrypting an Image

To restore an encrypted image, select:

```text
2. Decrypt
```

Example:

```text
Enter choice: 2
Enter image path: encrypted.png
Enter key (number): 50
```

The program reverses the pixel transformation and creates:

```text
decrypted.png
```

For successful restoration, use the **same key** that was used during encryption.

---

## 🎨 RGB and RGBA Support

The implementation handles both RGB and RGBA pixels.

### RGB

```text
(R, G, B)
```

The red, green, and blue channels are transformed.

### RGBA

```text
(R, G, B, A)
```

The RGB channels are transformed while the alpha channel is preserved.

This allows images containing transparency to retain their alpha information.

---

## 🔄 Encryption Flow

```text
Input Image
     │
     ▼
Read Image Pixels
     │
     ▼
Read Encryption Key
     │
     ▼
Modify RGB Values
     │
     ▼
Apply % 256
     │
     ▼
Save encrypted.png
```

---

## 🔓 Decryption Flow

```text
Encrypted Image
      │
      ▼
Read Image Pixels
      │
      ▼
Read Same Encryption Key
      │
      ▼
Reverse RGB Transformation
      │
      ▼
Apply % 256
      │
      ▼
Save decrypted.png
```

---

## 🧪 Testing

Recommended test cases:

* Encrypt a normal PNG image
* Decrypt the encrypted image
* Use a small positive key
* Use a key greater than 255
* Use a key of `0`
* Test RGB images
* Test RGBA images
* Test different image sizes
* Test an invalid menu choice
* Test an invalid image path
* Verify that the decrypted image matches the original

### Basic Test

For example:

```text
Original Image
      ↓
   Encrypt
      ↓
encrypted.png
      ↓
   Decrypt
      ↓
decrypted.png
```

The final decrypted image should visually match the original image when the same key and compatible image format are used.

---

## ⚠️ Security Notice

This project is intended for **educational purposes only**.

The pixel transformation used here should **not be considered secure cryptography**.

Do not use this implementation to protect:

* Confidential photographs
* Personal documents
* Password-protected images
* Financial information
* Private data
* Sensitive business files

The algorithm is simple and does not provide the security properties expected from modern cryptographic systems.

For real-world image security, use established cryptographic algorithms and trusted cryptography libraries.

---

## 🚧 Limitations

* Designed primarily for educational use
* Uses a simple reversible pixel transformation
* Does not provide modern cryptographic security
* Does not authenticate encrypted data
* Does not provide integrity verification
* Requires the correct key for decryption
* Current interface is command-line based
* Invalid file paths may cause runtime errors
* The implementation currently focuses on image pixel manipulation

---

## 🔮 Future Improvements

Possible improvements include:

* [ ] Add input validation
* [ ] Add error handling for missing files
* [ ] Add support for more image formats
* [ ] Add a graphical user interface
* [ ] Add drag-and-drop image selection
* [ ] Add automated tests
* [ ] Add progress indicators for large images
* [ ] Add command-line arguments using `argparse`
* [ ] Add secure encryption using modern cryptographic algorithms
* [ ] Add password-based key derivation
* [ ] Add integrity verification
* [ ] Add GitHub Actions for automated testing

---

## 🤝 Contributing

Contributions are welcome for educational improvements.

Create a new branch:

```bash
git checkout -b improve-image-encryption
```

Make your changes and test them locally.

Then:

```bash
git add .
git commit -m "Improve image encryption handling"
git push origin improve-image-encryption
```

Open a Pull Request on GitHub.

---

## 🛡️ Safe Development Practices

* Never commit private or sensitive images
* Do not commit passwords or API keys
* Use sample images for testing
* Review files before pushing them
* Do not claim this implementation provides secure encryption
* Use modern cryptographic libraries for real security applications

---

## 📄 License

This project is intended as an educational cybersecurity project.

If a `LICENSE` file is added to the repository, refer to that file for the applicable licensing terms.

---

## 👨‍💻 Author

**Jeevicyber28**

GitHub Repository:

https://github.com/jeevicyber28/PRODIGY_CS_02

---

## 🙏 Acknowledgements

This project was created as part of a **Cyber Security learning/internship task** and focuses on understanding image processing, pixel manipulation, and basic encryption concepts.

---

## ⭐ Final Note

This project demonstrates how images can be represented as collections of pixels and how mathematical transformations can be applied to those pixels.

It is a beginner-friendly project for learning:

* Python
* Pillow
* Image processing
* Pixel manipulation
* Functions
* Loops
* Conditional statements
* Modular arithmetic
* Basic encryption concepts
* Git and GitHub

If you find this project useful, consider giving the repository a ⭐.
