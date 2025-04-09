import requests
from bs4 import BeautifulSoup
import time

def fetch_page(url):
    response = requests.get(url)
    return response.text

def parse_page(html):
    """
    Parses the HTML content of the page to extract product details 
    and return them as a dictionary.
    """
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('div', class_='header-product-info--title').get_text(strip=True)
    dolar_product_price = float(soup.find('div', class_='header-product-info--price').get_text(strip=True).replace('.', '').replace(',', '.').replace('$', '').replace('US', ''))
    other_currencies_product_price =  soup.find('div', class_='header-product-info--currency').get_text(strip=True).replace('R$', '').replace('.', '').replace(',', '.').replace('$', '')
    reais_product_price = float(other_currencies_product_price.split()[0])
    peso_arg_product_price = float(other_currencies_product_price.split()[1])
    dolar_reais_quote = reais_product_price / dolar_product_price
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')


    
    return {
        'product_name': product_name,
        'price_dolars': dolar_product_price,
        'price_reais': reais_product_price,
        'price_pesos_arg': peso_arg_product_price,
        'dolar_reais_quote': dolar_reais_quote,
        'timestamp': timestamp
    }



if __name__ == '__main__':
    url = 'https://mobile.comprasparaguai.com.br/notebook-apple-macbook-pro-2023-apple-m2-pro-memoria-16gb-ssd-512gb-162_45342/'
    html_content = fetch_page(url)
    product_info = parse_page(html_content)
    print(product_info)