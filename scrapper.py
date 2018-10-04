#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup


URL = "https://www.carters.com/carters-lbb"


class Webscrapper(object):

    def __init__(self, source_url):
        req = urllib.request.Request(
            source_url,
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; '
                              'rv:61.0) Gecko/20100101 Firefox/61.0'
            }
        )

        source_html = urllib.request.urlopen(req).read()
        self.soup = BeautifulSoup(source_html, 'html.parser')

    def get_page_title(self):
        return self.soup.title.string

    def get_products_links(self):
        # Collect all product links for product in the web page.
        products_hrefs = []
        products_divs = self.soup.find_all("div", class_="product-tile ")
        for x in products_divs:
            href = x.find('a')['href']
            products_hrefs.append(href)
        return products_hrefs

    def get_products_name(self):
        product_names = []
        products_name_links = self.soup.find_all("a", class_="name-link")
        for name in products_name_links:
            product_names.append(name.get_text().replace("\n", ""))
        return product_names


if __name__ == "__main__":
    scape_obj = Webscrapper(URL)
    title = scape_obj.get_page_title()
    product_links = scape_obj.get_products_links()
    product_names = scape_obj.get_products_name()
    for pl in product_links:
        print(pl)

