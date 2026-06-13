from selenium import webdriver
from shop_profile_page import LoginPage, InventoryPage, CartPage, CheckoutPage


def test_shop_checkout_total():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page.add_backpack_to_cart()
    inventory_page.add_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_first_name("Кристина")
    checkout_page.fill_last_name("Живноводенко")
    checkout_page.fill_postal_code("453100")
    checkout_page.click_continue()

    total_text = checkout_page.get_total()
    print(f"Итоговая стоимость: {total_text}")

    expected_total = "Total: $58.29"
    assert total_text == expected_total, (
            f"Ожидалось '{expected_total}', получено '{total_text}'"
        )

    print("Тест пройден: итоговая сумма верна")
    driver.quit()


if __name__ == "__main__":
    test_shop_checkout_total()
