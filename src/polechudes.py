"""
Pole Chudes on python

Copyright (C) 2025 Arseniy Dukup

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

#Игра "Поле Чудес" на Python (Это только начальная версия и в ней мало что готово)

#импорт библиотек
import random



#слова 
words = ['москва', 'торвальдс', 'кубань']

#разделение слова из списка на отдельные символы, слова выбираются рандомно
word_tostrip = random.choice(words)
currentword = list(word_tostrip)

currenttask = ['*'] * len(currentword) #разгаданые буквы лежат здесь
usedletters = [] #все названные буквы
score = 0 #очки игрока


#основная логика разгадывания
while True:
    print(usedletters)
    print(f"Разгаданые буквы: {''.join(currenttask)} ")
    if word_tostrip == 'москва':
        print("Столица страны")
    elif word_tostrip == 'торвальдс':
        print("Финский програмист. Создатель Linux и Git")
    elif word_tostrip == 'кубань':
        print("Регион России")

    letter = input('называйте букву: ')
    usedletters.append(letter)

    if letter in currentword:
        score += 10 #добавление +10 очков
        # letterindex = currentword.index(letter)
        # #currenttask.insert(letterindex, letter)
        # currenttask[letterindex] = letter
        for i in range(len(currentword)):
            if currentword[i] == letter:
                currenttask[i] = letter
        #print(letterindex) для дебага индекса букв
    elif len(currentword) > len(set(currentword)):
        print("тут две буквы")
    else:
        print("Такой буквы нет")
    if '*' not in currenttask:
        print(f"Игра окончена вы набрали: {score} очков")
        break