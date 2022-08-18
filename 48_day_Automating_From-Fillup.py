from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:/development/chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')

name=driver.find_element(By.NAME,"fName")
name.send_keys("Nirupam")

last_name=driver.find_element(By.NAME,"lName")
last_name.send_keys("Sur")

email=driver.find_element(By.NAME,"email")
email.send_keys("nirupamsur10@gmail.com")

search=driver.find_element(By.CSS_SELECTOR,"button")
search.send_keys(Keys.ENTER)

