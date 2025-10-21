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
   
3. Install Google Chrome and ChromeDriver (must match browser version).  
4. Ensure `variables.py` includes necessary constants (URL, login, password, product names, etc.).


## Test Cases

### 1. Login And Logout
1. Open browser and go to the site  
2. Click **Log In**  
3. Enter username and password  
4. Click **Log In** button  
5. Verify successful login  
6. Click **Log Out**  
7. Verify **Log In** button appears again  
8. Close browser  

---

### 2. Login Buy And Logout
1. Open browser and go to the site  
2. Log in with valid credentials  
3. Add multiple products to the cart  
4. Open cart and click **Place Order**  
5. Fill in order details  
6. Confirm purchase  
7. Verify success message  
8. Log out  
9. Close browser  

---

### 3. Sign Up New User And Login And Logout
1. Open browser and go to the site  
2. Click **Sign Up**  
3. Enter new username and password  
4. Submit and accept confirmation alert  
5. Log in with new credentials  
6. Verify successful login  
7. Log out  
8. Close browser  

---

### 4. Sign Up New User And Login And Buy And Logout
1. Open browser and go to the site  
2. Create a new user (Sign Up)  
3. Log in with new credentials  
4. Add product to cart  
5. Go to cart and click **Place Order**  
6. Fill in payment form  
7. Confirm purchase  
8. Verify success message  
9. Log out  
10. Close browser  

---

## Run Tests
```bash
robot test.robot
```
