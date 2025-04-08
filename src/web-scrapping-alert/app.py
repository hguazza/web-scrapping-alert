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
    product_name = soup.find('h1', class_='ui-pdp-title').text.strip()
    prices = soup.find_all('span', class_='andes-money-amount__fraction')
    old_price = int(prices[0].get_text(strip=True).replace('.', ''))
    new_price = int(prices[1].get_text(strip=True).replace('.', ''))
    installment_price = int(prices[2].get_text(strip=True).replace('.', ''))

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price,
        'timestamp': timestamp
    }



if __name__ == "__main__":
    url = "https://www.mercadolivre.com.br/macbook-air-m2-2022-midnight-16gb-de-ram-256gb-ssd-apple-m/p/MLB29578461#polycard_client=search-nordic&searchVariation=MLB29578461&wid=MLB4020634589&position=4&search_layout=grid&type=product&tracking_id=64fa67f8-9370-40ec-8bda-f0f673393914&sid=search"
    page_content = fetch_page(url)
    product_info = parse_page(page_content)
    print(product_info)
    time.sleep(10)