#!/usr/bin/python3
"""Flask app displaying product data from JSON or CSV."""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def read_csv(filename):
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    return render_template('items.html', items=data.get('items', []))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                    error="Invalid product ID")

        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html',
                                    error="Product not found")
        return render_template('product_display.html', products=filtered)

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)