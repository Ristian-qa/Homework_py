import math

def square(side):
    S = side * side
    if not isinstance(side, int):
        S = math.ceil(S)
    return S

print(square(5))  