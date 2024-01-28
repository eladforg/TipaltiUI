import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://qa-tipalti-assignment.tipalti.com/index.html")

driver.find_element(By.CSS_SELECTOR, "nav>ul a").click()
menu_items=driver.find_elements(By.CSS_SELECTOR, "#menu li")
menu_items_texts =[]
for item in menu_items:
    text = item.text
    menu_items_texts.append(text)
# print(menu_items_texts)

isKika=False
for text in menu_items_texts:
    if text=="Kika":
        isKika=True

# print(isKika)
# menu_items_texts['Kika'].click()
# or;
driver.find_element(By.CSS_SELECTOR,"#menu > div > ul > li:nth-child(2) > a").click()
time.sleep(1)
driver.find_element(By.ID, "name").send_keys("Cookie")
driver.find_element(By.ID, "email").send_keys("cookie@gmail.com")
driver.find_element(By.ID, "message").send_keys("this is a message")
# driver.find_element(By.CSS_SELECTOR, "[value='send']").click()


input("click")




