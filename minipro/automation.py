from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import pyautogui
import pyperclip


options = Options()
options.add_experimental_option("detach", True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# id입력
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()

pyperclip.copy("")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
# pw 입력
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

login_btn = driver.find_element_by_css_selector("#log\.login")
login_btn.click()

print(driver.current_url)

