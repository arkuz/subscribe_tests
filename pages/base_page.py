from selenium import webdriver

from helpers.wait import Wait
from locators.base_page_loc import BasePageLocators


class BasePage(object):

    driver: webdriver
    driver = None

    base_page_loc = BasePageLocators()


    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(driver)

