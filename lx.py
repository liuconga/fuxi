import os
import random

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
class PageLogin(object):
    driver=None
    def get_driver(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['deviceName'] = '192.168.56.102:5555'
        desired_caps['appPackage']='com.yunmall.lc'
        desired_caps['appActivity']='com.yunmall.ymctoc.ui.activity.MainActivity'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=desired_caps)

        self.driver.implicitly_wait(10)
        # driver.push_file('/sdcard/接口清单.txt','/Users/liucong/Desktop/接口清单.txt')
        # print(driver.current_activity)
        # driver.start_activity('com.yunmall.lc','com.yunmall.ymctoc.ui.activity.MainActivity')
        # driver.find_element_by_xpath('//*[contains(@text,"运动户外")]').click()
        # driver.open_notifications()
        # el=WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_xpath('//*[contains(@text,"刘德华")]'))
        # el.click()

        # print(driver.network_connection)
        # driver.get_screenshot_as_file(os.getcwd()+'/1.png')
        # for i in range(0,3):
        #     print(i)
        #     driver.keyevent(24)
        # print(driver.get_window_size())
        # driver.find_element_by_xpath('//*[contains(@text,"我")]').click()
        # touch=TouchAction(driver)
        # touch.move_to(driver.find_element_by_xpath('//*[contains(@text,"帮助中心")]')).perform()
        return self.driver
    def quitdirver(self):
        self.driver.quit()

