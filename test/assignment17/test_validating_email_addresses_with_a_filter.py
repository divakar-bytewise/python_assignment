import unittest
from python_assignment.src.assignment17.util import filter_mail

class TestEmailFilter(unittest.TestCase):
    def test_valid_emails(self):
        emails = ["user@domain.com", "valid_123@site.in", "test-user@abc.org"]
        result = filter_mail(emails)
        self.assertEqual(result, emails)

    def test_invalid_emails(self):
        emails = ["User@domain.com", "invalid@domain.comm", "noatsymbol.com", "bad@site."]
        result = filter_mail(emails)
        self.assertEqual(result, [])

    def test_mixed_emails(self):
        emails = ["good@abc.com", "BadEmail@x", "okay@x.org"]
        result = filter_mail(emails)
        self.assertEqual(result, ["good@abc.com", "okay@x.org"])

if __name__ == '__main__':
    unittest.main()
