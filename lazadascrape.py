from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver_path = './chromedriver.exe'

browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options, desired_capabilities=capa)

def scrapeLazada(query) -> list[dict]:
	products = []
	try:
		url = f"https://www.lazada.co.id/tag/{query.replace(' ', '-')}"

		browser.get(url)
		wait = WebDriverWait(browser, 10)
		url = f"https://www.lazada.co.id/tag/{query}/?ajax=true&isFirstRequest=true&page=1"

		def waitcon(browser):
			res = browser.find_elements(By.CLASS_NAME, 'Bm3ON')
			return res if len(res) > 10 else False

		product_items = wait.until(waitcon)
		scroll_height = browser.execute_script("return document.body.scrollHeight")
		while browser.execute_script("return window.pageYOffset + window.innerHeight") < scroll_height:
			browser.execute_script("window.scrollBy(0, 50);")

		for product_item in product_items:
			img = product_item.find_element(By.CLASS_NAME, "jBwCF").get_attribute("src")
			name_and_link = product_item.find_element(By.CLASS_NAME, "RfADt")
			link = name_and_link.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
			name = name_and_link.find_element(By.CSS_SELECTOR, "a").get_attribute("title")
			price = product_item.find_element(By.CLASS_NAME, "ooOxS").get_attribute("innerHTML")
			products.append({'link': link,'img_src': img,'name':name, 'price': price})

		browser.execute_script("window.scrollBy(-1 * document.body.scrollHeight, 0);")
	except:
		pass
	return products
