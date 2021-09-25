from selenium import webdriver
import time

class Browser:

    xpath_textarea = '/html/body/form/table/tbody/tr[4]/td[2]/div/div[1]/p'
    xpath_button = '//*[@id="ctl00_ctl00_BodyPlaceHolder_ContentPlaceHolder1_SubmitButton"]'
    ACCENT = 769
    SOGLACN = 'бвгджзйклмнпрстфхцчшщъь'
    VOWEL = 'ауоыиэяюёе'

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.headless = False
        self.driver = webdriver.Firefox(options=options)
        self.driver.get('https://morpher.ru/accentizer/')

    def search_word(self, word : str) -> str:
        text_area = self.driver.find_element_by_xpath(self.xpath_textarea)
        button = self.driver.find_element_by_xpath(self.xpath_button)

        text_area.clear()
        text_area.send_keys(word)
        button.click()

        text_area = self.driver.find_element_by_xpath(self.xpath_textarea)
        return text_area.text

    def del_soglacn(self, string : str) -> str:
        return ''.join(c for c in string if c not in self.SOGLACN)

    def del_accent(self, string : str) -> str:
        return ''.join(c for c in string if ord(c) != self.ACCENT)

    def get_accent_syllable(self, word : str) -> int:
        word = self.del_soglacn(word.lower())
        accent_index = None

        for index, char in enumerate(word):
            if ord(char) == self.ACCENT:
                accent_index = index - 1
            if char == 'ё':
                accent_index = index

        return accent_index

    def get_word_info(self, word:str) -> list:
        output = []
        word = word.lower()
        accent_words = self.search_word(word).split('|')

        for i in range(len(accent_words)):
            accent_index = self.get_accent_syllable(accent_words[i])
            word = accent_words[i]
            if accent_index != None:
                word = self.del_soglacn(word)
                word = self.del_accent(word)
                syllable_before = accent_index
                accent_syllable = accent_index + 1
                syllable_after = len(word) - accent_index - 1

                output.append((syllable_before,
                        accent_syllable,
                        syllable_after))
            else:
                word = self.del_soglacn(word)
                syllable_before = 0
                accent_syllable = 1
                syllable_after = 0

                output.append((syllable_before,
                        accent_syllable,
                        syllable_after))

        return output


    def close(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    browser = Browser()
    for item in browser.get_word_info("небом"):
        (syllable_before,
         accent_syllable,
         syllable_after) = item

        print(f"Слогов до: {syllable_before}")
        print(f"Ударный слог: {accent_syllable}")
        print(f"Слогов после: {syllable_after}")
    browser.close()
