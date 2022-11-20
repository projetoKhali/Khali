from datetime import date

_fake_today:date = None

def set_today(dd:int, mm:int, aaaa:int = 2022):
    _set_today(date(aaaa, mm, dd))
    
def _set_today(new_fake_today:date):
    global _fake_today
    _fake_today = new_fake_today


def today():
    return _fake_today if _fake_today is not None else date.today()