from bs4 import BeautifulSoup
import requests
from web_scraping.main.functions import change_string_to_int, change_string_to_int_2


# code for first page
def morele_net(phrase):
    morele_phrase = '+'.join(phrase)
    morele = requests.get(f'https://www.morele.net/wyszukiwarka/0/0/,,,,,,,,,,,,/1/?q={morele_phrase}').text
    morele_soup = BeautifulSoup(morele, 'lxml')

    morele_products = []
    for div in morele_soup.find_all('div', class_='cat-product card'):
        item_image = div.find('img', class_='product-image')['src']

        item_name = div.find('div', class_='cat-product-center-inside').h2.a.text

        link = div.find('div', class_='cat-product-center-inside').h2.a['href']

        item_price = div.find('div', class_='price-new').text

        morele_products.append({'item_image': item_image,
                                'item_name': item_name,
                                'item_price': change_string_to_int(item_price),
                                'link': f'https://www.morele.net{link}'})
    return morele_products


# code for second page
def x_kom(phrase):
    x_kom_phrase = '%20'.join(phrase)
    x_kom = requests.get(f'https://www.x-kom.pl/szukaj?q={x_kom_phrase}').text
    x_kom_soup = BeautifulSoup(x_kom, 'lxml')

    x_kom_products = []
    for div in x_kom_soup.find_all('div', class_='sc-162ysh3-1 bsrTGN sc-bdVaJa cRgopZ'):
        item_image = div.find('img', class_='sc-1tblmgq-1 bxjRuC')['src']

        item_name = div.find('div', class_='sc-3g60u5-0 cDisn').a.h3.text

        item_price_source = div.find('div', class_='sc-6n68ef-1 eOCAwm')
        item_price = item_price_source.find(class_='sc-6n68ef-3').text

        link = div.find('div', class_='sc-1yu46qn-9 gxYtMJ sc-3g60u5-0 cDisn').a['href']

        x_kom_products.append({'item_image': item_image,
                               'item_name': item_name,
                               'item_price': change_string_to_int(item_price),
                               'link': f'https://www.x-kom.pl{link}'})
    return x_kom_products


# code for third page
def komputronik(phrase):
    komputronik_phrase = '%20'.join(phrase)
    komputronik = requests.get(f'https://www.komputronik.pl/search/category/1?query={komputronik_phrase}').text
    komputronik_soup = BeautifulSoup(komputronik, 'lxml')

    komputronik_products = []
    stage_1 = komputronik_soup.find('ul', class_='product-entry2-wrap')
    stage_2 = stage_1.find_all('li', class_='product-entry2')

    for item in stage_2:
        img = item.find('div', class_='pe2-img').a.img
        img1 = img
        item_image_source = img1
        item_image = item_image_source['data-original']

        item_name = item.find('div', class_='pe2-head').a.text

        link = item.find('div', class_='pe2-head').a['href']

        item_price = item.find('div', class_='prices')
        item_price_2 = item_price.find(class_='price').text

        komputronik_products.append({'item_image': item_image,
                                     'item_name': item_name,
                                     'item_price': change_string_to_int_2(item_price_2),
                                     'link': link})
    return komputronik_products
