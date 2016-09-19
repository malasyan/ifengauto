#-*- coding: UTF-8 -*-
'''
Created on 2015年12月6日

@author: li_min
'''

from appium import webdriver
import time

class CommonFunctions(object):
    '''
                公用函数类
    '''


    def setup(self):
        '''
                            打开应用，划过欢迎页
        '''
        global DRIVER
        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'MI_NOTE_LTE'
        desired_caps['app'] = 'C:\\Users\\li_min\\Desktop\\apptestcase\\F_IfengNewsV524_V5.2.4_1603.apk'
        desired_caps['appPackage'] = 'com.ifeng.news2'
        desired_caps['appActivity'] = 'com.ifeng.news2.activity.SplashActivity'
        DRIVER = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        
    def Login(self,username,psd):
        '''
                            进入用户中心，登陆账号
        '''
        DRIVER.find_element_by_id("com.ifeng.news2:id/tab_menu_item_rb_account").click()
        time.sleep(2)
        DRIVER.find_element_by_id("com.ifeng.news2:id/img_user_circle_head").click()
        time.sleep(2)
        username1=DRIVER.find_element_by_id("com.ifeng.news2:id/ul_input_user_account")
        username1.click()
        username1.send_keys(username)
        time.sleep(3)
        Password=DRIVER.find_element_by_id("com.ifeng.news2:id/ul_input_user_password")
        Password.click()
        Password.send_keys(psd)
        #click 登陆 按钮
        DRIVER.find_element_by_id("com.ifeng.news2:id/ul_button_login").click()
        time.sleep(5)
        
        
    def gettest(self,loc):
        '''
                            获取元素定位
        '''
        elem=DRIVER.find_element_by_id(loc)
        return elem.text
            