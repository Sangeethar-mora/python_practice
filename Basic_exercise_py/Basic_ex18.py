# Check if a given year is a leap year
# A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.
#
# Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
#
# Write a code find if a given year is a leap year.
year1 = int(input("enter the year"))
if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
    print(True)
else:
    print(False)
############ using functions ##########

def leap_year(year1):
    if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
        return True
    else:
        return False
leap_year(2025)
