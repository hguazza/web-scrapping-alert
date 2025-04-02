import requests

def fetch_page(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "https://www.mercadolivre.com.br/macbook-air-m2-2022-midnight-16gb-de-ram-256gb-ssd-apple-m/p/MLB29578461#polycard_client=search-nordic&searchVariation=MLB29578461&wid=MLB4020634589&position=4&search_layout=grid&type=product&tracking_id=64fa67f8-9370-40ec-8bda-f0f673393914&sid=search"
    page_content = fetch_page()
    print(page_content)
