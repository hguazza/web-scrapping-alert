import asyncio
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import sqlite3
from dotenv import load_dotenv
import os
from telegram import Bot

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
bot = Bot(token=TOKEN)

def fetch_page(url):
    response = requests.get(url)
    return response.text

def parse_page(html):
    """
    Parses the HTML content of the page to extract product details 
    and return them as a dictionary.
    """
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_='ui-pdp-title').get_text(strip=True)
    product_price = int(soup.find('span', class_='andes-money-amount__fraction').get_text(strip=True).replace('.', ''))
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')


    
    return {
        'product_name': product_name,
        'price': product_price,
        'timestamp': timestamp
    }


def create_connection(db_name='macbook_prices.db'):
    """
    Creates a connection to the SQLite database and returns the connection object.
    """
    conn = sqlite3.connect(db_name)
    return conn

def setup_database(conn):
    """
    Sets up the table in the database if it doesn't exist.
    """
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            price INTEGER,
            timestamp TEXT
        )
    ''')
    conn.commit()

def save_to_database(conn, data):
     """
    Saves the product information to the database
     """
     df = pd.DataFrame([data])
     df.to_sql('prices', conn, if_exists='append', index=False)


def get_min_price(conn):
    """
    Retrieves the minimum price from the database.
    """
    cursor = conn.cursor()
    cursor.execute('SELECT MIN(price), timestamp FROM prices')
    result = cursor.fetchone()
    if result and result[0] is not None:
        return result[0], result[1]
    return None, None

async def send_telegram_message(text):
    """
    Sends a message to the specified Telegram chat.
    """
    await bot.send_message(chat_id=CHAT_ID, text=text)

async def main():
        url = "https://www.mercadolivre.com.br/apple-iphone-16-pro-1-tb-titnio-preto-distribuidor-autorizado/p/MLB1040287851#polycard_client=search-nordic&wid=MLB5054621110&sid=search&searchVariation=MLB1040287851&position=6&search_layout=stack&type=product&tracking_id=92c2ddf6-f70e-475b-b41e-fe2742459774"

        # setting up the database
        conn = create_connection()
        setup_database(conn)

        try:
            while True:
                # Fetching and parsing the page
                page_content = fetch_page(url)
                product_info = parse_page(page_content)
                current_price = product_info['price']

                # get minimun price and its timestamp from the database
                min_price, min_price_timestamp = get_min_price(conn)
                
                # Program logic -> check if there is new lowest price
                if current_price is None or current_price < min_price:
                    print(f"Lowest price found: {current_price} at {product_info['timestamp']}")
                    min_price = current_price
                    min_price_timestamp = product_info['timestamp']
                    await send_telegram_message(f"Lowest price found: {min_price} at {min_price_timestamp}")
                else:
                    print(f"Current price: {current_price} - No new lowest price found.")
                    await send_telegram_message(f"Current price: {current_price} - No new lowest price found.")

                # Saving product information to sqlite database
                save_to_database(conn, product_info)
                print("Dados salvos no banco:", product_info)

                await asyncio.sleep(10)

        except KeyboardInterrupt:
            print("Process interrupted by user.")
        finally:
            conn.close()

asyncio.run(main())