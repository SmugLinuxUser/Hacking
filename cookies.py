from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
# path to chromedriver.exe 
# create nstance of webdriver
browser = webdriver.Firefox()
action = ActionChains(browser)
# google url
url = 'https://cookieupdate.neocities.org/'
# Code to open a specific url
browser.get(url)

script = "localStorage.setItem('CookieClickerGame', 'Mi4wMTJ8fDE2NDkwNDg3NjYxMDA7MTY0OTA0ODc2NjEwMDsxNjQ5NDY0NjU4NTE5O1NjaWVuY2UgUG9ydGFsO3ZqZ3pmfDExMTExMDAxMTAwMTAwMTAwMTB8MjM1MzY0ODA4MC4xMDczMzU2OzM3OTA4Njc4NTQ5OS43NjQ5NTsxMjY1Mzc7MTg7MTc2OTI1NzkwNzAuMDgzOTQyOzE2NTswOzA7MDswOzA7MDswOzA7MDsxODswOzA7MDswOzA7MDs7MDswOzA7MDswOzA7MDstMTstMTstMTstMTstMTswOzA7MDswOzU1OzA7MDsxOzU7MTY0OTM5NDM2NjEwOTswOzA7O3wxMjAsMTIwLDE1OTUxODQ1ODE5LDEsLDA7MTE0LDExNCw5ODc3MDQ4MDA2LDEsLDA7ODUsODUsMTQ4OTIyOTM1MSwwLCwwOzcwLDcwLDQwNTIwNzE5MzksMCwsMDs1Nyw1Nyw4NTY3NDM1NDgxLDAsLDA7NTIsNTIsMzczODQwOTAxNTksMCwsMDszMiwzMiwxMDk3MDM4MjI0NDMsMCwsMDsyNCwyNCwxMjgzODA5NDM2OTMsMSwsMDs2LDYsMjQ2NDY1ODg2ODUsMSwsMDswLDAsMCwwLCwwOzAsMCwwLDAsLDA7MCwwLDAsMCwsMDswLDAsMCwwLCwwOzAsMCwwLDAsLDA7MCwwLDAsMCwsMDt8MTExMTExMTExMTExMDAxMTExMTExMTExMTExMTExMTExMTExMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTExMTExMTExMTExMTExMDEwMTAwMDExMTExMDExMDAwMDAwMDAxMTAwMDAxMDEwMTExMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMTEwMDEwMTAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTExMTAwMDAxMTExMTEwMDAwMDAxMTExMDAwMDAwMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDB8MTExMTExMTAwMDAwMDAwMDExMTExMTEwMDAwMDAwMTExMTExMTEwMDExMTExMDExMDExMDEwMDAwMDAwMDAwMDAwMDExMDAxMTExMTEwMDAwMDAwMDAwMDAwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTEwMDAxMDAwMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDB8%21END%21');"

browser.execute_script(script)
WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "bigCookie")))

bigCookie = browser.find_element_by_id("bigCookie")


while True:

    bigCookie.click()


