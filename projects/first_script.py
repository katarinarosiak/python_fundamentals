from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://youtube.com")  # sending a request

accept_button = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form'
)  # locating an element on the page

accept_button.click()

search_box = driver.find_elements_by_xpath('//*[@id="search"]')
search_box[0].send_keys("Funny kittens")  # input text into a search box
search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')

search_button.click()
