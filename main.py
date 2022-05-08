from requests_html import HTMLSession
from models import Model
import time


def get_page_html(session, url):
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
    s = HTMLSession()
    url = 'https://www.adidas.co.uk/outdoor-men-hiking-shoes'
    html_list = get_page_html(s, url)
    for html_data in html_list:
        codes = parse_product_codes(html_data)
        for c in codes:
            item = load_json_model(get_product_json(s, c))
            print(item.json())
            time.sleep(0.2)


if __name__ == '__main__':
    main()
