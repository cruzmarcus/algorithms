import unittest

from ..valid_anagram import are_anagrams


class TestAreAnagrams(unittest.TestCase):
    def test_are_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))  # Anagrams
        self.assertTrue(are_anagrams("", ""))  # Empty strings (Anagrams)
        self.assertTrue(are_anagrams("a", "a"))  # Single character (Anagrams)

        self.assertFalse(are_anagrams("hello", "world"))  # Different strings
        self.assertFalse(are_anagrams("listen", "silen"))  # Different lengths
        self.assertFalse(are_anagrams("hello", "chell"))  # Same length, not anagrams


if __name__ == "__main__":
    unittest.main()
