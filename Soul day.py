from datetime import datetime


def soul_day():
    date_str = input('Enter your birthday in DD/MM/YYYY\n')
    # Convert date string to python date
    try:
        birthday = datetime.strptime(date_str, "%d/%m/%Y")
    except TypeError:
        birthday = datetime.datetime(*(time.strptime(date_str, "%d/%m/%Y")[0:6]))

    # A control date(The first day of the AD)
    ctrl = str('01/01/0001')
    try:
        ctrl_day = datetime.strptime(ctrl, "%d/%m/%Y")
    except TypeError:
        ctrl_day = datetime.datetime(*(time.strptime(ctrl, "%d/%m/%Y")[0:6]))

    birth_date = datetime(birthday.year, birthday.month, birthday.day)
    ctrl_date = datetime(ctrl_day.year, ctrl_day.month, ctrl_day.day)

    # Finds the number of days that elapsed before the user's birth
    number_of_days = (birth_date - ctrl_date).days
    # Accounts for the one day from the ctrl date
    actual_number_of_days = number_of_days + 1

    # Soul day block
    if actual_number_of_days % 7 == 0:
        print('You were born on Sunday')
    elif actual_number_of_days % 7 == 1:
        print('You were born on Monday')
    elif actual_number_of_days % 7 == 2:
        print('You were born on Tuesday')
    elif actual_number_of_days % 7 == 3:
        print('You were born on Wednesday')
    elif actual_number_of_days % 7 == 4:
        print('You were born on Thursday')
    elif actual_number_of_days % 7 == 5:
        print('You were born on Friday')
    elif actual_number_of_days % 7 == 6:
        print('You were born on Saturday')

while True:
    print(soul_day())
