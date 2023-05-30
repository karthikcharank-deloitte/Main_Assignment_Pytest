import time

import pytest

from TestData.TestDataFromExcel import TestDataFromExcel
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.ProfilePage import ProfilePage
from utilities.baseclass import BaseClass

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestProfileAndNotes(BaseClass):

    def test_login(self, get_login_data):
        log = self.getLogger()
        self.driver.get("https://practice.expandtesting.com/notes/app/login")
        login_page = LoginPage(self.driver)
        log.info("Log in using the same credentials")
        login_page.get_email().send_keys(get_login_data["email"])
        login_page.get_password().send_keys(get_login_data["password"])
        login_page.get_login_btn().click()
        time.sleep(3)
        log.info("Login Successful..!!")

    def test_update_profile(self, get_profile_data):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.get_profile().click()
        log.info("Clicked on Profile Icon")
        profile_page = ProfilePage(self.driver)
        profile_page.get_phone_number().clear()
        profile_page.get_phone_number().send_keys(get_profile_data["phone number"])
        log.info("Updated phone number is: " + get_profile_data["phone number"])
        profile_page.get_company_name().clear()
        profile_page.get_company_name().send_keys(get_profile_data["company name"])
        log.info("Updated company name is: " + get_profile_data["company name"])
        profile_page.get_update_profile().click()
        profile_updated_msg = profile_page.get_success_msg().text
        assert profile_updated_msg == "Profile updated successful"
        log.info("Profile updated successfully..!!")

    def test_update_password(self, get_profile_data):
        log = self.getLogger()
        profile_page = ProfilePage(self.driver)
        profile_page.get_change_password().click()
        log.info("Clicked on Change Password Icon")
        profile_page.get_current_password().send_keys(get_profile_data["current password"])
        log.info("Current Password is entered")
        profile_page.get_new_password().send_keys(get_profile_data["new password"])
        log.info("New Password is entered")
        profile_page.get_confirm_password().send_keys(get_profile_data["new password"])
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        log.info("Scrolled to the bottom of the webpage")
        self.driver.execute_script("arguments[0].click();", profile_page.get_update_password_btn())
        password_updated_msg = profile_page.get_success_msg().text
        assert password_updated_msg == "The password was successfully updated"
        log.info("Password updated successfully..!!")
        profile_page.get_my_notes().click()

    def test_create_notes(self, get_notes_data):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        time.sleep(1)
        home_page.get_add_note_btn().click()
        log.info("Clicked on Add Note button")
        self.selectOptionFromDropdown(home_page.get_category(), get_notes_data["category"])
        log.info("The Category of the note is selected as: " + get_notes_data["category"])
        home_page.get_title().send_keys(get_notes_data["title"])
        log.info("The Title of the note is: " + get_notes_data["title"])
        home_page.get_description().send_keys(get_notes_data["description"])
        log.info("The Description of the note is: " + get_notes_data["description"])
        home_page.get_create_btn().click()
        log.info("Note created successfully")

    def test_edit_notes(self,get_edited_notes):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.get_home_notes().click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(home_page.edit_btn_loc)))
        home_page.get_description().clear()
        home_page.get_description().send_keys(get_edited_notes["home note"])
        log.info("Home Note edited successfully..!!")
        home_page.get_save_btn().click()
        self.driver.find_element(By.XPATH, "//a[@data-testid='home']").send_keys(Keys.CONTROL + Keys.HOME)
        home_page.get_work_notes().click()
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(home_page.edit_btn_loc)))
        home_page.get_description().clear()
        home_page.get_description().send_keys(get_edited_notes["work note"])
        home_page.get_save_btn().click()
        log.info("Work Note edited successfully..!!")
        home_page.get_personal_notes().click()
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(home_page.edit_btn_loc)))
        home_page.get_description().clear()
        home_page.get_description().send_keys(get_edited_notes["personal note"])
        home_page.get_save_btn().click()
        log.info("Personal Note edited successfully..!!")
        home_page.get_all_notes().click()

    def test_mark_completed(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(home_page.mark_completed_loc)))
        log.info("Note 3 is marked as completed")
        time.sleep(2)
        completed_bg_colour = self.driver.find_element(By.XPATH, "//div[normalize-space()='Note 3']").value_of_css_property('background-color')
        assert completed_bg_colour == "rgba(40, 46, 41, 0.6)"
        log.info("Note 3 is verified as completed")

    def test_search_notes(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.get_search_box().send_keys("1234")
        log.info("Search key is entered as: 1234")
        search_msg = home_page.get_search_msg().text
        assert search_msg == "Couldn't find any notes"
        log.info("1234 is not present")
        log.info("Search message is verified")
        home_page.get_search_box().clear()
        home_page.get_search_box().send_keys("Note 1")
        log.info("Search key is entered as: Note 1")
        note_title = self.driver.find_element(By.XPATH, "//div[@class='card-header fw-bold text-truncate']").text
        assert note_title == "Note 1"
        log.info("Note 1 is present")

    def test_logout(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.get_logout_btn().click()
        log.info("Log out successful..!!")

    def test_delete_account(self, get_login_data):
        log = self.getLogger()
        self.driver.get("https://practice.expandtesting.com/notes/app/login")
        login_page = LoginPage(self.driver)
        log.info("Login with the same user")
        login_page.get_email().send_keys(get_login_data["email"])
        log.info("Email entered is: " + get_login_data["email"])
        login_page.get_password().send_keys(get_login_data["new password"])
        log.info("Password entered is: " + get_login_data["new password"])
        login_page.get_login_btn().click()
        log.info("Login successful..!!")
        time.sleep(3)
        home_page = HomePage(self.driver)
        home_page.get_profile().click()
        log.info("Clicked on Profile Icon")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        profile_page = ProfilePage(self.driver)
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(
                     EC.element_to_be_clickable(profile_page.delete_account_loc)))
        log.info("Clicked on Delete Account button")
        profile_page.get_delete_btn().click()
        log.info("Clicked on Delete button")
        log.info("Account deleted successfully..!!")

    @pytest.fixture(params=TestDataFromExcel.get_testData("Register & Login Data"))
    def get_login_data(self, request):
        return request.param

    @pytest.fixture(params=TestDataFromExcel.get_testData("Profile Data"))
    def get_profile_data(self, request):
        return request.param

    @pytest.fixture(params=TestDataFromExcel.get_testData("Notes Data"))
    def get_notes_data(self, request):
        return request.param

    @pytest.fixture(params=TestDataFromExcel.get_testData("Update Notes"))
    def get_edited_notes(self, request):
        return request.param

    @pytest.fixture(params=TestDataFromExcel.get_testData("Register & Login Data"))
    def get_login_data(self, request):
        return request.param
