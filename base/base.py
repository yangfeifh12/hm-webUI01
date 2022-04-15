from common.web_util import UtilWebdriver

from selenium.webdriver.support.wait import WebDriverWait

#对象层基类封装
class BasePage:
    def __init__(self):
        self.driver = UtilWebdriver.houtai_driver()


    def get_element(self,location):
        #添加显示等待加载元素
        wait = WebDriverWait(self.driver,10,1)
        elemet = wait.until(lambda x:x.find_element(*location))
        # elemet = lambda x:x.find_element(*location)
        return elemet

#操作层基类封装
class Beanhandler:
    def input_text(self,elemet,text):
        # elemet.clear()
        elemet.send_keys(text)