from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Cтраницa авторизации"""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        return self

    def enter_username(self, username):
        field = self.wait.until(EC.presence_of_element_located(
            self.USERNAME_INPUT))
        field.send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self


class InventoryPage:
    """Главная страница"""

    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        button = self.wait.until(EC.element_to_be_clickable(
            self.BACKPACK_BUTTON))
        button.click()
        return self

    def add_tshirt_to_cart(self):
        self.driver.find_element(*self.TSHIRT_BUTTON).click()
        return self

    def add_onesie_to_cart(self):
        self.driver.find_element(*self.ONESIE_BUTTON).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
        return self


class CartPage:
    """Корзина"""

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self


class CheckoutPage:
    """Оформление заказа"""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        return self

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        return self

    def fill_postal_code(self, postal_code):
        self.driver.find_element(*self.POSTAL_CODE_INPUT
                                 ).send_keys(postal_code)
        return self

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def get_total(self):
        total = self.wait.until(EC.presence_of_element_located(
            self.TOTAL_LABEL))
        return total.text
