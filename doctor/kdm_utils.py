import datetime

WHS = datetime.time(9,0)
WHEND = datetime.time(17,0)
TIME = datetime.timedelta(hours=1)


def CheckDatetime(curr_date, date_time, invalid_dates):
    """ (datetime, datetime, list of datetimes) -> bool
    Return True iff date_time passes all checks.
    1. checks if date_time less then curr_date
    2. checks if date_time.weekday() is Saturday or Sunday(5,6)
    3. checks if date_time.time() outside of clinic work time
    4. checks if date_time in invalid_dates and if it is more or equal and less then invalid_date + TIME(1 hour)
    """
    # (1) checking if client chosen date and time is less then current date and time
    if date_time < curr_date:
        return False
    # (2) checking if client chosen day is Saturday or Sunday
    if date_time.weekday() > 4:
        return False
    # (3) checking if client chosen time is outside of clinic work time
    #or he have not enough time for doctor appointment left(1 hour)
    if not WHS <= date_time.time() <= WHEND:
        return False
    # (4) checking if client date and time in someone else's appointment
    for invalid_date in invalid_dates:
        if invalid_date <= date_time < invalid_date + TIME:
            return False
    
    return True