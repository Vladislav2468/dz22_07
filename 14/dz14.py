def powers_of_two(N):
    power = 1
    while power <= N:
        print(power)
        power *= 2

N = int(input('Введите число '))
print("Целые степени двойки не превосходящие", N)
powers_of_two(N)
