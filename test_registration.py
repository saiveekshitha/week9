from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ✅ Start ChromeDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # ✅ Open your app (update the port if different)
    driver.get("http://localhost:32676")

    # ✅ Wait for page to load
    wait = WebDriverWait(driver, 15)

    # ✅ Fill the registration form
    wait.until(EC.presence_of_element_located((By.NAME, "full_name"))).send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
    driver.find_element(By.NAME, "username").send_keys("testuser123")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "confirm_password").send_keys("password123")
    driver.find_element(By.NAME, "phone").send_keys("9876543210")
    driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
    driver.find_element(By.NAME, "gender").send_keys("Male")
    driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

    # ✅ Wait for the submit button to appear
    submit_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    # ✅ Scroll into view (helpful for buttons at bottom)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    time.sleep(1)

    # ✅ Use JavaScript click (bypasses overlay issues)
    driver.execute_script("arguments[0].click();", submit_btn)

    # ✅ Wait a bit for confirmation / redirection
    time.sleep(3)

    # ✅ Optional: Take screenshot after submission
    driver.save_screenshot("form_submission_result.png")
    print("✅ Test Completed Successfully!")

except TimeoutException:
    print("❌ Timeout: Some element took too long to load. Check app or selector names.")
    driver.save_screenshot("error_timeout.png")

except Exception as e:
    print(f"❌ Test Failed: {e}")
    driver.save_screenshot("error_generic.png")

finally:
    # ✅ Always close browser at the end
    driver.quit()
