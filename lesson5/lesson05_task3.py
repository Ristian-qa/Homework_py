from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("12345")

    sleep(5)

    input_field.clear()

    input_field.send_keys("54321")

    sleep(5)

    print("Успешно!")

finally:
    driver.quit()
