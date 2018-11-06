"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime
from datetime import date
def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month==12:
        return (date(year+1,1,1)-date(year,month,1)).days
    return (date(year,month+1, 1) - date(year, month, 1)).days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        return False
    return True

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    try:
        datetime.datetime(int(year1),int(month1),int(day1))
        datetime.datetime(int(year2),int(month2),int(day2))
    except ValueError:
        return 0
    if year1>year2:
        return 0
    elif month1>month2 and year1==year2:
        return 0
    elif day1>day2 and month1==month2 and year1==year2:
        return 0
    #return the difference between date
    return (date(year2,month2,day2) - date(year1, month1,day1)).days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    try:
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        return 0
    if year>datetime.date.today().year:
        return 0
    elif month>datetime.date.today().month and year==datetime.date.today().year:
        return 0
    elif day>datetime.date.today().day and month==datetime.date.today().month :
        if(year==datetime.date.today().year):
            return 0
    return(datetime.date.today()-datetime.date(year,month,day)).days
