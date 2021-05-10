from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.whatsapp.com/?lang=en")
time.sleep(3)

accept_cookies_button = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div[3]/a[2]"
)
accept_cookies_button.click()

web_app_button = driver.find_element_by_xpath('//*[@id="header-inner"]/nav/ul/li[1]/a')
web_app_button.click()

sonek = driver.find_element_by_xpath(
    '//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div[1]/div[2]/div[1]/div[1]/span/span'
)

sonek.click()

message_box = driver.find_element_by_xpath(
    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
)

message_box[0].send_keys(
    "to jest automatyczna wiadomosc wyslana do ciebie przez skrypt, ktory napisala Kasia, zeby cie podenerwowac. Hahaha"
)

driver.key_down(Keys.ENTER)
