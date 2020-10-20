from bs4 import BeautifulSoup
from googletrans import Translator


with open('./english-HTML.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

translator = Translator()

for text in soup.find_all(['p', 'h1', 'h2']):
    untranslated_text = text.get_text("|", strip=True)

    if(untranslated_text == ''):
        continue

    translated_text = translator.translate(untranslated_text, src="en", dest='sv')
    text.string = translated_text.text

with open('./swedish-HTML.html', 'w') as file:
    file.write(str(soup.prettify()))