from random import randint

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X

# length = int(input("Введите длину массива: "))
# array_int = [randint(0, length - 1) for item in range(length)]
# print(array_int)
# number = int(input("Введите искомое число: "))
# print(f"число встречается {array_int.count(number)} раз")


# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X

# length = int(input("Введите длину массива: "))
# array_int = [randint(0, length - 1) for item in range(length)]
# print(array_int)
# number = int(input("Введите искомое число: "))
# min_diff = abs(number) + length
# min_diff_dict = {}
# i = 0
# for item in array_int:
#     diff = abs(number - item)
#     if diff < min_diff:
#         min_diff_dict.clear()
#         min_diff = diff
#     if diff <= min_diff:
#         min_diff_dict.update({i: item})
#     i += 1
# print("Ближайшие значения: ", end=' ')
# for key in min_diff_dict:
#     print(f"A[{key}] = {min_diff_dict[key]}", end=", ")


# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

alphabet_Eng = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
alphabet_Ru = {'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3}

def SelectLang():
    language = input("Выберите язык (E/R): ").upper()
    if language == 'E':
        alphabet = alphabet_Eng
        print("Английский язык")
    elif language == 'R':
        alphabet = alphabet_Ru
        print("Русский язык")
    else:
        alphabet = SelectLang()
    return alphabet

alphabet = SelectLang()

points = 0
word = input("Введите слово: ")
try:
    for letter in word:
        points += alphabet[letter.upper()]
    print(f"В слове {points} очков")    
except Exception:
    print(f"В слове недопустимые символы")