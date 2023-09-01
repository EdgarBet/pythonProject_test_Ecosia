import math
# def test_sqrt():
#     num = 25
#     assert math.sqrt(num) == 5
#
# def testsquare():
#     num = 7
#     assert 7*7 == 40
#
# def testquality():
#     assert 10 == 11

# def test_greater():
#     num = 100
#     assert num > 100
#
# def test_greater_equal():
#     num = 100
#     assert num >= 100
#
# def test_less():
#     num = 100
#     assert num < 200

# I create an autotest where I open https://duckduckgo.com/
# and enter the word "шахтар" into the search,
# then go to the third search result,
# open it and count the number of times the word "шахтар" appears on that page

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import pytest
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
# def test_duckduckgo_search(driver):
#     # Navigate to DuckDuckGo
#     driver.get("https://duckduckgo.com/")
#
#     # Find the search box and enter the query
#     search_box = driver.find_element_by_id("search_form_input_homepage")
#     search_box.send_keys("шахтар\n")
#
#     # Wait for the search results to load
#     driver.implicitly_wait(10)
#
#     # Find the third search result and click on it
#     search_results = driver.find_elements_by_css_selector(".result__url")
#     third_result = search_results[2]
#     third_result.click()
#
#     # Wait for the page to load
#     driver.implicitly_wait(10)
#
#     # Get the page source and count the number of occurrences of "шахтар"
#     page_source = driver.page_source
#     num_occurrences = page_source.count("шахтар")
#
#     # Assert that the word "шахтар" appears at least once on the page
#     assert num_occurrences >= 1




