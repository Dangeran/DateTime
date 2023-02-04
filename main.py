from datetime import datetime

week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
month_names = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля",
               "августа", "сентября", "октября", "ноября", "декабря"]


def print_current_date():
    now_date = datetime.today()
    print("Добро пожаловать!")
    print(f'Сегодня {now_date.day} {month_names[now_date.month]} {now_date.year} года,'
          f' день недели - {week_days[now_date.weekday()]}')


if __name__ == '__main__':
    print_current_date()
