from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Wait(object):

    driver: webdriver
    driver = None

    wait_const = 10


    def __init__(self, driver):
        self.driver = driver


    def presence_of_element_located(self, by, loc, implicitly_wait=wait_const):
        return WebDriverWait(self.driver, implicitly_wait).until(
            EC.presence_of_element_located((by, loc)))


    def element_to_be_clickable(self, by, loc, implicitly_wait=wait_const):
        return WebDriverWait(self.driver, implicitly_wait).until(
            EC.element_to_be_clickable((by, loc)))

