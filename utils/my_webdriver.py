from random import random
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('--incognito')
        options.binary_location = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager(version='104.0.5112.20').install(), chrome_options=options)

    def get_url(self, url):
        try:
            self.driver.get(url)
        except TimeoutException:
            print("Couldn't load the requested url")
            self.driver.quit()

    def exit_browser(self):
        self.driver.quit()

    def search_with_toolbar(self, search_key):
        search_bar = self.driver.find_element(by=By.ID, value='twotabsearchtextbox')
        search_bar.clear()
        search_bar.send_keys(search_key)
        search_bar.send_keys(Keys.RETURN)

    def find_all_cards(self):
        cards = self.driver.find_elements_by_xpath('//div[@data-component-type="s-search-result"]')

        return cards

    @staticmethod
    def sleep_for_random_interval():
        time_in_seconds = random() * 2
        sleep(time_in_seconds)

