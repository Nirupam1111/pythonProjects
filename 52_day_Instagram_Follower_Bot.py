from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

CHROME_DRIVER_PATH = "C:/development/chromedriver.exe"
SIMILAR_ACCOUNT='usatoday'
INSTA_USERNAME = "foodtheraphy1111"
INSTA_PASSWORD = "asdf@1"


class InstaFollower:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        username=self.driver.find_element(By.NAME,'username')
        username.send_keys(INSTA_USERNAME)
        sleep(1)
        password=self.driver.find_element(By.NAME,'password')
        password.send_keys(INSTA_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(8)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(5)
        followers=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a/span')
        followers.click()
        sleep(2)
        pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))
        for i in range(10):
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/ html / body / div[7] / div / div / div / div[3] / button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
