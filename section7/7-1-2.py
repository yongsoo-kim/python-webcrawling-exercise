# Section 7-1
# Selenium advanced(1)

import sys
import io

# About managing time
import time
# bs4
from bs4 import BeautifulSoup
# Selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import \
    expected_conditions as EC  # This will help program keep running when it gets expected result.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  # This will make web browser input key by selenium (up,enter etc...)
# Image download
import urllib.request as req
# Image byte processing
from io import BytesIO
# Excel processing
import xlsxwriter

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Firefox option
firefox_options = Options()
# Set headless
firefox_options.add_argument("--headless")
# Sound mute(noisy!)
firefox_options.add_argument("--mute-audio")

# Webdriver setting(Firefox) -Headless mode
# browser = webdriver.Firefox(executable_path="C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section7/webdriver/firefox/geckodriver.exe"
#                             , options=firefox_options)


# Webdriver setting(Firefox) -Normal mode
browser = webdriver.Firefox(
    executable_path="C:/Users/yongs/OneDrive/Desktop/personal_projects/python/inforun/python-webcrawling-exercise/section7/webdriver/firefox/geckodriver.exe")

# Excel process start
workbook = xlsxwriter.Workbook("you_crawl_result.xlsx")

# Work sheet
worksheet = workbook.add_worksheet()

# Firefox browser stanby(To prevent from missing initial timing)
browser.implicitly_wait(5)

# Browser size control
# minimize_window()
# maximize_window()
browser.set_window_size(1920, 1280)

# Page move(GET)
browser.get("https://www.youtube.com/watch?v=oPUgiyNYUSc")
# Wait for 5 secs
time.sleep(5)

# codes for waiting until getting HTML focus
# Explicitly_wait
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'html'))).send_keys(Keys.PAGE_DOWN)

# Wait for 2 secs
time.sleep(2)

# Print page contents
# print('Before Page Contents : {}'.format(browser.page_source))

# Standby time for loading and getting new data
scroll_pause_time = 4

# Current page scroll height. -> You can get this by running javascript.
last_height = browser.execute_script("return document.documentElement.scrollHeight")

print()

# Loop until all comment data will be loaded(rendering).
while True:
    # Move scroll bar
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
    # Stand by
    time.sleep(scroll_pause_time)

    # Scroll bar move -> new comments loading(rendering) -> Get current scroll height
    new_height = browser.execute_script("return document.documentElement.scrollHeight")

    # Compare new height and old height
    print("Last Height : {}, Current Height : {}".format(last_height, new_height))

    # If there is no new data loaded, end loop.
    if new_height == last_height:
        # End while
        break

    # Change height
    last_height = new_height

# Initialize bs4
soup = BeautifulSoup(browser.page_source, "html.parser")

# statistics list
top_level = soup.select('div#menu-container yt-formatted-string#text')

# Comment list selector
comment = soup.select('ytd-comment-renderer#comment')

# HTML source check
# print(soup.prettify())

print('Total Like Count : {}'.format(top_level[0].text.strip()))
print('Total DisLike Count : {}'.format(top_level[1].text.strip()))

# Excel row count
ins_cnt = 1

# Dom repetition
for dom in comment:
    print()
    # Image URL
    img_src = dom.select_one("#img").get('src')

    # Writer
    author = dom.select_one('#author-text > span').text.strip()

    # Comment body
    content = dom.select_one('#content-text').text.strip()

    # Like
    posi_cnt = dom.select_one('#vote-count-middle').text.strip()

    print('Thumbnail Image URLS : {}'.format(img_src if img_src else 'None'))

    # Writer
    print('Author : {}'.format(dom.select_one('#author-text > span').text.strip()))

    # Comment body
    print('Content Text : {}'.format(dom.select_one('#content-text').text.strip()))

    # Like
    print('Vote Positive Count : {}'.format(dom.select_one('#vote-count-middle').text.strip()))

    print()

    # Save in Excel
    worksheet.write('A%s' % ins_cnt, author)  # Column A
    worksheet.write('B%s' % ins_cnt, content)  # Column B
    worksheet.write('C%s' % ins_cnt, posi_cnt)  # Column C

    # Save Image in Excel
    if img_src:
        # Request image anc convert into bytes
        img_data = BytesIO(req.urlopen(img_src).read())
        # Image data check
        print(img_data)

        worksheet.insert_image('D%s' % ins_cnt, author, {'image_data': img_data})
    else:
        worksheet.write('D%s' % ins_cnt, 'None')

    # Increase count
    ins_cnt += 1

    print()

# Brwoser quite
browser.quit()

# Close Excel file
workbook.close()