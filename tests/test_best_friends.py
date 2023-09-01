from selene import Browser, by
from selene.support.shared import browser
import time

# def test_open_registration_page():
#     browser.open('http://opencart.qatestlab.net/')
#
#     browser.element(by.text('My Account')).click()
#     browser.element('[href="http://opencart.qatestlab.net/index.php?route=account/register"]').click()
#
# def test_fill_registration_form():
#     browser.element('[name="firstname"]').type('Edgar')
#     browser.element('[name="lastname"]').type('1234')
#     browser.element('[name="email"]').type('0125@friends.com')
#     browser.element('[name="telephone"]').type('1515')
#     browser.element('[name="password"]').type('12345pass')
#     browser.element('[name="confirm"]').type('12345pass')
#
# def test_accept_privacy_policy():
#     browser.element('[href="http://opencart.qatestlab.net/index.php?route=information/information/agree&information_id=3"]').click()
#
# def test_submit_registration_form():
#     browser.element('[value="Continue"]').click()


# def test_open_registration_page():
#     browser.open('http://opencart.qatestlab.net/')
#
#     browser.element(by.text('My Account')).click()
#     browser.element('[href="http://opencart.qatestlab.net/index.php?route=account/register"]').click()


# def test_login():
#     browser.element(by.text('My Account')).click()
#     browser.element('[href="http://opencart.qatestlab.net/index.php?route=account/login"]').click()
#
#     browser.element('[name="email"]').type('0125@friends.com')
#     browser.element('[name="password"]').type('12345pass')
#     browser.element('[#top-links > ul > li > ul > li:nth-child(2) > a]').type('12345pass')
#
#     time.sleep(5)
    # browser.element('[value="Login"]').click()

# def test_search_product():
#     browser.open('http://opencart.qatestlab.net/')
#
#     search_input = browser.element('[name="search"]').type('easipet')
#     browser.element('[#search > button]').click()
#     time.sleep(5)
#     search_results = browser.all('.product-layout')
#     assert len(search_results) > 0, "No search results found"

# код Володимира
def test_registration():
    browser.open('http://opencart.qatestlab.net/')

    browser.element('.toggle.active').click()
    time.sleep(2)
    browser.element('#todo-list>li:nth-of-type(1)').click()
    time.sleep(5)
    browser.element('#input-firstname').type('firstname').press_tab()
    time.sleep(2)
    browser.element('#input-lastname').type('12345').press_tab()
    time.sleep(2)
    browser.element('#input-email').type('volodymyr@ddd').press_tab()
    time.sleep(2)
    browser.element('#input-telephone').type('12322344345').press_tab()
    time.sleep(2)
    browser.element('#input-password').type('12345').press_tab()
    time.sleep(2)
    browser.element('#input-confirm').type('12345').press_tab()
    time.sleep(2)
    browser.element('[name="agree"]').click()

    browser.element('.btn.btn-primary').click()







