from django.utils import timezone
import datetime

WD = (1,2,3,4,5)
WHS = datetime.time(9,0)
WHEND = datetime.time(17,0)
TIME = datetime.timedelta(hours=1)


def check_datetime(curr_date, date, time, invalid_dates):
	if date < curr_date:
		return False
	if not date.isoweekday() in WD:
		return False
	if not WHS <= time <= WHEND:
		return False
	
	date_time = combine_datetime(date, time)
	for invalid_date in invalid_dates:
		if invalid_date <= date_time < invalid_date + TIME:
			return False
	
	return True
	
def combine_datetime(date, time): 
	return timezone.make_aware(datetime.datetime.combine(date, time))
		
