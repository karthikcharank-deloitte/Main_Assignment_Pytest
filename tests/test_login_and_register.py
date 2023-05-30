import time

import pytest

from TestData.TestDataFromExcel import TestDataFromExcel
from pageObjects.LoginPage import LoginPage
from pageObjects.RegistrationPage import RegistrationPage
from utilities.baseclass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegisterAndLogin(BaseClass):

    def test_create_account(self, get_login_data):
        log = self.getLogger()
        self.driver.get("https://practice.expandtesting.com/notes/app")
        log.info("Application loaded successfully..!!")
        registration_page = RegistrationPage(self.driver)
        registration_page.get_create_acc_btn().click()
        registration_page.get_email().send_keys(get_login_data["email"])
        log.info("E-mail entered is: "+get_login_data["email"])
        registration_page.get_name().send_keys(get_login_data["name"])
        log.info("Name entered is: " + get_login_data["name"])
        registration_page.get_password().send_keys(get_login_data["password"])
        log.info("Password entered is: " + get_login_data["password"])
        registration_page.get_confirm_password().send_keys(get_login_data["password"])
        registration_page.get_register_btn().click()
        registration_success_msg = registration_page.get_success_msg().text
        assert "User account created successfully" in registration_success_msg
        log.info("Account Created successfully..!!")
        login = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(registration_page.click_to_login_loc))
        login.click()

    def test_login(self, get_login_data):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        login_page.get_email().send_keys(get_login_data["email"])
        log.info("E-mail entered is: " + get_login_data["email"])
        login_page.get_password().send_keys(get_login_data["password"])
        log.info("Password entered is: " + get_login_data["password"])
        login_page.get_login_btn().click()
        time.sleep(3)
        log.info("Login successful..!!")

    @pytest.fixture(params=TestDataFromExcel.get_testData("Register & Login Data"))
    def get_login_data(self, request):
        return request.param
