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

        # code for first page
        morele_phrase = '+'.join(looking_for_split)
        morele = requests.get(f'https://www.morele.net/wyszukiwarka/0/0/,,,,,,,,,,,,/1/?q={morele_phrase}').text
        morele_soup = BeautifulSoup(morele, 'lxml')

        morele_products = []
        for div in morele_soup.find_all('div', class_='cat-product card'):
            item_image = div.find('img', class_='product-image')['src']

            item_name = div.find('div', class_='cat-product-center-inside').h2.a.text

            item_price = div.find('div', class_='price-new').text

            morele_products.append({'item_image': item_image,
                                    'item_name': item_name,
                                    'item_price': change_string_to_int(item_price)})

        # code for second page
        x_kom_phrase = '%20'.join(looking_for_split)
        x_kom = requests.get(f'https://www.x-kom.pl/szukaj?q={x_kom_phrase}').text
        x_kom_soup = BeautifulSoup(x_kom, 'lxml')

        x_kom_products = []
        for div in x_kom_soup.find_all('div', class_='sc-162ysh3-1 bsrTGN sc-bdVaJa cRgopZ'):
            item_image = div.find('img', class_='sc-1tblmgq-1 bxjRuC')['src']

            item_name = div.find('div', class_='sc-3g60u5-0 cDisn').a.h3.text

            item_price_source = div.find('div', class_='sc-6n68ef-1 eOCAwm')
            item_price = item_price_source.find(class_='sc-6n68ef-3').text

            x_kom_products.append({'item_image': item_image,
                                   'item_name': item_name,
                                   'item_price': change_string_to_int(item_price)})

        # code for third page
        komputronik_phrase = '%20'.join(looking_for_split)
        komputronik = requests.get(f'https://www.komputronik.pl/search/category/1?query={komputronik_phrase}').text
        komputronik_soup = BeautifulSoup(komputronik, 'lxml')

        komputronik_products = []
        stage_1 = komputronik_soup.find_all(class_='product-entry2')

        for div in stage_1:
            item_image_source = div.find('div', class_='pe2-img').a.img

            print(item_image_source)
            print(item_image_source['src'])

            print('OK')
            # item_image = item_image_source['src']

            # item_name = div.find('div', class_='pe2-head').a.text
            #
            # item_price = div.find('div', class_='prices').text

            # komputronik_products.append({'item_image': item_image,
            #                              'item_name': item_name,
            #                              'item_price': item_price})

        print(komputronik_products)

        # x_kom_prices = []
        # for item in x_kom_products:
        #     x_kom_prices.append(item['item_price'])
        # min_price = min(x_kom_prices)
        # max_price = max(x_kom_prices)
        # medium_price = median(x_kom_prices)

        return render_template('results.html', title='Results', products1=morele_products,
                               products2=x_kom_products, products3=komputronik_products)

    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='About')


@app.route("/results")
def results():
    return render_template('results.html', title='Results')


if __name__ == '__main__':
    app.run(debug=True)
