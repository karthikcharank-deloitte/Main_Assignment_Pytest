from selenium.webdriver.common.by import By


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver

    phone_number_loc = (By.XPATH, "//input[@name='phone']")
    company_name_loc = (By.XPATH, "//input[@name='company']")
    update_profile_loc = (By.XPATH, "//button[@class='btn btn-outline-primary']")
    success_msg_loc = (By.XPATH, "//div[@class='toast-body']")
    change_password_loc = (By.XPATH, "//button[normalize-space()='Change password']")
    current_password_loc = (By.XPATH, "//input[@name='currentPassword']")
    new_password_loc = (By.XPATH, "//input[@name='newPassword']")
    confirm_password_loc = (By.XPATH, "//input[@name='confirmPassword']")
    update_password_btn_loc = (By.XPATH, "//button[@class='btn btn-outline-primary']")
    my_notes_loc = (By.XPATH, "//a[@class='navbar-brand mb-2 mb-sm-0 logo_title']")
    delete_account_loc = (By.XPATH, "//button[@class='mt-2 btn btn-danger']")
    delete_btn_loc = (By.XPATH, "//button[normalize-space()='Delete']")

    def get_phone_number(self):
        return self.driver.find_element(*ProfilePage.phone_number_loc)

    def get_company_name(self):
        return self.driver.find_element(*ProfilePage.company_name_loc)

    def get_update_profile(self):
        return self.driver.find_element(*ProfilePage.update_profile_loc)

    def get_success_msg(self):
        return self.driver.find_element(*ProfilePage.success_msg_loc)

    def get_change_password(self):
        return self.driver.find_element(*ProfilePage.change_password_loc)

    def get_current_password(self):
        return self.driver.find_element(*ProfilePage.current_password_loc)

    def get_new_password(self):
        return self.driver.find_element(*ProfilePage.new_password_loc)

    def get_confirm_password(self):
        return self.driver.find_element(*ProfilePage.confirm_password_loc)

    def get_update_password_btn(self):
        return self.driver.find_element(*ProfilePage.update_password_btn_loc)

    def get_my_notes(self):
        return self.driver.find_element(*ProfilePage.my_notes_loc)

    def get_delete_account(self):
        return self.driver.find_element(*ProfilePage.delete_account_loc)

    def get_delete_btn(self):
        return self.driver.find_element(*ProfilePage.delete_btn_loc)

