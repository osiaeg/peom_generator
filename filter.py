import pandas as pd

def count_syllabels(word):
    vowel = 'ауоыиэяюёе'
    only_vowel_letters = "".join(c for c in word.lower() if c in vowel)
    return len(only_vowel_letters)


def main():
    words = pd.read_csv('words.csv')

    words.drop_duplicates(inplace=True)
    words = words.assign(low=lambda x: x.word.str.lower())
    words.drop_duplicates(subset='low', inplace=True)
    del words['low']

#    num_syll = [count_syllabels(row[1]) for row in words.itertuples()]
#    words = words.assign(num_syll=num_syll)

    words.to_csv('words_from_pandas.csv', index=False)

if __name__ == '__main__':
    main()
