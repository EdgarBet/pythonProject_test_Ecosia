import time

from selene import browser, have
from selene.support.shared import config
from selene.support.shared.jquery_style import s, ss

config.window_width = 1920
config.window_height = 1080

browser.open('https://itstep.org/uk')
time.sleep(5)

ss('.marker-city.cremenchug-small .marker-point').first.click()
page_text = browser.driver.page_source.lower()
count = page_text.count('it step')
print('Вираз it step повторюється:', count, 'рази')
