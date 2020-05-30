import sys
import io
from selenium import webdriver


# Rest: POST, GET, PUT:UPDATE, REPLACE (FETCH: UPDATE, MODIFY), DELETE
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

driver = webdriver.Firefox(executable_path="C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/geckodriver.exe")
#wati for 5 mins...
driver.implicitly_wait(5)
driver.get('https://google.com')
driver.save_screenshot("C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/test.png")
driver.implicitly_wait(5)
driver.get('https://daum.net')
driver.save_screenshot("C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/test2.png")
driver.quit()

print('screenshot done.')

#"C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section3/webdriver/firefox/geckodriver.exe"
