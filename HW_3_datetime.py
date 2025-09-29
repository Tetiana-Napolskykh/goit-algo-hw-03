from datetime import datetime #Imported the datetime module.

def get_days_from_today(date): 

    try:
        target_data=datetime.strptime(date, "%Y-%m-%d").date() #Converted the date string in 'YYYY-MM-DD' format into a datetime object.
        today=datetime.today().date() #Got the current date using datetime.today().
        delta=today-target_data #Calculated the difference between the current date and the given date.
        return delta.days #Returned the difference in days as an integer.

    except ValueError:
        return ValueError ("Incorrect date format. Expected 'YYYY-MM-DD'")
    
print(get_days_from_today("2025-09-28"))
print(get_days_from_today("1985-05-30"))
