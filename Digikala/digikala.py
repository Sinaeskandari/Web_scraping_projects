from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Dictionary to store the data that we scraped.
details = {}
# Product name
# It doesn't need to be the full name.
n = input("Enter something to search:")
browser = webdriver.Chrome()
browser.get('https://www.digikala.com')
# We need to  find the search box by its name.
search_box = browser.find_element_by_name('q')

search_box.send_keys(n)
search_box.send_keys(Keys.ENTER)
# First item in the page.
item = browser.find_element_by_xpath(
    '//*[@id="content"]/div/div/div/div[2]/div/article/div/ul/li[1]/div/div[2]/div[1]/div[1]/a')
item.click()
# Change the window.
browser.switch_to.window(browser.window_handles[1])
# Make sure the product page loaded.
input('Press enter to continue')
# Make sure the product is available and has a price.
try:
    price = browser.find_element_by_xpath("//div[@class='c-product__seller-price-raw js-price-value']")


    def translate_price(p):
        persian_num = {'۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8',
                       '۹': '9', ',': ''}
        price = ''
        for n in p:
            price += persian_num[n]
        return price


    details["price"] = translate_price(str(price.text))
except:
    details["price"] = "Not available"
comment_section = browser.find_element_by_css_selector('#tabs > ul > li:nth-child(3) > a')
# This is the method i used and i explain about it in attachment pdf.
browser.execute_script("arguments[0].click();", comment_section)
# Wait until the comment section loaded completely.
sleep(4)


def check(n):
    if n == 'عالی':
        return 'great'
    elif n == 'خوب':
        return 'good'
    elif n == 'معمولی':
        return 'medium'
    elif n == 'بد':
        return 'bad'
    else:
        return "unknown"


# Find details
quality = browser.find_element_by_xpath('//*[@id="tabs"]/div/div[3]/div[1]/div[1]/ul/li[1]/div[2]/div/div')
val_quality = quality.get_attribute("data-rate-digit")
details['quality'] = check(val_quality)
value = browser.find_element_by_xpath('//*[@id="tabs"]/div/div[3]/div[1]/div[1]/ul/li[2]/div[2]/div')
val_value = value.get_attribute("data-rate-digit")
details['value'] = check(val_value)
creativity = browser.find_element_by_xpath('//*[@id="tabs"]/div/div[3]/div[1]/div[1]/ul/li[3]/div[2]/div')
val_creativity = creativity.get_attribute('data-rate-digit')
details['creativity'] = check(val_creativity)
facilities = browser.find_element_by_xpath('//*[@id="tabs"]/div/div[3]/div[1]/div[1]/ul/li[4]/div[2]/div')
val_facilities = facilities.get_attribute('data-rate-digit')
details['facilities'] = check(val_facilities)
ease = browser.find_element_by_xpath('//*[@id="tabs"]/div/div[3]/div[1]/div[1]/ul/li[5]/div[2]/div')
val_ease = ease.get_attribute('data-rate-digit')
details['ease of use'] = check(val_ease)
design = browser.find_element_by_xpath('//*[@id="tabs"]/div/div[3]/div[1]/div[1]/ul/li[6]/div[2]/div')
val_design = design.get_attribute('data-rate-digit')
details['design'] = check(val_design)
with open(f'{n}.txt', 'w') as f:
    print(str(details), file=f)
browser.close()
