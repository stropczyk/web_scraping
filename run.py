from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from statistics import median

app = Flask(__name__)


def change_string_to_int(string):
    x = [i for i in string.split(' ')]
    y = [i.replace(',', '.') for i in x]
    z = []
    for i in y:
        if not i.isalpha():
            z.append(i)
    output = float(''.join(z))
    return output


@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        products = []
    if request.method == 'POST':
        looking_for = request.form['product']
        looking_for_split = looking_for.split(' ')

        # source_1_phrase = '+'.join(looking_for_split)
        # source_1 = requests.get(f'https://www.morele.net/wyszukiwarka/0/0/,,,,,,,,,,,,/1/?q={source_1_phrase}').text
        # soup_1 = BeautifulSoup(source_1, 'lxml')
        #
        # source_3_phrase = '%20'.join(looking_for_split)
        # source_3 = requests.get(f'https://www.komputronik.pl/search/category/1?query={source_3_phrase}').text
        # soup_3 = BeautifulSoup(source_3, 'lxml')

        source_2_phrase = '%20'.join(looking_for_split)
        source_2 = requests.get(f'https://www.x-kom.pl/szukaj?q={source_2_phrase}').text
        soup_2 = BeautifulSoup(source_2, 'lxml')

        products = []
        for div in soup_2.find_all('div', class_='sc-162ysh3-1 bsrTGN sc-bdVaJa cRgopZ'):
            item_image = div.find('img', class_='sc-1tblmgq-1 bxjRuC')['src']

            item_name = div.find('div', class_='sc-3g60u5-0 cDisn').a.h3.text

            item_price_source = div.find('div', class_='sc-6n68ef-1 eOCAwm')
            item_price = item_price_source.find(class_='sc-6n68ef-3').text

            products.append({'item image': item_image,
                             'item name': item_name,
                             'item price': change_string_to_int(item_price)})

        data_prices = []
        for item in products:
            data_prices.append(item['item price'])
        min_price = min(data_prices)
        max_price = max(data_prices)
        medium_price = median(data_prices)

    return render_template('home.html', title='Home', products=products)


if __name__ == '__main__':
    app.run(debug=True)
