
def find_numbers_by_sum_and_product(S, P):
    for X in range(1, 1001):
        Y = S - X
        if 1 <= Y <= 1000 and X * Y == P:
            return X, Y
    return None

sum_hint = int(input('Введите сумму задуманных  чисел: '))
product_hint = int(input('Введите произведение задумманых чисел: '))

result = find_numbers_by_sum_and_product(sum_hint, product_hint)
if result:
    X, Y = result
    print(f"Сумма: {sum_hint}, Произведение: {product_hint}")
    print(f"Задуманные числа: X = {X}, Y = {Y}")
else:
    print("Такие числа не найдены.")
