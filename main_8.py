from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays_to_greet = set()

    for user in users:
        birthday = user['birthday'].date()
        if today <= birthday <= next_week:
            weekday = weekdays[birthday.weekday()]
            weekdays_to_greet.add(weekday)

    for weekday in sorted(weekdays_to_greet):
        print(f"{weekday}: ", end="")
        names = [user['name'] for user in users if weekdays[user['birthday'].date().weekday()] == weekday]
        print(", ".join(names))

# Приклад виклику функції з тестовим списком користувачів
users = [
    {'name': 'Bill', 'birthday': datetime(2023, 8, 4)},
    {'name': 'Jill', 'birthday': datetime(2023, 8, 6)},
    {'name': 'Kim', 'birthday': datetime(2023, 8, 7)},
    {'name': 'Jan', 'birthday': datetime(2023, 8, 8)},
]

get_birthdays_per_week(users)