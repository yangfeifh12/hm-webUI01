
#定义对象库层
from selenium.webdriver.common.by import By

from base.base import BasePage, Beanhandler


class getuser(BasePage):
    def __init__(self):
        super().__init__()
        self.input_kuang =(By.XPATH,'//*[@id="app-main"]/div/form/div/div[1]/div/div/div/div/div/input')
        self.get_buton = (By.XPATH,'//*[@id="app-main"]/div/form/div/div[2]/div/div/button[1]')

    def find_input_kuang(self):
        input = self.get_element(self.input_kuang)
        return input

    def find_get_button(self):
        button = self.get_element(self.get_buton)
        return button


class getuserHandle(Beanhandler):
    def __init__(self):
        self.handle = getuser()
    def input_kuang(self,str):
        self.input_text(self.handle.find_input_kuang(),str)

    def click_button(self):
        self.handle.find_get_button().click()

class  get_user_yewu():
    def __init__(self):
        self.userhandle = getuserHandle()
    def get_one_user(self,str):
        self.userhandle.input_kuang(str)
        self.userhandle.click_button()

