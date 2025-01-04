import unittest

def is_palindrome(s):
    cleaned_string = "".join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]


class TestPalindrome(unittest.TestCase):
    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))

    def test_palindrome_ignore_case(self):
        self.assertTrue(is_palindrome("Madam"))

    def test_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(""))
        
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("А роза упала на лапу Бориса"))
        
    def test_palindrome_only_spaces(self):
        self.assertTrue(is_palindrome("   "))
        
    def test_palindrome_numbers(self):
        self.assertTrue(is_palindrome("12321"))
        
    def test_not_palindrome_numbers(self):
        self.assertFalse(is_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()