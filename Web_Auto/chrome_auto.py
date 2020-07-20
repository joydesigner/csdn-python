from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROMEDRIVER = './chromedriver'


driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
driver.get('https://www.baidu.com')

# get input
input = driver.find_element_by_id('kw')
input.clear()
# type content
input.send_keys('CSDN')
# click enter
input.send_keys(Keys.ENTER)
