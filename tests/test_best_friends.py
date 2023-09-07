import pytest
from selene import Browser, by, have, config
from selene.support.shared import browser
import time
from selene.support.shared.jquery_style import s, ss


# def test_open_registration_page():
#     browser.open('http://opencart.qatestlab.net/')
#
#     browser.element(by.text('My Account')).click()
#     browser.element('[href="http://opencart.qatestlab.net/index.php?route=account/register"]').click()
#
#     browser.element('[name="firstname"]').type('Edgar')
#     browser.element('[name="lastname"]').type('1234')
#     browser.element('[name="email"]').type('50125@friends.com')
#     browser.element('[name="telephone"]').type('1515')
#     browser.element('[name="password"]').type('12345pass')
#     browser.element('[name="confirm"]').type('12345pass')
#
#     browser.element('[href="http://opencart.qatestlab.net/index.php?route=information/information/agree&information_id=3"]').click()
#
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
#     browser.element('[name="email"]').type('50125@friends.com')
#     browser.element('[name="password"]').type('12345pass')
#     browser.element('[#top-links > ul > li > ul > li:nth-child(2) > a]').type('12345pass')
#
#     time.sleep(5)
# browser.element('[value="Login"]').click()

# def test_search_product():
#     browser.open('http://opencart.qatestlab.net/')
#
#     search_input = browser.element('[name="search"]').type('easipet')
#     browser.element('#search > button').click()
#     time.sleep(5)
#     search_results = browser.all('.product-layout')
#     assert len(search_results) > 0, "No search results found"

@pytest.mark.skip()
def test_add_product():
    browser.open('http://opencart.qatestlab.net/')
    s('[href="http://opencart.qatestlab.net/index.php?route=product/category&path=31"]').click()
    s('#content > div:nth-child(2) > div:nth-child(3) > div > div.content > div > h4 > a').click()
    ss('.sbHolder .sbToggle')[0].click()
    time.sleep(2)
    s('[href="#19"]').click()
    time.sleep(2)
    ss('.sbHolder .sbToggle')[1].click()
    time.sleep(2)
    s('[href="#22"]').click()
    time.sleep(2)
    s('#button-cart.btn-primary').click()
    time.sleep(2)
    s('#cart-total2').should(have.text('1'))

@pytest.mark.skip()
def test_shopping_cart():
    browser.open('http://opencart.qatestlab.net/')
    time.sleep(5)
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=product/category&path=31"]').click()
    time.sleep(5)
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=product/product&path=31&product_id=34"]').click()
    time.sleep(5)
    browser.element('[href="#tab-specification"]').click()
    time.sleep(5)
    browser.element('.counter.counter-plus.material-design-add186').click()
    time.sleep(5)
    browser.element('#button-cart.btn-primary').click()
    time.sleep(5)

# код Володимира
# def test_registration():
#     browser.open('http://opencart.qatestlab.net/')
#
#     browser.element('.toggle.active').click()
#     time.sleep(2)
#     browser.element('#todo-list>li:nth-of-type(1)').click()
#     time.sleep(5)
#     browser.element('#input-firstname').type('firstname').press_tab()
#     time.sleep(2)
#     browser.element('#input-lastname').type('12345').press_tab()
#     time.sleep(2)
#     browser.element('#input-email').type('volodymyr@ddd').press_tab()
#     time.sleep(2)
#     browser.element('#input-telephone').type('12322344345').press_tab()
#     time.sleep(2)
#     browser.element('#input-password').type('12345').press_tab()
#     time.sleep(2)
#     browser.element('#input-confirm').type('12345').press_tab()
#     time.sleep(2)
#     browser.element('[name="agree"]').click()
#
#     browser.element('.btn.btn-primary').click()

def test_brain():
    browser.open('https://duckduckgo.com/')
    browser.driver.maximize_window()
    s(by.name('q')).type('brain магазин').press_enter()
    time.sleep(2)
    ss(".LnpumSThxEWMIsDdAT17")[0].click()
    time.sleep(2)
    ss(by.text('Увійти'))[0].click()
    time.sleep(2)
    ss('#modal-login-phone-field')[0].type('+38 (096) 607-20-14').press_tab()
    time.sleep(2)
    ss('#modal-login-password-field')[0].type('769f3858b5')
    time.sleep(2)
    ss(by.text('Увійти'))[2].click()
    time.sleep(2)
    s(by.text("Ноутбуки і комп'ютери")).click()
    time.sleep(2)
    ss(by.text('Перейти'))[0].click()
    time.sleep(2)
    s('[href="/ukr/Noutbuk_Lenovo_V15_82KB0006RA-p827070.html"]').click()
    time.sleep(2)
    s('[data-articul="82KB0006RA"]').click()
    time.sleep(1)
    s('//*[@id="br-pr-2"]/a').click()
    s('body > header > div.header-bottom > div > div > div.cart.js-cart.br-h-cart > button').click()
    time.sleep(1)
    ss('.increment')[1].click()
    time.sleep(1)
    s('//*[@id="cart_list"]/div[2]/div/div[2]/div/button').click()
    time.sleep(2)
    s(by.text('Видалити не зберігаючи')).click()
    time.sleep(2)
    browser.quit()
