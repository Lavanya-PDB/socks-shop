import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from faker import Faker

def generate_random_string(length=8):
    """Generate a random string of the given length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def open_web_page(driver):
    driver.get("http://localhost/index.html")
    print("Sock shop website opened")

def open_login_page(driver):
    Login_text_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/ul/li[1]/a")
    Login_text_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div")))

def login(driver, username, password):
    try:
        open_login_page(driver)
        time.sleep(3)
        username_input = driver.find_element(By.ID, "username-modal")
        password_input = driver.find_element(By.ID, "password-modal")
        username_input.send_keys(username)
        password_input.send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/p/button")))
        login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/p/button")
        login_button.click()
        print(f"Login successful! Username: {username}, Password: {password}")
    except Exception as e:
        print(f"An error occurred during login: {str(e)}")

def open_registration_page(driver):
    Register_text_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/ul/li[2]/a")
    Register_text_button.click()

def register(driver):
    try:
        open_registration_page(driver)
        time.sleep(3)
        fake = Faker()
        username = fake.user_name()
        firstname = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        password = fake.password()
        username_input = driver.find_element(By.ID, "register-username-modal")
        firstname_input = driver.find_element(By.ID, "register-first-modal")
        lastname_input = driver.find_element(By.ID, "register-last-modal")
        email_input = driver.find_element(By.ID, "register-email-modal")
        password_input = driver.find_element(By.ID, "register-password-modal")
        username_input.send_keys(username)
        firstname_input.send_keys(firstname)
        lastname_input.send_keys(lastname)
        email_input.send_keys(email)
        password_input.send_keys(password)
        register_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/form/p/button")
        register_button.click()
        time.sleep(2)
        print(f"Registration successful! Username: {username}, Email: {email}, Password: {password}")
        return username, password
    except Exception as e:
        print(f"An error occurred during registration: {str(e)}")
        return None, None

def fill_details_and_submit(driver, is_payment=False):
    try:
        time.sleep(1)
        if is_payment:
            Register_text_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/p/a")
        else:
            Register_text_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[1]/div/div[1]/p/a")
        Register_text_button.click()
        time.sleep(1)
        House_Number = ''.join(random.choices(string.digits, k=4))
        Street_Name = generate_random_string()
        City = generate_random_string()
        Postal_Code = ''.join(random.choices(string.digits, k=4))
        Country = generate_random_string()
        House_Number_input = driver.find_element(By.ID, "form-number")
        Street_Name_input = driver.find_element(By.ID, "form-street")
        City_input = driver.find_element(By.ID, "form-city")
        Postal_Code_input = driver.find_element(By.ID, "form-post-code")
        Country_input = driver.find_element(By.ID, "form-country")
        House_Number_input.send_keys(House_Number)
        Street_Name_input.send_keys(Street_Name)
        City_input.send_keys(City)
        Postal_Code_input.send_keys(Postal_Code)
        Country_input.send_keys(Country)
        submit_button_xpath = "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/div/div/div[2]/form/p/button"
        if is_payment:
            submit_button_xpath = "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/div/div/div[2]/p/button"
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, submit_button_xpath))
        )
        submit_button.click()
        print("Details submitted successfully.")
        time.sleep(2)
        return House_Number, Street_Name, City, Postal_Code, Country
    except Exception as e:
        print(f"An error occurred while filling details: {str(e)}")

def check_updated_details(driver, is_payment=False, house=None, street=None, city=None, postal=None, country=None):
    try:
        time.sleep(1)
        if is_payment:
            Shipping_text = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[2]/div/p").text
        else:
            Shipping_text = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[1]").text
        if house in Shipping_text and street in Shipping_text and city in Shipping_text and postal in Shipping_text and country in Shipping_text:
            print("Details are updated successfully.")
        else:
            print("Address details are not updated correctly")
    except Exception as e:
        print(f"An error occurred while checking updated details: {str(e)}")

def fill_details_and_submit_Payment(driver):
    try:
        time.sleep(1)
        Register_text_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/p/a")
        Register_text_button.click()
        time.sleep(1)
        Card_Number = ''.join(random.choices(string.digits, k=12))
        Expires = ''.join(random.choices(string.digits, k=4))
        Ccv = ''.join(random.choices(string.digits, k=3))
        Card_Number_input = driver.find_element(By.ID, "form-card-number")
        Expires_input = driver.find_element(By.ID, "form-expires")
        Ccv_input = driver.find_element(By.ID, "form-ccv")
        Card_Number_input.send_keys(Card_Number)
        Expires_input.send_keys(Expires)
        Ccv_input.send_keys(Ccv)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/div/div/div[2]/p/button"))
        )
        submit_button.click()
        print("Payment Details submitted successfully.")
        time.sleep(2)
        return Card_Number, Expires, Ccv
    except Exception as e:
        print(f"An error occurred while filling payment details: {str(e)}")

def check_updated_details_Payment(driver, card=None, expires=None, ccv=None):
    try:
        time.sleep(1)
        Shipping_text = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/div[2]/div[2]/div/p").text
        if card in Shipping_text and expires in Shipping_text and ccv in Shipping_text:
            print("Payment Details are updated successfully.")
        else:
            print("Payment Details are not updated correctly")
    except Exception as e:
        print(f"An error occurred while checking updated payment details: {str(e)}")

def add_item_to_cart(driver):
    try:
        time.sleep(1)
        driver.get("http://localhost/index.html")
        mapping = {1: "Holy", 2: "Colourful", 3: "SuperSport XL"}
        random_number = random.randint(1, 3)
        print("Random number", random_number)
        xpath = f"/html/body/div[3]/div[1]/div[3]/div[2]/div/div[1]/div/div[{random_number}]/div/div/div[1]/div/div[1]/a/img"
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        print(f"{mapping[random_number]} Added to cart")
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "buttonCart"))
        )
        add_to_cart_button.click()
        #print(f"Clicked on the element with XPath: {xpath}")
        time.sleep(1)
        return mapping[random_number]
    except Exception as e:
        print(f"An error occurred while adding to the cart: {str(e)}")

def check_cart_page(driver, expected_item):
    try:
        time.sleep(1)
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/a"))
        )
        cart_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/a"))
        )
        cart_page_text = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div").text
        if expected_item in cart_page_text:
            print(f"Added product '{expected_item}' found in the cart")
        else:
            print(f"Added product '{expected_item}' not found in the cart")
        time.sleep(1)
    except Exception as e:
        print(f"An error occurred while checking the cart page: {str(e)}")

def is_user_logged_in(driver):
    try:
        # Locate the element using XPath
        user_info_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/ul/li[1]/a")

        # Extract the text content of the element
        user_info_text = user_info_element.text

        # Check if the text contains "logged in as"
        return "Logged in as" in user_info_text.lower()  # Case-insensitive check

    except Exception as e:
        return False

def close_login_modal(driver):
    try:
        # Check if the login modal is present
        login_modal = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div")
        if login_modal.is_displayed():
            # Close the login modal
            close_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/button")
            close_button.click()
    except Exception as e:
        pass  # If the login modal is not present, ignore the exception

def navigate_to_page(driver, menu_item, index):
    try:
        # Close the login modal before navigating to the page
        close_login_modal(driver)

        # Locate and click the menu item using the provided index
        menu_locator =driver.find_element(By.XPATH, f"/html/body/div[2]/div/div/div[2]/ul/li[{index}]")
        #print(f"/html/body/div[2]/div/div/div[2]/ul/li[{index}]")
        menu_item_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(menu_locator))
        menu_item_link.click()

        # Wait for the page to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f"/html/body/div[2]/div/div/div[2]/ul/li[{index}]"))
        )

        print(f"Successfully navigated to {menu_item} page.")

    except Exception as e:
        print(f"An error occurred while navigating to {menu_item} page: {str(e)}")


def main():
    driver = webdriver.Chrome()
    try:
        open_web_page(driver)
        print("Registration and login")
        generated_username, generated_password = register(driver)
        #login(driver, generated_username, generated_password)
        print("Navigation validation")
        # Determine if the user is logged in
        if is_user_logged_in(driver):
            # User is logged in, show 3 menu items
            menu_items = ["HOME", "CATALOGUE", "ACCOUNT"]
        else:
            # User is not logged in, show 2 menu items
            menu_items = ["HOME", "CATALOGUE"]

        for index, item in enumerate(menu_items, start=1):
            # Pass the index value when calling the function
            navigate_to_page(driver, item, index)
            time.sleep(2)  # Add a short delay for visibility in the example
        print("Add to cart and check that")
        # Add items to the cart
        added_item = add_item_to_cart(driver)
        # Check the cart page to verify that the added items are shown
        check_cart_page(driver, added_item)
        print("Detail information checking in cart page")
        #if is_address_present(driver):
            # Test filling details
            #fill_details_and_submit(driver)
            # Test updating details
            #House,street,city,postal,country=fill_details_and_submit(driver)
        #else:
            # Test updating details
            #House,street,city,postal,country=fill_details_and_submit(driver)

        #Test filling address details
        fill_details_and_submit(driver)
        # Test updating details
        House,street,city,postal,country=fill_details_and_submit(driver)
        # Check if the details are updated
        check_updated_details(driver,House,street,city,postal,country)
        #Test filling payment details
        fill_details_and_submit_Payment(driver)
        # Test updating details
        Card,expires,ccv=fill_details_and_submit_Payment(driver)
        # Check if the details are updated
        check_updated_details_Payment(driver,Card,expires,ccv)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
