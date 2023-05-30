from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    profile_loc = (By.XPATH, "//a[@class='btn btn-outline-primary me-2 mb-2 mb-sm-0']")
    search_box_loc = (By.XPATH, "//input[@id='search-note-input']")
    all_notes_loc = (By.XPATH, "//button[normalize-space()='All']")
    home_notes_loc = (By.XPATH, "//span[normalize-space()='Home']")
    work_notes_loc = (By.XPATH, "//span[normalize-space()='Work']")
    personal_notes_loc = (By.XPATH, "//span[normalize-space()='Personal']")
    add_note_btn_loc = (By.XPATH, "//button[normalize-space()='Add Note']")
    category_loc = (By.XPATH, "//select[@id='category']")
    title_loc = (By.XPATH, "//input[@id='title']")
    description_loc = (By.XPATH, "//textarea[@id='description']")
    create_btn_loc = (By.XPATH, "//button[@type='submit']")
    mark_completed_loc = (By.XPATH, "(//input[contains(@class,'form-check-input')])[1]")
    edit_btn_loc = (By.XPATH, "//div[@class='row']//div[1]//div[1]//div[4]//div[1]//button[1]")
    save_btn_loc = (By.XPATH, "//button[@type='submit']")
    search_msg_loc = (By.XPATH, "//h4[@class='my-2 mb-4']")
    logout_loc = (By.XPATH, "//button[normalize-space()='Logout']")

    def get_profile(self):
        return self.driver.find_element(*HomePage.profile_loc)

    def get_search_box(self):
        return self.driver.find_element(*HomePage.search_box_loc)

    def get_all_notes(self):
        return self.driver.find_element(*HomePage.all_notes_loc)

    def get_home_notes(self):
        return self.driver.find_element(*HomePage.home_notes_loc)

    def get_work_notes(self):
        return self.driver.find_element(*HomePage.work_notes_loc)

    def get_personal_notes(self):
        return self.driver.find_element(*HomePage.personal_notes_loc)

    def get_add_note_btn(self):
        return self.driver.find_element(*HomePage.add_note_btn_loc)

    def get_category(self):
        return self.driver.find_element(*HomePage.category_loc)

    def get_title(self):
        return self.driver.find_element(*HomePage.title_loc)

    def get_description(self):
        return self.driver.find_element(*HomePage.description_loc)

    def get_create_btn(self):
        return self.driver.find_element(*HomePage.create_btn_loc)

    def get_mark_competed(self):
        return self.driver.find_element(*HomePage.mark_completed_loc)

    def get_edit_btn(self):
        return self.driver.find_element(*HomePage.edit_btn_loc)

    def get_save_btn(self):
        return self.driver.find_element(*HomePage.save_btn_loc)

    def get_search_msg(self):
        return self.driver.find_element(*HomePage.search_msg_loc)

    def get_logout_btn(self):
        return self.driver.find_element(*HomePage.logout_loc)