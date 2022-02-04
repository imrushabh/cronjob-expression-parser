import TestConstants
from generator.Validator import Validator
import unittest
  
class TestValidator(unittest.TestCase):
    def test_valid_cron_expression(self):
        validator = Validator(TestConstants.Valid_cron_expression)
        self.assertTrue(validator._is_valid())

    def test_invalid_cron_expression(self):
        validator = Validator(TestConstants.Invalid_cron_expression)
        self.assertFalse(validator._is_valid())

if __name__ == '__main__':
    unittest.main()


