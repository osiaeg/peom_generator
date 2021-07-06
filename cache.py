import os
import string
import csv
from pymystem3 import Mystem
import json

_, _, filenames = next(os.walk('poems'))

all_words = ''
for poem in filenames:
    with open(f"poems/{poem}", 'r') as f:
        all_words += f.read()

lines = all_words.split('\n')

punctuation = string.punctuation
punctuation += '—'
punctuation += '\xa0'
punctuation += '«'
punctuation += '»'

words = []

parts_of_speech = {
        'S': 'сущ.',
        'A': 'прил.',
        'NUM': 'числ.',
        'A-NUM': 'числ.-прил.',
        'V': 'глаг.',
        'ADV': 'нареч.',
        'PRAEDIC': 'предикатив',
        'PARENTH': 'вводное',
        'S-PRO': 'местоим. сущ.',
        'A-PRO': 'местоим. прил.',
        'ADV-PRO': 'местоим. нареч.',
        'PRAEDIC-PRO': 'местоим. предик.',
        'PR': 'предлог',
        'CONJ': 'союз',
        'PART': 'частица',
        'INTJ': 'межд.'
        }

# Убираем всю пунктуации из строк
for line in lines:
    line = "".join(c for c in line if c not in punctuation)
    word_arr = line.split(' ')
    words.extend(word_arr)

cache = {}
def get_word(word):
    if not cache.get(word):
        data = None
        cache[word] = data
        return data

for word in words:
    get_word(word)



