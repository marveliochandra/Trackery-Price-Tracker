from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
chrome_options = Options()
chrome_options.add_argument("--headless")

driver_path = './chromedriver.exe'

browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)


def scrapeTokopedia(name) -> list[dict]:
    if name:
        url = 'https://www.tokopedia.com/search?st=product&q='+name
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9"
        }
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        product_div = soup.find_all('div', {'data-testid': 'master-product-card'})
        data_list = [
        {
            'link': product.find('a', {'class': 'pcv3__info-content css-gwkf0u'})['href'],
            'img_src': product.find('img', {'class': 'css-1q90pod'})['src'],
            'name': product.find('div', {'data-testid': 'spnSRPProdName'}).text.strip(),
            'price': product.find('div', {'data-testid': 'spnSRPProdPrice'}).text.strip()
        }
        for product in product_div
        ]
        return data_list

