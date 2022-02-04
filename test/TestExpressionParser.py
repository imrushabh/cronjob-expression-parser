import TestConstants
from generator.ExpressionParser import ExpressionParser
import unittest
  
class TestExpressionParser(unittest.TestCase):
    # Test to verify the minute functionality & */multiple expression check.
    def test_valid_minute_parsing(self):
        expressionParser = ExpressionParser(TestConstants.Valid_cron_expression)
        self.assertListEqual(expressionParser._parse_minutes(TestConstants.Minutes),[0,20,40])

    # Test to verify the invalid minute functionality & */multiple expression check.
    def test_invalid_minute_parsing(self):
        expressionParser = ExpressionParser(TestConstants.Valid_cron_expression)
        self.assertNotEqual(expressionParser._parse_minutes(TestConstants.Minutes),[1,20,40])
    
    # Test to verify the hour functionality & [a-b] (hyphen) expression check.
    def test_valid_hour_parsing(self):
        expressionParser = ExpressionParser(TestConstants.Valid_cron_expression)
        self.assertListEqual(expressionParser._parse_hours(TestConstants.Hours),[2,3,4])

    # Test to verify the month_parsing functionality & comma seperated expression check.
    def test_valid_day_in_month_parsing(self):
        expressionParser = ExpressionParser(TestConstants.Valid_cron_expression)
        self.assertListEqual(expressionParser._parse_month(TestConstants.Days_in_month),[6,8,9])

    # Test to verify the week functionality & * expression check.
    def test_valid_day_in_week_parsing(self):
        expressionParser = ExpressionParser(TestConstants.Valid_cron_expression)
        self.assertListEqual(expressionParser._parse_day_of_week(TestConstants.Days_in_week),[1,2,3,4,5,6,7])
    
    # Test to verify the command functionality check.
    def test_valid_command(self):
        expressionParser = ExpressionParser(TestConstants.Valid_cron_expression)
        self.assertListEqual(expressionParser._parse_command(TestConstants.Command),['/usr/bin/find'])

if __name__ == '__main__':
    unittest.main()
