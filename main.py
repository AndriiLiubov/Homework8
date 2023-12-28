from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if len(users) == 0:
        return {}

    selected_list = []
    congrat_dict = {}

    days_in_a_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    today = date.today()
    second_day = today + timedelta(days=1)
    third_day = today + timedelta(days=2)
    forth_day = today + timedelta(days=3)
    fifth_day = today + timedelta(days=4)
    sixth_day = today + timedelta(days=5)
    seventh_seven = today + timedelta(days=6)

    week = [today.day, second_day.day, third_day.day, forth_day.day, fifth_day.day, sixth_day.day, seventh_seven.day]
    week2 = [today, second_day, third_day, forth_day, fifth_day, sixth_day, seventh_seven]
    month = [today.month, second_day.month, third_day.month, forth_day.month, fifth_day.month, sixth_day.month, seventh_seven.month]


    for man in users:
        if man["birthday"].month in month:
            if man["birthday"].day in week:
                selected_list.append(man)
                
    for person in selected_list:
        for day_change in week2:
            if person['birthday'].day == day_change.day:
                person['birthday'] = day_change

    for person in selected_list:
        if person['birthday'].strftime('%A') in days_in_a_week:
            congrat_dict.setdefault(person['birthday'].strftime('%A'), []).append(person['name'])
        else:
            congrat_dict.setdefault('Monday', []).append(person['name'])

    return congrat_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

