import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#To do list:
#Create an error handler in case of website scraping error

#Note:
#output function dalam bentuk list yang berisi Link, img source, nama, dan price

def scrapeTokopedia(name):
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

# def scrapeShopee(name):#might be impossible??? idk sumpah redirect ke login terus
#     url = 'https://shopee.co.id/search?keyword='+name
#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Language": "en-US,en;q=0.9"
#     }
#     response = requests.get(url,headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return

def scrapeLazada(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver_path = './chromedriver.exe'

    browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    search_url = f'https://www.lazada.co.id/catalog/?q={query}&_keyori=ss'

    # load the search page
    browser.get(search_url)
    browser.execute_script("window.scrollTo(300, 0);")
    scroll_height = browser.execute_script("return document.body.scrollHeight")
    while browser.execute_script("return window.pageYOffset + window.innerHeight") < scroll_height:
        browser.execute_script("window.scrollBy(0, 50);")
        time.sleep(0.1)

    html_content = browser.page_source

    soup = BeautifulSoup(html_content, 'html.parser')

    product_items = soup.find_all('div', {'class': 'Bm3ON'})
    products = []
    #print(product_items)

    for product_item in product_items:
        #print(product_item)
        img = product_item.find('img',{'class':'jBwCF'})['src']
        name = product_item.find('img',{'class':'jBwCF'})['alt']
        link = product_item.find('a')['href']
        link = link.replace("//", "")
        price = product_item.find('span', {'class': 'ooOxS'}).text

        products.append({'link': link,'img_src': img,'name':name, 'price': price})
    return products



def dailyScrape():
    #Code here for getting data from the database, should be in a form of 1d array with inside of it is name

    #end code
    #Node: Name need to be pre-processed so that any space ' ' changed into '+', atleast on tokopedia. other idk
    scrapelist =['bakso','kalkulator']#temp array
    for i in scrapelist:
        lazada_list=scrapeLazada(i)
        # shopee_list=scrapeShopee(i)
        tokopedia_list=scrapeTokopedia(i)
        #idk ini mau process lagi gmn, either cmn langsung taro average harga dlm database atau gmn.
    return