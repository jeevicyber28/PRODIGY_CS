from PIL import Image

# Encrypt image
def encrypt_image(path, key):
    img = Image.open(path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel = pixels[i, j]
            if len(pixel) == 3:
                r, g, b = pixel
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[i, j] = (r, g, b)
            elif len(pixel) == 4:
                r, g, b, a = pixel
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[i, j] = (r, g, b, a)

    img.save("encrypted.png")
    print("Encrypted image saved as encrypted.png - main.py:25")


# Decrypt image
def decrypt_image(path, key):
    img = Image.open(path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel = pixels[i, j]
            if len(pixel) == 3:
                r, g, b = pixel
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[i, j] = (r, g, b)
            elif len(pixel) == 4:
                r, g, b, a = pixel
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[i, j] = (r, g, b, a)

    img.save("decrypted.png")
    print("Decrypted image saved as decrypted.png - main.py:50")


# Main
print("1. Encrypt - main.py:54")
print("2. Decrypt - main.py:55")

choice = int(input("Enter choice: "))
path = input("Enter image path: ")
key = int(input("Enter key (number): "))

if choice == 1:
    encrypt_image(path, key)
elif choice == 2:
    decrypt_image(path, key)
else:
    print("Invalid choice - main.py:66")