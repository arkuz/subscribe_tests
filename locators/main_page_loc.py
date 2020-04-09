from selenium.webdriver.common.by import By


class MainPageLocators(object):

    EMAIL_EDIT = (By.XPATH, "//input[contains(@data-test,'new-subs-email')]")
    NAME_EDIT= (By.XPATH, "//input[contains(@data-test,'new-subs-name')]")
    TIME_EDIT = (By.XPATH, "//input[contains(@data-test,'new-subs-time')]")


    SUBSCRIBE_BTN = (By.XPATH, "//button[contains(@data-test,'new-subs-submit')]")
    REFRESH_BTN = (By.XPATH, "//button[contains(@data-test,'sync-button')]")
    DELETE_BTN = (By.XPATH, "//button[contains(@data-test,'clear-button')]")


    TABLE_ROW = (By.XPATH, "//tr[contains(@data-test,'subs-table-row')]")
    NAME_TABLE_ROW = (By.XPATH, ".//th[contains(@data-test,'subs-table-name')]")
    EMAIL_TABLE_ROW = (By.XPATH, ".//td[contains(@data-test,'subs-table-email')]")
    TIME_TABLE_ROW = (By.XPATH, ".//td[contains(@data-test,'subs-table-sub')]")
    TIME_IMG = (By.XPATH, ".//*[name()='svg']")
    TIME_IMG_OK = (By.XPATH, ".//*[name()='svg' and contains(@data-icon, 'check')]")
    TIME_IMG_BAD = (By.XPATH, ".//*[name()='svg' and contains(@data-icon, 'time')]")

