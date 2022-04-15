#hzb宏之博教务系统登录页面对象


#定义对象库层
import time

import allure
from selenium.webdriver.common.by import By
from base.base import BasePage, Beanhandler


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username =(By.XPATH,'//*[@id="content"]/div/form/div[3]/div/div[1]/input')
        self.password = (By.XPATH,'//*[@id="content"]/div/form/div[4]/div/div/input')
        self.button = (By.XPATH,'//*[@id="content"]/div/form/button')

    #定位账号输入框
    def find_username(self):
        # username = self.get_element(self.username)
        # return username

        return self.get_element(self.username)
    #定位密码输入框
    def find_password(self):
        # password = self.get_element(self.password)
        # return password
        return self.get_element(self.password)
    #定位按钮位置
    def find_button(self):
        # button = self.get_element(self.button)
        # return button
        return self.get_element(self.button)

#定义操作库层
class LoginHandle(Beanhandler):
    def __init__(self):
        self.login_page = LoginPage()
    @allure.step(title='输入用户名')
    def input_username(self,username):
        # self.login_page.find_username(username)
        self.input_text(self.login_page.find_username(),username)
        # uname = self.login_page.find_username()
        # uname.send_keys(username)

    @allure.step(title='输入密码1')
    def input_password(self,password):
        # self.login_page.find_password()
        self.input_text(self.login_page.find_password(),password)
        # pwd = self.login_page.find_password()
        # pwd.send_keys(password)

    def click_button(self):
        self.login_page.find_button().click()

#定义业务层
class Hzb_Login:
    def __init__(self):
        self.login_handle = LoginHandle()


    #登录业务
    def login_user(self,username,password):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.click_button()
        time.sleep(5)