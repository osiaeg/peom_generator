import csv


def count_syllables(word : str) -> int:
    vowel = 'ауоыиэяюёе'
    only_vowel_letters = "".join(c for c in word.lower() if c in vowel)
    return len(only_vowel_letters)

def get_vowel(word : str) -> str:
    vowel = 'ауоыиэяюёе'
    only_vowel_letters = "".join(c for c in word.lower() if c in vowel)
    return only_vowel_letters


def main():
    with open('words_from_pandas.csv', 'r') as f:
        words = (word.strip() for word in f.readlines())


    with open('names.csv', 'w', newline='') as csvfile:
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
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for word in words:
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

            writer.writerow(row)


if __name__ == '__main__':
    main()
