import time
import requests
from selenium import webdriver

CHROMEDRIVER = './chromedriver'

name = 'joydesigner/csdn-python'

api = 'https://api.github.com/repos/' + name

weburl = 'https://github.com/' + name

old_time = None

while True:
    r = requests.get(api)
    if r.status != 200:
        print('请求api失败')
        break
    # how to tell project is updated or not? simple, by project time, if time updated, project is updated
    now_time = r.json()['updated_at']
    if not old_time:
        old_time = now_time
    if old_time < now_time:
        print('项目更新了')
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
        driver.get(weburl)

    # 休眠十分钟
    time.sleep(600)
