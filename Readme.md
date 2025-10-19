# Automated UI Tests for Demoblaze

## Test Objective
This repository contains automated UI test cases for the [Demoblaze](https://www.demoblaze.com/) e-commerce website. The main goal is to validate the following user flows:

- User registration
- Login and logout functionality
- Adding products to the cart
- Purchasing products

Tests are implemented using **Robot Framework** with custom Python-based keywords built on **SeleniumLibrary**.

---

## Preconditions

Before executing any tests, ensure the following setup is complete:

1. **Python 3.7+** is installed.
2. **Robot Framework** is installed:
   ```bash
   pip install robotframework
   pip install robotframework-selenium2library  
   ```
   
3. Google Chrome is installed with the matching version of **ChromeDriver** in your system **PATH**.
4. Custom keywords from **CustomKeywords.py** are available and imported properly.
6. A variables.py file is configured with the following constants:
- URL – base URL of the Demoblaze site
- NAME, COUNTRY, CITY, CREDIT_CARD, MONTH, YEAR – customer info for checkout
- PRODUCT_ONE, PRODUCT_THREE – product names for testing


# Test Case Descriptions
## 1. Login And Logout

Goal: Verify successful login and logout of an existing user.

Steps:
1. Open the Demoblaze website.
2. Click "Log in".
3. Enter USERNAME and PASSWORD.
4. Submit login.
5. Verify the text Welcome USERNAME is displayed.
6. Wait for 2 seconds.
7. Wait another 3 seconds.
8. Click "Log out".
9. Verify the "Log in" button is visible again.
10. Wait for 0.5 seconds.
11. Close the browser.

## 2. Login Buy And Logout

Goal: Login as an existing user, add products to cart, complete a purchase, and log out.

Steps:
1. Open the Demoblaze website.
2. Login using USERNAME and PASSWORD.
3. Confirm successful login (Welcome USERNAME).
4. Wait 2 seconds.
5. Add product PRODUCT_ONE to the cart.
6. Wait 2 seconds.
7. Add default product (e.g., Iphone 6 32gb) to the cart.
8. Wait 2 seconds.
9. Add product PRODUCT_THREE to the cart.
10. Wait 2 seconds.
11. Go to cart and click "Place Order".
12. Fill in the purchase form (name, country, city, card, etc.).
13. Confirm the purchase.
14. Verify Thank you for your purchase! message appears and click "OK".
15. Wait 3 seconds.
16. Log out.
17. Wait 0.5 seconds.
18. Close the browser.

## 3. Sign Up New User And Login And Logout

Goal: Verify that a new user can register, log in, and log out successfully.

Steps:
1. Open the Demoblaze website.
2. Generate a unique username with prefix user and password test123.
3. Click "Sign up", enter credentials, and submit.
4. Accept the registration confirmation alert.
5. Wait 3 seconds.
6. Log in with the new credentials.
7. Confirm login with Welcome ${USERNAME}.
8. Wait 2 seconds.
9. Log out.
10. Wait 0.5 seconds.
11. Close the browser.

## 4. Sign Up New User And Login And Buy And Logout

Goal: End-to-end test: user registration, login, adding a product, completing a purchase, and logging out.

Steps:
1. Open the Demoblaze website.
2. Register a new user with user_xxxxxxxx and password test123.
3. Submit the registration and accept the confirmation alert.
4. Wait 3 seconds.
5. Login with new user credentials.
6. Confirm login with Welcome ${USERNAME}.
7. Wait 2 seconds.
8. Add a product to the cart (default: Iphone 6 32gb).
9. Wait 2 seconds.
10. Open cart and click "Place Order".
11. Fill out the purchase form and click "Purchase".
12. Verify the success message and click "OK".
13. Wait 3 seconds.
14. Log out.
15. Wait 0.5 seconds.
16. Close the browser.