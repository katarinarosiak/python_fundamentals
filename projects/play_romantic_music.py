from selenium import webdriver

import pyautogui
import time

driver = webdriver.Chrome()

driver.get("https://youtube.com")

accept_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form'
)  # locating an element on the page

accept_button.click()
search_box = driver.find_elements_by_xpath('//*[@id="search"]')
search_box[0].send_keys("Romantic music")

search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
search_button.click()

time.sleep(3)
pyautogui.moveTo(300, 300)
pyautogui.moveTo(300, 600)
pyautogui.click()


time.sleep(7)

pyautogui.moveTo(850, 650)
pyautogui.click()
