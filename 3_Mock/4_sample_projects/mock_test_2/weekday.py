from datetime import datetime

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6    
    return (0 <= today.weekday() < 5)

# Test if today is a weekday
#assert not is_weekday()


if __name__=='__main__':
    is_weekday()