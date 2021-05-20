from datetime import date


def get_today_name():
    return date.today().strftime('%A')

def get_message():
    return f'Hello {get_today_name()}!'
