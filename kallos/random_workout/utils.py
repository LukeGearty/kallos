from datetime import date
import calendar


#formating the date
def format_date():
    today = date.today()
    day = calendar.day_name[today.weekday()]
    month = today.strftime("%B")
    day_of_month = date.today().day
    return f"{day}, {month} {day_of_month}"
