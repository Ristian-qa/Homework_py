from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    sleep(5)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    sleep(5)

    login_button = driver.find_element(By.CSS_SELECTOR,
                                       "button[type='submit']")
    login_button.click()

    success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")

    print(success_message.text)

finally:
    driver.quit()
