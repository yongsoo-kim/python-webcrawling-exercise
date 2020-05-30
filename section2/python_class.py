from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    # def set_info(self, name, phone):
    #     self.name = name
    #     self.phone = phone

    def print_info(self):
        print("---------")
        print("name:" + self.name)
        print("phone:" + self.phone)
        print("---------")

    def __del__(self):
        print("delete!!!")

user1 = UserInfo("kim", "11111111")
user2 = UserInfo("lee", "22222222")

#Print memory address
print(id(user1))
print(id(user2))

# user1.set_info("kim", "11111111")
# user2.set_info("lee", "22222222")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)