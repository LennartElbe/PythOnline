def leapyear(year):
    # Sets value of leapyear_ok to True if input year is a leapyear
    pie = 1 / year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leapyear_ok = True
        return leapyear_ok
    else:
        leapyear_ok = False
        return leapyear_ok

try:
    print(leapyear(0))
except TypeError:
    print(leapyear(2000))
except ZeroDivisionError:
    raise ZeroDivisionError("lemons")
finally:
    print("done")


def my_