def romanToInt(s):
    cnt = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(s)):
        if i + 1 != len(s) and d[s[i]] < d[s[i+1]]:  # если цифра меньше следующей
            cnt -= d[s[i]]
        else:
            cnt += d[s[i]]
    return cnt


def intToRoman(num_int):
    num_rom = ''
    d = {'1': 'I', '4': 'IV', '5': 'V', '9': 'IX', '10': 'X', '40': 'XL',
         '50': 'L', '90': 'XC', '100': 'C', '400': 'CD', '500': 'D', '900': 'DM', '1000': 'M', '0': ''}
    mnj = 1                         # Через него считал десятки сотки тысячные
    while num_int > 0:
        last = num_int % 10                 # работал всегда с последней цифрой
        cnt = last * mnj                    # присваивал ей десятичную часть
        if str(last) in d:
            num_rom += d[str(cnt)]
        else:
            while str(cnt) not in d:
                cnt -= mnj                  # поиск ближайшей цифры в словаре
                num_rom += d[str(mnj)]
            if str(cnt) in d:
                num_rom += d[str(cnt)]
        num_int = num_int // 10             # переходил к следующей цифре
        mnj *= 10                           # прибавлял десятичную часть
    return num_rom[::-1]


# Просто калькулятор
def calc(a, b, opr):
    if opr == '+':
        return a + b
    elif opr == '-':
        return a - b
    elif opr == '*':
        return a * b
    elif opr == '/' and b > 0:
        return a / b
    else:
        return 'Ошибка'


nums = input("Введите 2 числа через пробел: ").split(' ')
operator = input("Введите оператор: ")
if nums[0].isdigit() and nums[1].isdigit():
    answer = calc(*list(map(int, nums)), operator)
else:
    answer = calc(*list(map(romanToInt, nums)), operator)
    print(answer)
    answer = intToRoman(answer)

print(answer)






