from datetime import date, datetime
import calendar


def get_birthdays_per_week(users):
    weekday_names_list = [day for day in calendar.day_name]
    birthdays = {weekday_names: [] for weekday_names in weekday_names_list}
    current_day = date.today()
    filtered_birthdays = dict()
    number_of_days = 365 if date.today().year % 4 else 366

    for user in users:
        current_year_birthday = datetime(current_day.year, user["birthday"].month, user["birthday"].day).date()
        delta_days = int(str((current_year_birthday - current_day).days))
        to_next_year_days = 0
        if delta_days < 0:
            to_next_year_days = number_of_days + delta_days
            current_year_birthday = datetime(current_day.year + 1, user["birthday"].month, user["birthday"].day).date()
        if ((delta_days >= 0) and (delta_days <= 6)) or ((to_next_year_days >= 0) and (to_next_year_days <= 6)):
            weekday_num = current_year_birthday.weekday()
            if weekday_num < 5:
                weekday_name = current_year_birthday.strftime('%A')
            else:
                weekday_name = "Monday"

            name = user["name"]
            birthdays[weekday_name].append(name)

    for day, name in birthdays.items():
        if name:
            filtered_birthdays[day] = name

    return filtered_birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
