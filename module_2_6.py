print()
def keys(number):
    key_ = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                key_ += str(i) + str(j)
    return key_
print('Привет Индиана Джонс, введи любое число от 3 до 20: ')
print("Нужный тебе пароль:", keys(int(input())))