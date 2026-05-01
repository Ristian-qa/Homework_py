def month_to_season(season):
    if season == 12 or 1 <= season <= 2:
        return "Зима"
    if 3 <= season <= 5:
        return "Весна"
    if 6 <= season <= 8:
        return "Лето"
    if 9 <= season <=11:
        return "Осень"
    if 0 >= season <= 13:
        return "Неверный номер месяца"
season = int(input ("Введите номер месяца (1-12): "))
print (month_to_season(season))