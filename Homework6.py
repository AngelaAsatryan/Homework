# Python code to demonstrate working of unittest
import unittest
import time
# import _json
from selenium import webdriver
driver = webdriver.Chrome()
#driver.implicitly_wait(10)

class web_page:
    def __init__(self, baseurl, search_area, submit_button):
        self.baseurl = baseurl
        self.search_area = search_area
        self.submit_button = submit_button

class search_element:
    def __init__(self, keyword, location, path, path_new):
        self.keyword = keyword
        self.location = location
        self.path = path
        self.path_new = path_new

#define my instance
search_element = search_element("LEGO", '0, 964.8', '//*[@id="search"]/div[1]/div[2]//span[4]/div[1]/div[3]//span//div[2]/div[2]//div[1]//div[1]/h2/a/span', '//*[@id="productTitle"]')
web_page = web_page('https://amazon.com', 'twotabsearchtextbox', '//*[@id="nav-search"]/form/div[2]/div/input')


class TestSearchFunctionality(unittest.TestCase):
    def setUp(self) -> None:
        # define search area and submit button
        driver.get(web_page.baseurl)
        driver.maximize_window()
        self.search_area = driver.find_element_by_id(web_page.search_area)
        self.submit_button = driver.find_elements_by_xpath(web_page.submit_button)[0]
        # type text
        self.search_area.send_keys(search_element.keyword)
        # search the text
        self.submit_button.click()
        #scroll the window to desired location
        driver.execute_script('window.scrollTo(0, 964.8)')
        self.search_results = driver.find_elements_by_xpath(search_element.path)[0]
        self.search_results.click()
        self.new_window = driver.find_elements_by_xpath(search_element.path_new)[0]
    def tearDown(self) -> None:
        driver.quit()
    def test_run(self):
        self.assertEqual(str(self.search_results), str(self.new_window))
if __name__ == '__main__':
    unittest.main()