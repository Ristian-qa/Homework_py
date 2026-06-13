from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_profile_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    # Создаём объект страницы
    calculator = CalculatorPage(driver)

    # Выполняем действия
    calculator.open()
    calculator.set_delay("45")
    calculator.click_button_7()
    calculator.click_button_plus()
    calculator.click_button_8()
    calculator.click_button_equals()
    calculator.wait_for_result("15")

    # Проверка
    result = calculator.get_result()
    assert result == "15", f"Ожидалось 15, получено {result}"

    print("Результат 15 отобразился корректно через 45 секунд")
    driver.quit()


if __name__ == "__main__":
    test_calculator()
