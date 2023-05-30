from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    create_acc_loc = (By.XPATH, "//a[@class='btn btn-outline-secondary btn-lg px-4']")
    email_loc = (By.XPATH, "//input[@id='email']")
    name_loc = (By.XPATH, "//input[@id='name']")
    password_loc = (By.XPATH, "//input[@id='password']")
    confirm_password_loc = (By.XPATH, "//input[@id='confirmPassword']")
    register_loc = (By.XPATH, "//button[@type='submit']")
    success_msg_loc = (By.XPATH, "//div[@class='alert alert-success']")
    click_to_login_loc = (By.XPATH, "//a[text()='Click here to Log In']")

    def get_create_acc_btn(self):
        return self.driver.find_element(*RegistrationPage.create_acc_loc)

    def get_email(self):
        return self.driver.find_element(*RegistrationPage.email_loc)

    def get_name(self):
        return self.driver.find_element(*RegistrationPage.name_loc)

    def get_password(self):
        return self.driver.find_element(*RegistrationPage.password_loc)

    def get_confirm_password(self):
        return self.driver.find_element(*RegistrationPage.confirm_password_loc)

    def get_register_btn(self):
        return self.driver.find_element(*RegistrationPage.register_loc)

    def get_success_msg(self):
        return self.driver.find_element(*RegistrationPage.success_msg_loc)

    def get_click_to_login(self):
        return self.driver.find_element(*RegistrationPage.click_to_login_loc)
