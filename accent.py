from selenium import webdriver
import time
import logging


options = webdriver.FirefoxOptions()
options.headless = False
browser = webdriver.Firefox(options=options)
browser.get('https://morpher.ru/accentizer/')

xpath_textarea = '/html/body/form/table/tbody/tr[4]/td[2]/div/div[1]/p'
xpath_button = '//*[@id="ctl00_ctl00_BodyPlaceHolder_ContentPlaceHolder1_SubmitButton"]'
ACCENT = 769
SOGLACN = 'бвгджзйклмнпрстфхцчшщъь'

def get_word_from_site(word : str) -> str:
    text_area = browser.find_element_by_xpath(xpath_textarea)
    button = browser.find_element_by_xpath(xpath_button)
    text_area.clear()
    text_area.send_keys(word)
    button.click()
    text_area = browser.find_element_by_xpath(xpath_textarea)
    word = text_area.text
    return word

def del_soglacn(word : str) -> str:
    word = ''.join(c for c in word if c not in SOGLACN)
    return word

def get_accent_syllable(word : str) -> int:
    word = word.lower()
    word = del_soglacn(word)
    accent_index = None
    for index, char in enumerate(word):
        if ord(char) == ACCENT:
            accent_index = index - 1
    return accent_index

def del_accent(word : str) -> str:
    word = ''.join(c for c in word if ord(c) != ACCENT)
    return word

def parse_syllable(word : str) -> list:
    syllables_array = []
    word = word.lower()
    word_with_accent = get_word_from_site(word)
    word_with_accent = word_with_accent.split('|')

    for i in range(len(word_with_accent)):
        accent_index =  get_accent_syllable(word_with_accent[i])
        word = word_with_accent[i]
        if accent_index != None:
            word = del_soglacn(word)
            print(word)
            word = del_accent(word)
            syllable_before = accent_index
            accent_syllable = accent_index + 1
            syllable_after = len(word) - accent_index - 1
            #print(f"Слогов до: {syllable_before}")
            #print(f"Ударный слог: {accent_syllable}")
            #print(f"Слогов после: {syllable_after}")
            syllables_array.append((syllable_before,
                    accent_syllable,
                    syllable_after))
        else:
            word = del_soglacn(word)
            print(word)
            syllable_before = 0
            accent_syllable = 1
            syllable_after = 0
            #print(word)
            #print(f"Слогов до: {0}")
            #print(f"Ударный слог: {1}")
            #print(f"Слогов после: {0}")
            syllables_array.append((syllable_before,
                    accent_syllable,
                    syllable_after))

    return syllables_array


if __name__ == '__main__':
    for item in parse_syllable("небом"):
        (syllable_before,
         accent_syllable,
         syllable_after) = item

        print(f"Слогов до: {syllable_before}")
        print(f"Ударный слог: {accent_syllable}")
        print(f"Слогов после: {syllable_after}")

