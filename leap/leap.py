def is_leap_year(year):
    leap_year_bool = False
    if year%4==0:
        leap_year_bool = True
    if year%100==0:
        if year%400==0:
            leap_year_bool = True
        else:
            leap_year_bool = False
    return leap_year_bool

def is_leap_year_opt(year):
    leap_year_bool = False
    if year%4==0:
        pass
