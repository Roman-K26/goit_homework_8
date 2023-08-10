from datetime import datetime, timedelta 
 
def get_birthdays_per_week(users): 
    # Отримуємо поточну дату 
    today = datetime.now().date() 
 
    # Отримуємо день тижня для поточної дати 
    today_weekday = today.weekday() 
     
    # Встановлюємо початок і кінець поточного тижня 
    start_of_week = today 
    end_of_week = start_of_week + timedelta(days=6) 
 
    # Створюємо словник birthdays_per_week, де кожному дню тижня відповідає пустий список,  
    # в який будемо додавати імена користувачів з їхніми днями народження 
    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
    birthdays_per_week = {weekday: [] for weekday in weekday_names} 
 
    # Ітеруємось, та отримуємо ім'я користувача та його день народження 
    for user in users: 
        name = user['name'] 
        birthday = user['birthday'].date() 
 
        # Замінюємо рік на поточний, щоб функція працювала вірно 
        this_year_birthday = birthday.replace(year=today.year) 
 
 
        # Отримуємо назву дня тижня для дня народження у форматі 'Monday', 'Tuesday', і т.д. 
        weekday = this_year_birthday.strftime("%A") 
 
        # Якщо день народження припадає на суботу або неділю, змінюємо назву дня на понеділок 
        if weekday in ['Saturday', 'Sunday']: 
            weekday = 'Monday' 
 
        # Перевіряємо, чи день народження потрапляє у поточний тиждень,  
        # і якщо так, додаємо ім'я користувача до відповідного дня тижня в словнику 
        if start_of_week <= this_year_birthday <= end_of_week: 
            birthdays_per_week[weekday].append(name) 
             
    # виводимо результати - ім'я користувача та його день народження за тиждень, якщо вони є, для кожного дня тижня 
    for weekday, names in birthdays_per_week.items(): 
        if names: 
            print(f"{weekday}: {', '.join(names)}") 
 

# Приклад виклику функції з тестовим списком користувачів
users = [
    {'name': 'Bill', 'birthday': datetime(2023, 8, 10)},
    {'name': 'Jill', 'birthday': datetime(2023, 8, 11)},
    {'name': 'Kim', 'birthday': datetime(2023, 8, 12)},
    {'name': 'Jan', 'birthday': datetime(2023, 8, 13)},
]

get_birthdays_per_week(users)