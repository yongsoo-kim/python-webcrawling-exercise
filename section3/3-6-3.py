import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

# Rest: POST, GET, PUT:UPDATE, REPLACE (FETCH: UPDATE, MODIFY), DELETE
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# firefox_options = Options()
# firefox_options.add_argument("--headless")

driver = webdriver.Firefox(#options=firefox_options,
                           executable_path="C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/geckodriver.exe")
driver.set_window_size(1920,1280)
driver.implicitly_wait(5)

driver.get('https://nsite.net/login/')
time.sleep(7)
driver.implicitly_wait(10)
driver.find_element_by_name('username_or_email').send_keys('your_id_1234')
driver.implicitly_wait(1)
driver.find_element_by_name('password').send_keys('your_pw_1234')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="content"]/form/button').click()

print('Screenshot done')