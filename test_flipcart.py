from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
product=input("enter product")
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("/html/body/div[2]/div/div/button")
driver.find_element_by_name("q").send_keys(product)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
time.sleep(5)
driver.close()
print("closed")

