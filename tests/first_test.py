# import time
#
# from selene import browser, have
# from selene.support.shared import config
# from selene.support.shared.jquery_style import s, ss

# config.window_width = 1920
# config.window_height = 1080
#
# browser.open('https://itstep.org/uk')
# time.sleep(5)
#
# ss('.marker-city.cremenchug-small .marker-point').first.click()
# page_text = browser.driver.page_source.lower()
# count = page_text.count('it step')
# print('Вираз it step повторюється:', count, 'рази')

import time
from selene.api import browser, s, ss

def test_search_and_count():
    browser.open('https://duckduckgo.com/')
    s('[name="q"]').type('шахтар').press_enter()
    time.sleep(5)
    ss(".result__url").element(2).click()

    page_text = browser.driver.page_source.lower()
    word_to_count = "шахтар"
    count = page_text.count(word_to_count)
    print(f'Слово "{word_to_count}" зустрічається на сторінці {count} раз(ів)')
    assert count > 0, f'Слово "{word_to_count}" не знайдено на сторінці'
    browser.quit()

