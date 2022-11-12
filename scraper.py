from cmath import e
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\Owner\Documents\chromedriver")
driver.get("https://www.reddit.com/r/AskReddit/top/?t=month")

linkList = []
titleList = []
bodyTextList = []
commentList = []

def main():

    dropdown_button = driver.find_element(by=By.ID, value="USER_DROPDOWN_ID")
    dropdown_button.click()

    #figure out why dark mode button has to be clicked this way
    try: 
        dropdown_menu = driver.find_element(by=By.CLASS_NAME, value="_2uYY-KeuYHKiwl-9aF0UiL")
        buttons = dropdown_menu.find_elements(by=By.TAG_NAME, value="button")
        settings_button = buttons[9]
        settings_button.click()
        print("Left bar didn't appear")
    except:
        dropdown_menu = driver.find_element(by=By.CLASS_NAME, value="_2uYY-KeuYHKiwl-9aF0UiL")
        buttons = dropdown_menu.find_elements(by=By.TAG_NAME, value="button")
        settings_button = buttons[1]
        settings_button.click()
        print("Left bar appeared")

    postCard = driver.find_elements_by_tag_name('a')
    for post in postCard:
        links = post.findAll

    

main()


#driver.quit()