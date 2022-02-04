class Constant:
    def __init__(self):
        pass
    Astric = '*'
    Slash = '/'
    Hyphen = '-'
    Comma = ','
    ExpressionRegex = '((((\*\/\d*)|(\d+,)+\d+|(\d+(\/|-)\d+)|\d+|\*) ?){5,7})'
    Start_minutes = 0
    End_minutes = 59
    Start_hours = 0
    End_hours = 23
    Start_days_of_month = 1
    End_days_of_month = 31
    Start_month = 1
    End_month = 12
    Start_day_of_week = 1
    End_day_of_week = 7
    Field_minutes = 'Minutes:         '
    Field_hours = 'Hours:           '
    Field_days_of_month = 'Days_of_month:   '
    Field_month = 'Month:           '
    Field_day_of_week = 'Day_of_week:     '
    Field_command = 'Command:         '