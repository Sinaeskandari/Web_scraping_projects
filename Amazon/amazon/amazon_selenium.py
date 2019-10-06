from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from math import ceil
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
browser.get('https://www.amazon.com')
input_text = browser.find_element_by_css_selector('#twotabsearchtextbox')
input_text.send_keys(input('What do you want to search:'))
input_text.send_keys(Keys.ENTER)
link = browser.find_element_by_css_selector(
    '#pdagDesktopSparkleAsinsContainer > div:nth-child(1) > div.block.desktopSparkle__asin--desc > a')
link.click()
sleep(5)
link = browser.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a')
link.click()
sleep(5)
try:
    comment_quantity = str(browser.find_element_by_xpath(
        '//*[@id="cm_cr-product_info"]/div/div[1]/div[2]/div/div/div[2]/div/span').text).replace(',', '')
    page_nums = ceil(int(comment_quantity) / 10)
    next_page = browser.find_element_by_css_selector('#cm_cr-pagination_bar > ul > li.a-last > a')
    next_page.click()
    this_url = browser.current_url.replace('_2', '_{}')
    this_url = this_url.replace('=2', '={}')
    url_list = []
    for n in range(1, page_nums + 1):
        url = this_url.format(n, n)
        url_list.append(url)
except NoSuchElementException:
    url_list = []
    url_list.append(browser.current_url)

with open('links.txt', 'w') as f:
    for l in url_list:
        print(l, file=f)
browser.close()