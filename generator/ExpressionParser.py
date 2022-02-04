from asyncio.log import logger
from distutils.log import error
from generator.Constant import Constant
import logging
from generator.Util import Util

logger = logging.getLogger(__name__)
class ExpressionParser:

    def __init__(self,args):
        self.args = args
    
    #functionality to split the cron expression into respective fields
    def _split_expression(self):
        self.expression= self.args.split()
        self.minutes = self.expression[0]
        self.hours = self.expression[1]
        self.day_of_month = self.expression[2]
        self.months = self.expression[3]
        self.day_of_week = self.expression[4]
        self.command = self.expression[5]
    
    def _parse_expression(self):
        Util(self._parse_minutes())._print_list(Constant.Field_minutes)
        Util(self._parse_hours())._print_list(Constant.Field_hours)
        Util(self._parse_days_of_month())._print_list(Constant.Field_days_of_month)
        Util(self._parse_month())._print_list(Constant.Field_month)
        Util(self._parse_day_of_week())._print_list(Constant.Field_day_of_week)
        Util(self._parse_command())._print_list(Constant.Field_command)

    #functionality to parse minute part of the cron expression
    def _parse_minutes(self,minutes = None):
        if minutes is None:
            minutes = self.minutes
        start=Constant.Start_minutes
        end=Constant.End_minutes
        return self._get_possible_values(minutes,start,end)
    
    #functionality to parse hours part of the cron expression
    def _parse_hours(self,hours = None):
        if hours is None:
            hours = self.hours
        start=Constant.Start_hours
        end=Constant.End_hours
        return self._get_possible_values(hours,start,end)

    #functionality to parse days of months part of the cron expression
    def _parse_days_of_month(self,day_of_month = None):
        if day_of_month is None:
            day_of_month = self.day_of_month
        start=Constant.Start_days_of_month
        end=Constant.End_days_of_month
        return self._get_possible_values(day_of_month,start,end)
    
    #functionality to parse months part of the cron expression
    def _parse_month(self, months = None):
        if months is None:
            months = self.months
        start=Constant.Start_month
        end=Constant.End_month
        return self._get_possible_values(months,start,end)
    
    #functionality to parse days of week part of the cron expression
    def _parse_day_of_week(self, day_of_week = None):
        if day_of_week is None:
            day_of_week = self.day_of_week
        start=Constant.Start_day_of_week
        end=Constant.End_day_of_week
        return self._get_possible_values(day_of_week,start,end)
    
    #functionality to parse command part of the cron expression
    def _parse_command(self, command = None):
        if command is None:
            command = self.command
        return [command]

    #Utility to parse the respective cron expressions based on the literals present in the expression
    def _get_possible_values(self,time_entity,start,end):

        # If the subset of expression (current time entity) is only *
        if time_entity == Constant.Astric:
            try:
                values = [ int(value) for value in range(start, end+1) ]
                return values
            except ValueError as valueError:
                logger.error("Exception while parsing values for * : ",valueError)

        # If the expression contains the stepping function "/"
        elif str(time_entity).find(Constant.Slash) > 0:
            try:
                start_val,multiple=time_entity.split(Constant.Slash)
                if start_val == Constant.Astric: 
                    start_val = start
                values = [ int(value) for value in range(int(start_val), end, int(multiple)) ]
                return values
            except ValueError as valueError:
                logger.error("Exception while parsing values for / : ",valueError)

        # If the expression contains hyphen "-" (range)
        elif str(time_entity).find(Constant.Hyphen) > 0:
            try:
                start_val,end_val=time_entity.split(Constant.Hyphen)
                values = [ int(value) for value in range(int(start_val), int(end_val)+1) ]
                return values
            except ValueError as valueError:
                logger.error("Exception while parsing values for - : ",valueError)
        
        # If the expression contains is list seperated by comma ","
        elif str(time_entity).find(Constant.Comma) > 0:
            try:
                values = list(map(int,time_entity.split(Constant.Comma)))
                return values
            except ValueError as valueError:
                logger.error("Exception while parsing values for , : ",valueError)   
        # If it is a single number
        else:
            values = [int(time_entity)]
            return values