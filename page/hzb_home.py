import time

from selenium.webdriver.common.by import By

from base.base import BasePage, Beanhandler


#定义对象库层
class HonePage(BasePage):
    def __init__(self):
        super().__init__()
        #登录成功显示账号名称
        self.username = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div')
        #点击学员管理
        self.xueyuanGL = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')
        #点击在线学员
        self.ZXxueyuan = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li')
    #找到账号名称
    def find_username(self):
        username = self.get_element(self.username)
        return username
    #找到学员管理
    def find_xueyuanGL(self):

        GL = self.get_element(self.xueyuanGL)
        return GL

    #找到在线学员
    def find_ZXxueyuan(self):

        ZX = self.get_element(self.ZXxueyuan)
        return ZX

#定义操作层
class HomeHandle(Beanhandler):
    def __init__(self):
        self.home_page  = HonePage()
        # time.sleep(10)

    #找到登录用户名
    def find_username(self):
        text = self.home_page.find_username().text
        return text
    #获取学员管理按钮
    def click_xueyuanGL(self):
        Button = self.home_page.find_xueyuanGL().click()
        return Button
    #获取在线学员信息
    def click_ZXxueyuan(self):
        button = self.home_page.find_ZXxueyuan().click()
        return button

#定义业务层
class Home_yewu():
    def __init__(self):
        self.handle = HomeHandle()

    #获取用户名信息
    def get_username(self):
        self.handle.find_username()

    #首页业务
    def c_home(self):
        time.sleep(5)
        self.handle.click_xueyuanGL()
        time.sleep(20)
        self.handle.click_ZXxueyuan()


