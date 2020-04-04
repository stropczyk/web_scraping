from flask import render_template, request, Blueprint
from web_scraping.main.searching import morele_net, x_kom, komputronik
from web_scraping.main.functions import get_product
from statistics import median_low

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['product']
        phrase = user_input.split(' ')

        morele_products = morele_net(phrase)
        x_kom_products = x_kom(phrase)
        komputronik_products = komputronik(phrase)

        products = morele_products + x_kom_products + komputronik_products
        sorted_list = sorted(products, key=lambda i: i['item_price'])
        best_value = sorted_list[0]
        medium_price = median_low(i['item_price'] for i in sorted_list)
        medium_value = get_product(medium_price, sorted_list)
        worst_value = sorted_list[-1]

        return render_template('results.html', title='Results', product1=best_value,
                               product2=medium_value, product3=worst_value)

    return render_template('home.html', title='Home')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/contact")
def contact():
    return render_template('contact.html', title='About')


@main.route("/results")
def results():
    return render_template('results.html', title='Results')