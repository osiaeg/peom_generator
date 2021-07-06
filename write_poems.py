import requests
from bs4 import BeautifulSoup as bs

page = requests.get('https://ilibrary.ru/text/3934/index.html')
http = 'https://ilibrary.ru/'
soup = bs(page.content, 'html.parser')
link_poems = soup.find('table').find_all('a')

for index, poem in enumerate(link_poems):
    if poem.text == '»':
        link_poems.pop(index)

all_poems = {}
for item in link_poems:
    http_request = http + item['href'][1:]

    page_with_poem = requests.get(http_request)
    soup = bs(page_with_poem.content, 'html.parser')

    name_of_poem = item.text

    rows = soup.find_all('span', class_='vl')
    poem = ''
    for item in rows:
        poem += item.text + '\n'

    all_poems[name_of_poem] = poem

for k, v in all_poems.items():
    with open(f"poems/{k}", "w") as f:
        f.write(v)
