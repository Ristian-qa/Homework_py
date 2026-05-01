def is_year_leap (numbers):
    return 'True' if numbers %4 ==0 else 'False'
num = int (input ("Введите число: "))
result = is_year_leap (num)
print(f"Год високосный: {num}? - {result}")