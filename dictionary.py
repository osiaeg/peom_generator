import os
import string
import csv
from pymystem3 import Mystem
import json
from collections import OrderedDict
from itertools import islice
from accent import *
import time


parts_of_speech = {
        'S': 'сущ.',
        'A': 'прил.',
        'NUM': 'числ.',
        'ANUM': 'числ.-прил.',
        'V': 'глаг.',
        'ADV': 'нареч.',
        'PRAEDIC': 'предикатив',
        'PARENTH': 'вводное',
        'SPRO': 'местоим. сущ.',
        'APRO': 'местоим. прил.',
        'ADVPRO': 'местоим. нареч.',
        'PRAEDICPRO': 'местоим. предик.',
        'PR': 'предлог',
        'CONJ': 'союз',
        'PART': 'частица',
        'INTJ': 'межд.',
        'SPACE': 'пробел.'
        }


# Получаем список уникальных слов
cache = OrderedDict()
def get_word(word):
    if not cache.get(word):
        data = None
        cache[word] = data
        return data

for word in words:
    get_word(word)

words = list(cache.keys())

vowel = 'ауоыиэяюёе'

word_dict = OrderedDict()
for word in words:
    only_vowel_letters = "".join(c for c in word.lower() if c in vowel)
    word_dict[word] = only_vowel_letters

m = Mystem()

def get_inf_form(word):
    try:
        inf_form = m.analyze(word)[0]['analysis'][0]['lex'].split(',')[0]
        return inf_form
    except IndexError:
        return ''


def get_pos_tag(word):
    try:
        a = ord('а')
        russian_letter = [chr(i) for i in range(a,a+32)]
        gr = m.analyze(word)[0]['analysis'][0]['gr'].split(',')[0]

        pos_tag = "".join(c for c in gr if c not in punctuation)
        pos_tag = "".join(c for c in pos_tag if c not in russian_letter)
        return pos_tag
    except IndexError:
        return 'space'.upper()

def get_grammatic(word):
    try:
        grammatic = m.analyze(word)[0]['analysis'][0]['gr']
        pos_tag = get_pos_tag(word)
        print(parts_of_speech[get_pos_tag(k)])
        return grammatic
    except IndexError:
        return ''


    print(word_dict.items())


#with open('dictionary.csv', 'w', newline='') as csvfile:
#    fieldnames = [
#            'Слово',
#            'Гласные',
#            'Кол-во слогов',
#            'Часть речи',
#            'Начальная форма',
#            'Слогов до',
#            'Ударный слог',
#            'Слогов после'
#            ]
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#    writer.writeheader()
fieldnames = [
    'Слово',
    'Гласные',
    'Кол-во слогов',
    'Часть речи',
    'Начальная форма',
    'Слогов до',
    'Ударный слог',
    'Слогов после'
    ]

with open('dictionary.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    d = OrderedDict(islice(word_dict.items(), 720, 780))

    for k, v in d.items():

        count_syllables = parse_syllable(k)

        for item in count_syllables:
            print(k)
            #print(get_grammatic(k))
            (syllable_before,
             accent_syllable,
             syllable_after) = item

            if len(v) == 0:
                (syllable_before,
                 accent_syllable,
                 syllable_after) = (0, 0, 0)

            print(f"Слогов до: {syllable_before}")
            print(f"Ударный слог: {accent_syllable}")
            print(f"Слогов после: {syllable_after}")

            writer.writerow({
                'Слово': k,
                'Гласные': v,
                'Кол-во слогов': len(v),
                'Часть речи': parts_of_speech[get_pos_tag(k)],
                'Начальная форма' : get_inf_form(k),
                'Слогов до' : syllable_before,
                'Ударный слог' : accent_syllable,
                'Слогов после' : syllable_after,
                })
