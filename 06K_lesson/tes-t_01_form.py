from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").clear()
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажать кнопку Submit
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Ожидаем появления подсветки полей
    wait = WebDriverWait(driver, 10)

    # Проверка: поле Zip code подсвечено красным
    zip_code_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "#zip-code.alert-danger"))
    )
    assert zip_code_element is not None, "Zip code не подсвечен красным"
    print("Zip code подсвечен красным")

    # Список полей для проверки зеленой подсветки
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
        field_element = driver.find_element(
            By.CSS_SELECTOR, f"#{field_id}.alert-success"
        )
        assert field_element is not None, (
            f"Поле {field_id} не подсвечено зеленым")
        print(f"Поле {field_id} подсвечено зеленым")

    print("Проверки пройдены успешно!")

    driver.quit()


if __name__ == "__main__":
    test_form_validation()
