from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

# Открыть страницу
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()

# 1. Ввести значение 45 в поле задержки (локатор #delay)
delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
delay_input.clear()
delay_input.send_keys("45")

# 2. Нажать кнопки: 7, +, 8, =
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

# 3. Ожидать появления результата "15" в поле вывода (локатор .screen)
#    Таймаут = 50 секунд (45 задержка + небольшой запас)
result_element = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

# 4. Проверка: результат действительно равен 15
result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
assert result_text == "15", f"Ожидалось 15, получено {result_text}"

print("Результат 15 отобразился корректно через 45 секунд")


driver.quit()
