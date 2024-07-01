import unittest

from utils.chatbot_utils import levenshtein_distance


class LevenshteinDistanceTestCase(unittest.TestCase):
    def test_levenshtein_distance(self):
        # Test case 1: Same strings
        s1 = "hello"
        s2 = "hello"
        self.assertEqual(levenshtein_distance(s1, s2), 0)

        # Test case 2: One character difference
        s1 = "hello"
        s2 = "hella"
        self.assertEqual(levenshtein_distance(s1, s2), 1)

        # Test case 3: Completely different strings
        s1 = "kitten"
        s2 = "sitting"
        self.assertEqual(levenshtein_distance(s1, s2), 3)

        # Test case 4: Empty strings
        s1 = ""
        s2 = ""
        self.assertEqual(levenshtein_distance(s1, s2), 0)

        # Test case 5: One empty string
        s1 = "hello"
        s2 = ""
        self.assertEqual(levenshtein_distance(s1, s2), 5)


if __name__ == "__main__":
    unittest.main()
