import unittest
from password_checker import check_password_strength


class TestPasswordChecker(unittest.TestCase):
    def test_strong_password_passes_all_checks(self):
        rating, feedback = check_password_strength("Str0ng!Pass#26")
        self.assertEqual(rating, "Strong password!")
        self.assertEqual(feedback, [])

    def test_moderate_password_returns_missing_criteria(self):
        rating, feedback = check_password_strength("Abcdef12")
        self.assertEqual(rating, "Moderate password.")
        self.assertTrue(any("special character" in item for item in feedback))

    def test_weak_short_password(self):
        rating, feedback = check_password_strength("abc")
        self.assertEqual(rating, "Weak password.")
        self.assertGreaterEqual(len(feedback), 3)


if __name__ == "__main__":
    unittest.main()
