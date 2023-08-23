from selene.api import browser, s, ss
from selene.support.conditions import have

def test_search_and_check_links():
    browser.open('https://duckduckgo.com/')
    s('[name="q"]').type('yashaka selene').press_enter()
    s('a[href^="https://github.com/yashaka/selene"]').click()
    assert ss('a[href="/yashaka/selene"]').should(have.size(3))
    browser.quit()


