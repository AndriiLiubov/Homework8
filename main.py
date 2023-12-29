from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    if len(users) == 0:
        return {}

    selected_list = []
    congrat_dict = {}

    days_in_a_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    today = date.today()

    day = [today + timedelta(days=i) for i in range(7)]
    week = [i.day for i in day]
    month = [i.month for i in day]

    for man in users:
        if man["birthday"].month in month:
            if man["birthday"].day in week:
                selected_list.append(man)

    for person in selected_list:
        for day_change in day:
            if person['birthday'].day == day_change.day:
                person['birthday'] = day_change

    for person in selected_list:
        if person['birthday'].strftime('%A') in days_in_a_week:
            p_key = person['birthday'].strftime('%A')
            congrat_dict.setdefault(p_key, []).append(person['name'])
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
