import sys
import io
from bs4 import BeautifulSoup
import requests, json

# Rest: POST, GET, PUT:UPDATE, REPLACE (FETCH: UPDATE, MODIFY), DELETE
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# login user info
LOGIN_INFO = {
    "user_id": "your_id_1234",
    "user_pw": "your_pw_1234"
}

#Session creation and keep it in "with"

with requests.Session() as s:
    login_req = s.post("https://user.ruliweb.com/member/login_proc", data=LOGIN_INFO)
    #HTML source check
    #print('login_req', login_req.text)
    #Header check
    #HTML source check
    print('headers', login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get("https://bbs.ruliweb.com/family/4442/board/184513/write")
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())

        schedule = soup.select_one("table.game_info_table td:nth-of-type(3)").find_all('span')
        #print(schedule)

        for i in schedule:
            if i.string is not None:
                print(i.string)
