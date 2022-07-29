from selenium.common import exceptions
from selenium.webdriver.common.by import By


def extract_card_data(card, barcode):
    """
    Extracting data, which includes product description, price, rating, review count and product link.

    """
    sponsored = card.find_element(by=By.CLASS_NAME, value="a-color-base").text.strip()
    if sponsored == 'Sponsored':
        return
    barcode = barcode
    description = card.find_element_by_xpath('.//h2/a').text.strip()
    if "protector" in description.lower():
        return
    url = card.find_element_by_xpath('.//h2/a').get_attribute('href')
    try:
        price_whole = card.find_element_by_xpath('.//span[@class="a-price-whole"]').text
        price_fraction = card.find_element_by_xpath('.//span[@class="a-price-fraction"]').text
        price = f'{price_whole}.{price_fraction}'
    except exceptions.NoSuchElementException:
        return
    return description, barcode, price, url
