import time
import datetime

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Custom variables Constants are in constants.py
from constants import *

# Get today's date in "day", "month" and "year"
date = datetime.datetime.now()
day = date.day
month = date.month
year = date.year



class TestAutomation():

    @pytest.fixture(autouse=True)
    def launchBrowser(self):
        driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        yield
        driver.close()

    def test_Search_Flight(self):
        try:
            driver = self.driver
            driver.get(URL)

            radioButton = driver.find_element_by_id(RADIO_BUTTON_ID)
            radioButton.click()
            fromField = driver.find_element_by_id(FROM_INPUT_ID)
            fromField.send_keys(Keys.BACKSPACE)
            fromField.send_keys(FROM_CITY)
            toField = driver.find_element_by_id(TO_INPUT_ID)
            toField.send_keys(Keys.BACKSPACE)
            toField.send_keys(TO_CITY)
            departDateField = driver.find_element_by_id(DEPART_DATE_ID)
            departDateField.click()
            driver.find_element_by_link_text("%s" % day).click()
            returnDateField = driver.find_element_by_id(RETURN_DATE_ID)
            returnDateField.click()
            driver.find_element_by_link_text("%s" % (day + 1)).click()
            search_button = driver.find_element_by_id(SEARCH_BUTTON_ID)
            search_button.click()
            time.sleep(5)
            modal_dialog = driver.find_element_by_class_name(MODAL_DIALOG_CLASS)

            if modal_dialog:
                driver.find_element_by_link_text('Search Flight').click()
            # time.sleep(3)
            book_button_footer = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, BOOK_BUTTON_FOOTER_CSS)))
            book_button_footer.click()

            try:
                confirm_modal_dialog = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.ID, CONFIRM_MODAL_DIALOG_ID)))
                driver.find_element_by_link_text('Continue to Book').click()
            except:
                pass

        except Exception as e:
            print(e)
