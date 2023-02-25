# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# *Пример:*
# ноутбук
# 12

us_1 = dict.fromkeys(["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"], 1)
us_2 = dict.fromkeys(["D", "G"], 2)
us_3 = dict.fromkeys(["B", "C", "M", "P"], 3)
us_4 = dict.fromkeys(["F", "H", "V", "W", "Y"], 4)
us_5 = dict.fromkeys(["K"], 5)
us_6 = dict.fromkeys(["J", "X"], 8)
us_7 = dict.fromkeys(["Q", "Z"], 10)
ru_1 = dict.fromkeys(["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"], 1)
ru_2 = dict.fromkeys(["Д", "К", "Л", "М", "П", "У"], 2)
ru_3 = dict.fromkeys(["Б", "Г", "Ё", "Ь", "Я"], 3)
ru_4 = dict.fromkeys(["Й", "Ы"], 4)
ru_5 = dict.fromkeys(["Ж", "З", "Х", "Ц", "Ч"], 5)
ru_6 = dict.fromkeys(["Ш", "Э", "Ю"], 8)
ru_7 = dict.fromkeys(["Ф", "Щ", "Ъ"], 10)

usa_dict = (us_1 | us_2 | us_3 | us_4 | us_5 | us_6)
russia_dict = (ru_1 | ru_2 | ru_3 | ru_4 | ru_5 | ru_6 | ru_7)
word = input("Введите слово: ").upper()
count = 0
for key, value in usa_dict.items():  
    for i in word:
        if i == key:
            count += value
for ru_key, ru_value in russia_dict.items():
    for j in word:
        if j == ru_key:
            count += ru_value
print(count)