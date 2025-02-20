from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.menu1 = (By.XPATH,"//span[contains(text(),'Text Box')]")
        self.menu2 = (By.XPATH, "//span[contains(text(),'Check Box')]")
        self.menu3 = (By.XPATH, "//span[contains(text(),'Radio Button')]")
        self.menu4 = (By.XPATH, "//span[contains(text(),'Web Tables')]")
        self.menu5 = (By.XPATH, "//span[contains(text(),'Buttons')]")
        self.menu6 = (By.XPATH, "//span[contains(text(),'Links')]")
        self.menu7 = (By.XPATH, "//span[contains(text(),'Images')]")
        self.menu8 = (By.XPATH, "//span[contains(text(),'Download')]")
        self.menu8 = (By.XPATH, "//span[contains(text(),'Dynamic')]")

    def open_google(self):
        #self.driver.get("https://www.google.com")
        self.driver.get("https://demoqa.com/text-box")

    def search(self, query):
       # search_input = self.driver.find_element(*self.search_box)
      #  search_input.send_keys(query + Keys.RETURN)
        text_box = self.driver.find_element(*self.menu1)
        text_box.click()

        text_box = self.driver.find_element(*self.menu2)
        text_box.click()

