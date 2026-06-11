from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_checkout_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)


# 1. Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # 2. Авторизация
    username = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # 3. Добавление товаров в корзину
    wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "add-to-cart-sauce-labs-backpack"))
        ).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейти в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажать Checkout
    driver.find_element(By.ID, "checkout").click()

    # 6. Заполнить форму данными
    driver.find_element(By.ID, "first-name").send_keys("Кристина")
    driver.find_element(By.ID, "last-name").send_keys("Живноводенко")
    driver.find_element(By.ID, "postal-code").send_keys("453100")

    # 7. Нажать Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Прочитать итоговую стоимость
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        ".summary_total_label"))
        )
    total_text = total_element.text
    print(f"Итоговая стоимость: {total_text}")

    # 9. Проверка суммы
    expected_total = "Total: $58.29"
    assert total_text == expected_total, (
            f"Ожидалось '{expected_total}', получено '{total_text}'"
        )

    print("Тест пройден: итоговая сумма верна")

    driver.quit()


if __name__ == "__main__":
    test_shop_checkout_total()
