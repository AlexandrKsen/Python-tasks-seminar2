# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def raschet(n):
    if n == 1:
        return 1
    else:
        return n * raschet(n - 1)

# функция преобразования числа в список


def razborchisel(A, D):
    A = int(A)
    for peremen in range(1, A+1):
        D.append(raschet(peremen))
    return D

# функция проверки


def proverka(A, otvet):
    # из строки в число
    otvet1 = ''
    S = len(A)
    A = int(A)
    if S == 1:
        # список с только числами для проверки
        B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for perem in B:
            if perem == A:
                otvet = 'true'
                break
            elif perem != A:
                otvet = 'false'

    elif S > 1:
        for perem1 in str(A):
            # список с только числами для проверки
            B = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for perem in B:
                if perem == int(perem1):
                    otvet = 'true'
                    break
                elif perem != int(perem1):
                    otvet = 'false'
    return otvet


A = input("Введите число: ")

otvet = ''
E = proverka(A, otvet)

if E == 'true':
    D = []
    G = razborchisel(A, D)
    print(D)
elif E == 'false':
    print('Нужно вводить только числа!!!')
