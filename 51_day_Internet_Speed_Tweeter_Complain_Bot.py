from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 50
PROMISED_UP = 2
CHROME_DRIVER_PATH = "C:/development/chromedriver.exe"
TWITTER_EMAIL = "nirupamsur10@gmail.com"
TWITTER_USERNAME = 'NIRUPAMSUR1'
TWITTER_PASSWORD = "zxcvbnm@1"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        go = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        sleep(60)
        self.up = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                                                  'div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                    'div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(7)
        email = self.driver.find_element(By.NAME, 'text')
        email.click()
        sleep(2)
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(2)
        username = self.driver.find_element(By.NAME, 'text')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        create_tweet = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/'
                                                       'div[3]/a')
        create_tweet.click()
        sleep(3)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for{PROMISED_DOWN}down/{PROMISED_UP}up?"
        create_tweet.send_keys(tweet)
        sleep(3)
        post_tweet = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/'
                                                       'div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/'
                                                       'div[2]/div[3]/div/div/div[2]/div[4]')
        post_tweet.click()
        sleep(3)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
