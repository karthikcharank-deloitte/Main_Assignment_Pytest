from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_loc = (By.XPATH, "//input[@id='email']")
    password_loc = (By.XPATH, "//input[@id='password']")
    login_btn_loc = (By.XPATH, "//button[@type='submit']")

    def get_email(self):
        return self.driver.find_element(*LoginPage.email_loc)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password_loc)

    def get_login_btn(self):
        return self.driver.find_element(*LoginPage.login_btn_loc)

