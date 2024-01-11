from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
import time
chrome_path = chromedriver_autoinstaller.install() 
driver = webdriver.Chrome(chrome_path)
url = "https://www.inmotionhosting.com/"
driver.get(url)
time.sleep(5)
plan_elements = driver.find_elements_by_class_name('plan')
data = []

for plan_element in plan_elements:
    plan_name = plan_element.find_element_by_class_name('plan-name').text
    features = plan_element.find_element_by_class_name('plan-features').text
    price = plan_element.find_element_by_class_name('plan-price').text
    data.append({
        'plan_name': plan_name,
        'features': features,
        'price': price
    })
print(data)
driver.quit()
