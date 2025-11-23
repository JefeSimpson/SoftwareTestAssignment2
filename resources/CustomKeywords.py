from SeleniumLibrary import SeleniumLibrary
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
import time
import hashlib

from variables import (
    baseUrl,
    orderName, orderCountry, orderCity,
    orderCard, orderMonth, orderYear,
    usernamePrefix, usernamePassword
)

from locators import (
    signUpButton, signUpUsername, signUpPassword, signUpFormButton, categoriesCheck,
    loginButton, loginUsernameField, loginPasswordField, loginFormButton, logoutButton,
    cartButton, homeButton, addToCartButton, placeOrderButton, orderNameField, orderCountryField,
    orderCityField, orderCardField, orderMonthField, orderYearField, purchaseFormButton, purchaseOkButton
)

class CustomKeywords:

    def __init__(self):
        self.selib = SeleniumLibrary()


    def open_site(self, browser):
        print(f"=== Открываю сайт: {baseUrl} ===")
        self.selib.open_browser(baseUrl, browser)
        self.selib.wait_until_page_contains(homeButton, timeout=30)
        self.selib.maximize_browser_window()
        print("=== Браузер открыт ===")
        time.sleep(1)


    def sign_up_to_site(self):
        unique_id = str(time.time()).encode('utf-8')
        username_hash = hashlib.sha1(unique_id).hexdigest()[:8]

        unique_username = f"{usernamePrefix}_{username_hash}"
        self.selib.click_element(signUpButton)
        time.sleep(1)
        self.selib.input_text(signUpUsername, unique_username)
        self.selib.input_text(signUpPassword, usernamePassword)
        self.selib.click_button(signUpFormButton)
        time.sleep(1)

        try:
            alert = self.selib.driver.switch_to.alert
            print(f"Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("Пользователь успешно зарегистрирован (alert не появился)")

        return unique_username, usernamePassword


    def login_to_site(self, username, password):
        self.selib.click_element(loginButton)
        time.sleep(1)
        self.selib.input_text(loginUsernameField, username)
        self.selib.input_text(loginPasswordField, password)
        self.selib.click_button(loginFormButton)
        self.selib.wait_until_page_contains("Welcome", timeout=30)


    def logout_from_site(self):
        time.sleep(1)
        self.selib.click_element(logoutButton)
        self.selib.wait_until_page_contains_element(loginButton, timeout=30)
        print("Пользователь успешно вышел из аккаунта")


    def buy_product_from_site(self):
        self.selib.click_link(cartButton)
        time.sleep(2)

        self.selib.click_button(placeOrderButton)
        time.sleep(1)

        self.selib.input_text(orderNameField, orderName)
        self.selib.input_text(orderCountryField, orderCountry)
        self.selib.input_text(orderCityField, orderCity)
        self.selib.input_text(orderCardField, orderCard)
        self.selib.input_text(orderMonthField, orderMonth)
        self.selib.input_text(orderYearField, orderYear)

        self.selib.click_button(purchaseFormButton)
        time.sleep(2)

        self.selib.page_should_contain("Thank you for your purchase!")
        self.selib.click_button(purchaseOkButton)

        print("Покупка успешно завершена!")


    def add_to_cart(self, product_name="Iphone 6 32gb"):
        self.selib.click_link(product_name)
        self.selib.wait_until_page_contains_element(addToCartButton, timeout=30)

        self.selib.click_element(addToCartButton)
        time.sleep(2)

        try:
            alert = self.selib.driver.switch_to.alert
            print(f"🛒 Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("Нет alert'а при добавлении товара")

        time.sleep(1)
        self.selib.click_link(homeButton)
        self.selib.wait_until_page_contains_element(categoriesCheck, timeout=30)
        time.sleep(1)


    def close_browser(self):
        self.selib.close_browser()
