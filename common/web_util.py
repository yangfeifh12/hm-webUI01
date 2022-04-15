import time

from selenium import webdriver

class UtilWebdriver:
    # 定义浏览器驱动，可以同时定义几个浏览器驱动
    #定义管理系统的浏览器驱动
    qd = None
    #登录状态
    login_zt = True
    # 定义管理系统的浏览器驱动
    @classmethod
    def houtai_driver(self):
        if self.qd is None:
            # self.qd = webdriver.Chrome()
            self.qd = webdriver.Chrome(r'F:\python\93\chromedriver.exe')
            self.qd.maximize_window()
            self.qd.get("http://erp2.hzb-it.com/#/login")
            # time.sleep()
        return self.qd



    # #定义退出系统浏览器驱动
    # def out_driver(self):
    #     if self.qd is not None:
    #         #关闭浏览器
    #         self.houtai_driver().quit()
    #         self.qd = None

    #定义退出系统浏览器驱动
    def out_driver(self):
        if self.qd and self.login_zt:
            #关闭浏览器
            self.houtai_driver().quit()
            self.qd = None
    #修改登录状态
    @classmethod
    def set_login_zt(self,zt):
        self.login_zt = zt

