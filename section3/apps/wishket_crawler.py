import sys
import io
from bs4 import BeautifulSoup
import requests, json
from fake_useragent import UserAgent

# Rest: POST, GET, PUT:UPDATE, REPLACE (FETCH: UPDATE, MODIFY), DELETE
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# URL
URL = "https://www.wishket.com/accounts/login/"

# Fake User-Agent
ua = UserAgent()
# print(ua.ie)
# print(ua.chrome)
# print(ua.random)


with requests.Session() as s:
    #URL connection for getting csrf cookies
    s.get(URL,  headers={'User-Agent':str(ua.chrome)})

    # Login info
    LOGIN_INFO = {
        "identification": "your_id_1234",
        "password": "your_pw_1234",
        "csrfmiddlewaretoken": s.cookies['csrftoken']
    }
    print('[token]', s.cookies['csrftoken'])

    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent': str(ua.chrome), 'Referer': str(URL)})
    #HTML check
    print(response.status_code)
    print(response.text)
    # 'Referer header' to be sent by your Web browser, but none was sent. So add Referer header.
    # And "User-Agent" is python, that's why. We need to 'fake' this
    print(response.headers)

    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        project_list = soup.select_one("div.user-project").find_all('div')
        print(project_list)
        #TODO need to get more info...
        for i in project_list:
            print(i.contents[0], i.find('p').string)

