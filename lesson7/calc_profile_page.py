from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        """Открыть страницу калькулятора"""
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )
        self.driver.get(url)
        self.driver.maximize_window()
        return self

    def set_delay(self, seconds):
        """Установить задержку в поле ввода"""
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(seconds)
        return self

    def click_button_7(self):
        """Нажать кнопку 7"""
        self.driver.find_element(*self.BUTTON_7).click()
        return self

    def click_button_8(self):
        """Нажать кнопку 8"""
        self.driver.find_element(*self.BUTTON_8).click()
        return self

    def click_button_plus(self):
        """Нажать кнопку +"""
        self.driver.find_element(*self.BUTTON_PLUS).click()
        return self

    def click_button_equals(self):
        """Нажать кнопку ="""
        self.driver.find_element(*self.BUTTON_EQUALS).click()
        return self

    def get_result(self):
        """Получить текст результата"""
        return self.driver.find_element(*self.SCREEN).text

    def wait_for_result(self, expected_result):
        """Ожидать появления ожидаемого результата"""
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )
        return self
