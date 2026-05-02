def is_year_leap(numbers):
    return numbers % 4 == 0
num = int (input ("Введите число: "))
result = is_year_leap (num)
print(f"Год високосный: {num}? - {result}")