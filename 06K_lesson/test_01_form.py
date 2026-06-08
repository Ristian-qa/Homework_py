from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.maximize_window()

# Заполнение формы
# First name
first_name = driver.find_element(By.NAME, "first-name")
first_name.send_keys("Иван")

# Last name
last_name = driver.find_element(By.NAME, "last-name")
last_name.send_keys("Петров")

# Address
address = driver.find_element(By.NAME, "address")
address.send_keys("Ленина, 55-3")

# Email
email = driver.find_element(By.NAME, "e-mail")
email.send_keys("test@skypro.com")

# Phone number
phone = driver.find_element(By.NAME, "phone")
phone.send_keys("+7985899998787")

# Zip code (оставляем пустым)
zip_code = driver.find_element(By.NAME, "zip-code")
zip_code.clear()  # Очищаем поле на всякий случай

# City
city = driver.find_element(By.NAME, "city")
city.send_keys("Москва")

# Country
country = driver.find_element(By.NAME, "country")
country.send_keys("Россия")

# Job position
job_position = driver.find_element(By.NAME, "job-position")
job_position.send_keys("QA")

# Company
company = driver.find_element(By.NAME, "company")
company.send_keys("SkyPro")

# Нажать кнопку Submit
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

# Ожидаем появления подсветки полей
wait = WebDriverWait(driver, 10)

# Проверка: поле Zip code подсвечено красным (класс alert-danger)
zip_code_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "#zip-code.alert-danger"))
    )
assert zip_code_element is not None, "Zip code не подсвечен красным"
print("Zip code подсвечен красным")

# Список полей, которые должны быть подсвечены зеленым (класс alert-success)
fields_to_check = [
    "first-name",
    "last-name",
    "address",
    "e-mail",
    "phone",
    "city",
    "country",
    "job-position",
    "company"
    ]

# Проверка каждого поля на зелёную подсветку
for field_id in fields_to_check:
    field_element = driver.find_element(By.CSS_SELECTOR,
                                        f"#{field_id}.alert-success")
    assert field_element is not None, f"Поле {field_id} не подсвечено зеленым"
    print(f"Поле {field_id} подсвечено зеленым")
print(f"Поле {field_id} подсвечено зеленым")

print("Проверки пройдены успешно!")


driver.quit()
