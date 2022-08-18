from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path="C:/development/chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=software%20developer&location=India&sortBy=R')

time.sleep(3)
signin=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')
signin.click()

time.sleep(5)

email=driver.find_element(By.ID,"username")
email.send_keys("nirupamsur10@gmail.com")

password=driver.find_element(By.ID,"password")
password.send_keys("zxcvbnm@1")
password.send_keys(Keys.ENTER)

time.sleep(7)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container__link")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        job_apply=driver.find_element(By.CSS_SELECTOR,".jobs-apply-button--top-card button")
        job_apply.click()

        time.sleep(5)

        phone_number=driver.find_element(By.CSS_SELECTOR,'.display-flex input')
        if phone_number.text=="":
            phone_number.send_keys("8116852880")

        submit=driver.find_element(By.CSS_SELECTOR,'.display-flex button')
        if submit.get_attribute("data-control-name") == "continue_unify":
                    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
                    close_button.click()
                    time.sleep(2)
                    discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
                    discard_button.click()
                    print("Complex application, skipped.")
                    continue
        else:
            submit.click()
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
