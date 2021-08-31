import csv
from typing import List
from time import sleep
#from accent import *
from syntax import get_word_info
import json


def count_syllables(word : str) -> int:
    vowel = 'ауоыиэяюёе'
    only_vowel_letters = "".join(c for c in word.lower() if c in vowel)
    return len(only_vowel_letters)

def get_vowel(word : str) -> str:
    vowel = 'ауоыиэяюёе'
    only_vowel_letters = "".join(c for c in word.lower() if c in vowel)
    return only_vowel_letters


def split_arr(massive : List, step : int) -> List:
    arr = []
    parted_massive = []

    for i, item in enumerate(massive):
        if i % step == 0:
            parted_massive.append(arr)
            arr = []
        arr.append(item)

    parted_massive.append(arr)
    return parted_massive


def test(word: str, file_writer) -> None:
        row = {
                'Слово': word,
                'Гласные': get_vowel(word),
                'Кол-во слогов': count_syllables(word),
                'Часть речи': 1,
                'Начальная форма': 1,
                'Слогов до': 1,
                'Ударный слог': 1,
                'Слогов после': 1,
               }

        row.update(get_word_info(word))
        file_writer.writerow(row)
        print(json.dumps(row, ensure_ascii=False, indent=4))


def work(word: str, file_writer) -> None:
    for item in parse_syllable(word):
        (syllable_before,
         accent_syllable,
         syllable_after) = item

        row = {
                'Слово': word,
                'Гласные': get_vowel(word),
                'Кол-во слогов': count_syllables(word),
                'Часть речи': 1,
                'Начальная форма': 1,
                'Слогов до': syllable_before,
                'Ударный слог': accent_syllable,
                'Слогов после': syllable_after,
               }

        row.update(get_word_info(word))
        file_writer.writerow(row)
        print(json.dumps(row, ensure_ascii=False, indent=4))


def main():
    is_test = True

    with open('words_from_pandas.csv', 'r') as f:
        words = [word.strip() for word in f.readlines()]


    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = [
                'Слово',
                'Гласные',
                'Кол-во слогов',
                'Часть речи',
                'Начальная форма',
                'Слогов до',
                'Ударный слог',
                'Слогов после',
                'Наклонение',
                'Залог',
                'Включенность говорящего в действие',
                'Род',
                'Время',
                'Вид',
                'Число',
                'Переходность',
                'Лицо',
                'Падеж',
                'Одушевленность'
                ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        parted_word_list = split_arr(words, 5)

        for part in parted_word_list:
            for word in part:
                if is_test:
                    test(word, writer)
                else:
                    work(word, writer)

            print('------------------------')
            sleep(5)


if __name__ == '__main__':
    main()
