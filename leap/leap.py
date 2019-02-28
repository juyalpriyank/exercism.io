def is_leap_year(year):
    leap_year_bool = False
    if not year%4:
#        leap_year_bool = True
        if not year%100:
            if not year%400:
                leap_year_bool = True
        elif not year%400:
            leap_year_bool = True
#        else:
#            leap_year_bool = False
    return leap_year_bool


