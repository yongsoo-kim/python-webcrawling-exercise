import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Rest: POST, GET, PUT:UPDATE, REPLACE (FETCH: UPDATE, MODIFY), DELETE
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(options=firefox_options,
                           executable_path="C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/geckodriver.exe")
# wati for 5 mins...
driver.implicitly_wait(5)
driver.get('https://google.com')
driver.save_screenshot(
    "C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/test.png")
driver.implicitly_wait(5)
driver.get('https://daum.net')
driver.save_screenshot(
    "C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/test2.png")
driver.quit()

print('screenshot done.')

# "C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/geckodriver.exe"
