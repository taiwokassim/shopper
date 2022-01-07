from scraper.asos import asos_scraper_bot
from flask import Flask, render_template, request, jsonify
from scraper import jumia, konga, asos, payporte
from flask_cors import CORS
import random

app = Flask(__name__, static_url_path='',
            static_folder='static',)
CORS(app)


@app.route('/')
def search():
    if 'search' in request.args:
        key = request.args['search']
        products = []
        products = jumia.jumia_scraper_bot(key)
        products.extend(konga.konga_scraper_bot(key))
        products.extend(payporte.payporte_scraper_bot(key))
        products.extend(asos.asos_scraper_bot(key))
        random.shuffle(products)
        random.shuffle(products)
        return render_template("index.html", keyword=key, products=products)

    return render_template("index.html")


@app.route('/api')
def searchApi():
    key = request.args.get('search')
    products = []
    products = jumia.jumia_scraper_bot(key)
    products.extend(konga.konga_scraper_bot(key))
    products.extend(payporte.payporte_scraper_bot(key))
    random.shuffle(products)
    random.shuffle(products)

    return jsonify({'data': products})


if __name__ == '__main__':
    app.run()
