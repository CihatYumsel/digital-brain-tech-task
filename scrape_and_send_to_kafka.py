import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer
import json
import time
import sys

KAFKA_SERVER = ['localhost:9092']
KAFKA_TOPIC = 'shop_data'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8')
)

def get_product_details(product_url):
    try:
        response = requests.get(product_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        description_element = soup.find('div', class_='woocommerce-product-details__short-description')
        stock_element = soup.find('p', class_='stock in-stock')
        
        description = description_element.get_text(strip=True) if description_element else 'No Description'
        stock = stock_element.get_text(strip=True) if stock_element else 'No Stock Info'
        
        return description, stock
    except Exception as e:
        return 'No Description', 'No Stock Info'

def get_data():
    url = 'https://scrapeme.live/shop/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []

    product_list = soup.find('ul', class_='products columns-4')

    if product_list:
        products = product_list.find_all('li', class_='product')
        for product in products:
            link_element = product.find('a', class_='woocommerce-LoopProduct-link')
            product_url = link_element['href'] if link_element else None
            
            title_element = product.find('h2', class_='woocommerce-loop-product__title')
            price_element = product.find('span', class_='woocommerce-Price-amount amount')
            
            title = title_element.get_text(strip=True) if title_element else 'No Title'
            price = price_element.get_text(strip=True) if price_element else 'No Price'
            
            description, stock = get_product_details(product_url) if product_url else ('No Description', 'No Stock Info')

            data.append({
                'title': title,
                'price': price,
                'description': description,
                'stock': stock
            })

    return data

def main():
    last_data = None
    all_products_fetched = False

    while not all_products_fetched:
        data = get_data()
        
        if data and data != last_data:
            producer.send(KAFKA_TOPIC, data)
            producer.flush()
            last_data = data
            print(f"Data sent to Kafka: {data}")

        if len(data) > 0 and 'No Title' not in [item['title'] for item in data]:
            all_products_fetched = True
            print("All products fetched. Shutting down.")

        time.sleep(1)

    print("Process completed and program is shutting down.")
    sys.exit()

if __name__ == "__main__":
    main()
