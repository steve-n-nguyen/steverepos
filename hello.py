from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome("C:\\Users\\steve.nguyen\\Documents\\chromedriver")
driver.maximize_window()
driver.get("http://google.com")


element = driver.find_element_by_id("lst-ib")
element.send_keys("books")

element.send_keys(Keys.RETURN)
time.sleep(2)

try:
    driver.find_element_by_partial_link_text("Amazon.com: Books").click()
    print("Pass, you good Steve")

except NoSuchElementException:
    print("Failed, no such element Steve")


driver.save_screenshot("C:\\Users\\steve.nguyen\\screenshot.png")
text = driver.find_element_by_xpath(".//body").text
print(text)


time.sleep(5)
driver.quit()