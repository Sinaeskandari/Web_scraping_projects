from selenium import webdriver

browser = webdriver.Chrome()
# please enter the name correctly only letters and no the 'the'
n = input('enter movie name:').replace(' ', '_')
# store the data in a dictionary to write in json file later
details = {}
# data from movie main page
browser.get('https://www.rottentomatoes.com/m/' + n)
# rate of rottentomatoes
tomatometer = browser.find_element_by_id('tomato_meter_link')
details['tomatometer'] = str(tomatometer.text)
# rate of people
audience_score = browser.find_element_by_xpath(
    '//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/h2/a/span[2]')
details['audience_score'] = str(audience_score.text)
# gist of movie
movie_info = browser.find_element_by_id('movieSynopsis')
details['movie_info'] = str(movie_info.text)
# cast
i = 1
cast = []
browser.find_element_by_id('showMoreCast').click()
# loop for finding cast
while True:
    try:
        c = browser.find_element_by_css_selector(
            '#movie-cast > div > div > div:nth-child({}) > div > a > span'.format(i))
        cast.append(str(c.text))
        i += 1
    except:
        break
details['cast'] = cast
# review page
browser.get(browser.current_url + '/reviews')
critics = browser.find_elements_by_class_name('the_review')
c = []
for critic in critics:
    c.append(critic.text)
details['critics'] = c
#writing the file
with open(f'{n}.json', 'w') as f:
    f.write(str(str(details).encode('utf-8')).replace('\ '.strip(), ''))
