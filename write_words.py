import os, string

def main():
    _, _, filenames = next(os.walk('poems'))

    all_words = ""
    words = []
    punctuation = string.punctuation + '—\xa0«»'

    for poem in filenames:
        with open(f"poems/{poem}", 'r') as f:
            all_words += f.read()

    lines = all_words.split('\n')

    # Убираем всю пунктуации из строк
    for line in lines:
        line = "".join(c for c in line if c not in punctuation)
        word_arr = line.split(' ')
        words.extend(word_arr)

    with open('words.txt', 'w') as f:
        for word in words:
            f.write(f"{word}\n")

if __name__ == '__main__':
    main()
