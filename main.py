# pip3 install requests bs4
import requests
import urllib3
import json
from bs4 import BeautifulSoup
import time
import os

urllib3.disable_warnings()

def join_Form(cookies,CourseNo):
    base_url = "https://courseselection.ntust.edu.tw/AddAndSub/B01/"
    r_data = requests.post(base_url+"Join",headers=header,data=f"CourseNo=%0A{'+'*32}{CourseNo}%0A{'+'*28}&type=1".encode('utf-8'),cookies=cookies,verify=False)
    r_data_2 = requests.get(base_url+"B01",cookies=cookies,verify=False)
    return r_data.status_code

def getname(cookies):
    base_url = "https://courseselection.ntust.edu.tw/AddAndSub/B01/"
    r_data_2 = requests.get(base_url+"B01",cookies=cookies,verify=False)
    soup = BeautifulSoup(r_data_2.text, 'html.parser')
    if len(soup.find_all("span",{"class": "text-success"})) != 9:
        return "登入失敗"
    else:
        return soup.find_all("span",{"class": "text-success"})[7].text
    
def getcourse(cookies,course):
    base_url = "https://courseselection.ntust.edu.tw/AddAndSub/B01/"
    r_data_2 = requests.get(base_url+"B01",cookies=cookies,verify=False)
    soup = BeautifulSoup(r_data_2.text, 'html.parser')
    for i in soup.find_all("table",{"id": "cartTable"})[0].find_all("td"):
        if course in i.text:
            return 1
    return 0

config = {}
header = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}

with open(os.path.abspath('config.json'),"r") as f:
    config = json.load(f)


print(f"登入身份：{getname(config['Cookie'])}。若登入身分或課碼錯誤，請立即退出，將於 5 秒後開始執行")
time.sleep(5)

while True:
    for i in config['CourseNo']:
        join_Form(config['Cookie'],i)
        if getcourse(config['Cookie'],i) == 1:
            config['CourseNo'].remove(i)
            print(f"恭喜你！！！選課課碼：{i}{getcourse(config['Cookie'],i)} 上了啊啊啊！！")
        else:
            print(f"選課課碼：{i}{getcourse(config['Cookie'],i)} 還沒上，我們一起加油！！")
