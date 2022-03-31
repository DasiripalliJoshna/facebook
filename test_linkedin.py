from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
print("test case started")
driver.maximize_window()
driver.get("https://www.linkedin.com/")
driver.find_element_by_name("q").send_keys("Facebook")
time.sleep(7)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(7)
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("9880374096")
driver.find_element_by_name("pass").send_keys("joshna@123")
driver.find_element_by_name("login").send_keys(Keys.ENTER)
time.sleep(10)