# 开发者：Annona
# 开发时间：2022/12/7 15:55

from selenium import webdriver
import time
driver= webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(4)
driver.quit()
