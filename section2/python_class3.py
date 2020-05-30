from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


# Class variable, Instance variable

class WareHouse:
    # class variable
    stock_num = 0;

    def __init__(self, name):
        # name is instance variable
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1

user1= WareHouse('kim')
user2= WareHouse('park')

print(user1.name)
print(user2.name)

print(user1.__dict__)
print(user2.__dict__)
print(WareHouse.__dict__) # namespace -> class name space -> class variable

print(user1.stock_num)
print(user2.stock_num)