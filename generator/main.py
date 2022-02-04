import argparse
import logging
from Validator import Validator
import sys
from ExpressionParser import ExpressionParser

logger = logging.getLogger(__name__)

def main(cmdline_args):

    parser = argparse.ArgumentParser(description=__doc__)
    # Adding args to argparse that can be used as a help option on commandline usning --help or -h
    parser.add_argument(
        'expression',
        help="- Cron expression along with the command",
        default="*/15 0 1,15 * 1-5 /usr/bin/find",
    )

    args = parser.parse_args()
    # Spliting & parsing the cron expression using ExpressionParser
    try:
        validate = Validator(args.expression)
        if validate._is_valid():
            expressionParser = ExpressionParser(args.expression)
            expressionParser._split_expression()
            expressionParser._parse_expression()
        else:
            logger.error("Invalid Cron expression")
    except Exception as exception:
        logger.error("Exception occured while parsing the cron expression ",exception)

if __name__ == "__main__":
    main(sys.argv)