import datetime
def current_date():
    now = datetime.datetime.today()
    return now.strftime("%Y/%m/%d")

def current_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")


