import unittest
from caesar_cipher import caesar_encrypt, caesar_decrypt


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_preserves_case_and_punctuation(self):
        self.assertEqual(caesar_encrypt("Hello, World!", 3), "Khoor, Zruog!")

    def test_wrap_around_alphabet(self):
        self.assertEqual(caesar_encrypt("xyz XYZ", 3), "abc ABC")

    def test_decrypt_roundtrip_with_large_shift(self):
        message = "Cyber Security 2026!"
        encrypted = caesar_encrypt(message, 29)
        self.assertEqual(caesar_decrypt(encrypted, 29), message)


if __name__ == "__main__":
    unittest.main()
