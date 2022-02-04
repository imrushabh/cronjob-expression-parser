import logging

logger = logging.getLogger(__name__)
# Util class: functionality for general use
class Util:
    def __init__(self,timelist):
        self.timelist = timelist
    
    # functionality to present the data after log parsing
    def _print_list(self, field_name):
        try:
            print(field_name,end=" "),
            for value in self.timelist:
                print(value,end=" "),
            print()
        except TypeError as typeerror:
            logger.error("Exception while print the values: ",typeerror)