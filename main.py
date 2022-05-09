import json

from requests_html import HTMLSession
from models import Model
import time


def get_page_html(session, url):
    # collect all the HTML we need until there are no more pages
    base_url = 'https://www.adidas.co.uk'
    all_html = []
    while True:
        resp = session.get(url)
        print(url)
        all_html.append(resp.html)
        try:
            url = base_url + resp.html.find('a[data-auto-id=plp-pagination-next]', first=True).attrs['href']
        except AttributeError:
            break
    return all_html


def parse_product_codes(html):
    # get all the product codes from the page
    items = html.find('div.grid-item')
    product_codes = [item.attrs['data-grid-id'] for item in items]
    return product_codes


def get_product_json(session, product_id):
    # this is to get the product data
    resp = session.get(f"https://www.adidas.co.uk/api/products/{product_id}")
    return resp.json()


def load_json_model(json_data):
    product_model = Model(**json_data)
    return product_model


def main():
    results = []
    s = HTMLSession()
    url = 'https://www.adidas.co.uk/outdoor-men-hiking-shoes'
    html_list = get_page_html(s, url)
    for html_idx, html_data in enumerate(html_list, start=1):
        codes = parse_product_codes(html_data)
        for idx, c in enumerate(codes, start=1):
            item = load_json_model(get_product_json(s, c))
            results.append(item.dict())
            print(f"gathered item {c} index {idx}/{len(codes)} from page {html_idx}")
            time.sleep(0.1)

    with open('results.json', 'w') as f:
        json.dump(results, f)


if __name__ == '__main__':
    main()
