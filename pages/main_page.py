from time import sleep

from locators.main_page_loc import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    main_page_loc = MainPageLocators


    def fill_email(self, email):
        el = self.wait.element_to_be_clickable(*self.main_page_loc.EMAIL_EDIT)
        el.clear()
        el.send_keys(email)


    def fill_name(self, name):
        el = self.wait.element_to_be_clickable(*self.main_page_loc.NAME_EDIT)
        el.clear()
        el.send_keys(name)


    def fill_time(self, time):
        el = self.wait.element_to_be_clickable(*self.main_page_loc.TIME_EDIT)
        el.clear()
        el.send_keys(time)


    def subscribe_user(self, email, name, time):
        self.fill_email(email)
        self.fill_name(name)
        self.fill_time(time)
        self.subscribe_btn_click()


    def subscribe_btn_click(self):
        el = self.wait.element_to_be_clickable(*self.main_page_loc.SUBSCRIBE_BTN)
        el.click()


    def refresh_btn_click(self):
        el = self.wait.element_to_be_clickable(*self.main_page_loc.REFRESH_BTN)
        el.click()


    def delete_btn_click(self):
        el = self.wait.element_to_be_clickable(*self.main_page_loc.DELETE_BTN)
        el.click()


    def get_row(self, row_number, delay=1):
        for attempt in range(0, delay):
            sleep(1)
            by, loc = self.main_page_loc.TABLE_ROW
            rows = self.driver.find_elements(by, f'{loc}[{row_number}]')
            if rows:
                return rows[0]
        return None


    def get_rows(self, delay=1):
        for attempt in range(0, delay):
            sleep(1)
            rows = self.driver.find_elements(*self.main_page_loc.TABLE_ROW)
            if rows:
                return rows
        return None


    def get_row_data(self, row_number):
        row = self.get_row(row_number)
        if row is None:
            return None
        return self._create_row_object(row)


    def get_rows_data(self):
        rows_list = []
        rows = self.get_rows()
        if rows is None:
            return None
        for row_num in range(0, len(rows)):
            row = rows[row_num]
            data = self._create_row_object(row)
            rows_list.append(data)
        return rows_list


    def _create_row_object(self, row):
        name = row.find_element(*self.main_page_loc.NAME_TABLE_ROW).text
        email = row.find_element(*self.main_page_loc.EMAIL_TABLE_ROW).text
        time = row.find_element(*self.main_page_loc.TIME_IMG).get_attribute('data-icon')
        time = True if time == 'check' else False
        return {
            'name': name,
            'email': email,
            'time': time
        }

