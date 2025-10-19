from SeleniumLibrary import SeleniumLibrary
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
import time
import hashlib

from variables import (
    URL, NAME, COUNTRY, CITY,
    CREDIT_CARD, MONTH, YEAR
)

class CustomKeywords:

    def __init__(self):
        self.selib = SeleniumLibrary()

    def open_site(self, url):
        print(f"=== Открываю сайт: {url} ===")
        self.selib.open_browser(url, "chrome")
        self.selib.maximize_browser_window()
        print("=== Браузер открыт ===")

    def sign_up_to_demoblaze(self, username_prefix="user", password="test123"):
        unique_id = str(time.time()).encode('utf-8')
        username_hash = hashlib.sha1(unique_id).hexdigest()[:8]

        unique_username = f"{username_prefix}_{username_hash}"
        self.selib.click_element("id=signin2")
        time.sleep(1)
        self.selib.input_text("id=sign-username", unique_username)
        self.selib.input_text("id=sign-password", password)
        self.selib.click_button("xpath=//button[text()='Sign up']")
        time.sleep(1)

        try:
            alert = self.selib.driver.switch_to.alert
            print(f"Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("Пользователь успешно зарегистрирован (alert не появился)")

        return unique_username, password

    def login_to_demoblaze(self, username, password):
        self.selib.click_element("id=login2")
        time.sleep(1)
        self.selib.input_text("id=loginusername", username)
        self.selib.input_text("id=loginpassword", password)
        self.selib.click_button("xpath=//button[text()='Log in']")
        self.selib.wait_until_page_contains("Welcome", timeout=10)

    def verify_login_successful(self, username):
        self.selib.page_should_contain(f"Welcome {username}")
        print(f"Alert: {username}")

    def logout_from_demoblaze(self):
        time.sleep(1)
        self.selib.click_element("id=logout2")
        self.selib.wait_until_page_contains("Log in", timeout=10)
        print("Пользователь успешно вышел из аккаунта")

    def buy_product_from_demoblaze(self):
        self.selib.click_link("Cart")
        time.sleep(2)

        self.selib.click_button("xpath=//button[text()='Place Order']")
        time.sleep(1)

        self.selib.input_text("id=name", NAME)
        self.selib.input_text("id=country", COUNTRY)
        self.selib.input_text("id=city", CITY)
        self.selib.input_text("id=card", CREDIT_CARD)
        self.selib.input_text("id=month", MONTH)
        self.selib.input_text("id=year", YEAR)

        self.selib.click_button("xpath=//button[text()='Purchase']")
        time.sleep(2)

        self.selib.page_should_contain("Thank you for your purchase!")
        self.selib.click_button("xpath=//button[text()='OK']")

        print("Покупка успешно завершена!")

    def add_to_cart(self, product_name="Iphone 6 32gb"):
        self.selib.click_link(product_name)
        time.sleep(2)

        self.selib.click_element("xpath=//a[contains(text(), 'Add to cart')]")
        time.sleep(2)
        try:
            alert = self.selib.driver.switch_to.alert
            print(f"🛒 Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("Нет alert'а при добавлении товара")

        time.sleep(2)
        self.selib.click_link("Home")




    def close_browser(self):
        self.selib.close_browser()
