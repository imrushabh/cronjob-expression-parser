import re
from generator.Constant import Constant
import logging

logger = logging.getLogger(__name__)

class Validator:
    def __init__(self,args):
        self.expression = args

    # validator function that return true on successful matching of cron expression with regex
    # Currently the validator checks regex with limit functionality of digit range. 
    # This can be updated with digit range check regex for each part of cron expression.
    def _is_valid(self,expression = None):
        if expression is None:
            expression = self.expression
        expression = expression[:expression.rfind(' ')]
        pattern = Constant.ExpressionRegex
        result = re.compile(r"{}".format(pattern))
        if result.fullmatch(expression):
            logger.info("Valid cronjob expression",expression)
            return True
        else:
            logger.info("Invalid cronjob expression",expression)
            return False