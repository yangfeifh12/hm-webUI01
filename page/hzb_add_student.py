import time

from selenium.webdriver.common.by import By

from base.base import BasePage, Beanhandler


#定义对象库层
from common.chose_chanel import Chose
from common.web_util import UtilWebdriver


class HzbAddStudent(BasePage):
    def __init__(self):
        super().__init__()
        self.addstudent_button = (By.XPATH,'//*[@id="app-main"]/div/div[1]/div[1]/div[1]/button[1]/span')
        self.phone_number = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[1]/div/div[1]/input')
        self.HomName = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[2]/div/div/input')
        self.qinshu = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[3]/div/div/div[1]/input')
        self.studentName = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[4]/div/div[1]/input')
        self.studentSex = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[5]/div/div[1]/div[1]/input')
        self.YearMonth = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[6]/div/div/input')
        self.Idcard = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[7]/div/div/input')
        self.LaiYuan = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[8]/div/div/div[1]/input')
        self.BeiZhu = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[9]/div/div/textarea')
        self.submit = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[3]/button[2]/span')
        #退出日历
        self.out_rili = (By.XPATH,'//*[@id="app-main"]/div/div[2]/div/div[2]/div/form/div[6]/label')

    def find_button_addstudent(self):
        button_addstudent = self.get_element(self.addstudent_button)
        return button_addstudent

    def find_phone_number(self):
        phone_number = self.get_element(self.phone_number)
        return phone_number

    def find_HomName(self):
        HomName = self.get_element(self.HomName)
        return HomName

    def find_qishu(self):
        qishu = self.get_element(self.qinshu)
        return qishu

    def find_student_name(self):
        student_name = self.get_element(self.studentName)
        return student_name

    def find_study_sex(self):
        studysex=self.get_element(self.studentSex)
        return studysex

    def find_yearmoth(self):
        yearmoth = self.get_element(self.YearMonth)
        return yearmoth

    def find_idcard(self):
        idcard = self.get_element(self.Idcard)
        return idcard

    def find_laiyuan(self):
        laiyuan = self.get_element(self.LaiYuan)
        return laiyuan

    def find_beizhu(self):
        beizhu = self.get_element(self.BeiZhu)
        return beizhu

    def click_submit(self):
        submit = self.get_element(self.submit)
        return submit
    #退出日历
    def click_out_rili(self):
        out = self.get_element(self.out_rili)
        return out
#定义操作层
class HzbAddHandle(Beanhandler):
    def __init__(self):
        self.Hzb_handler = HzbAddStudent()
        self.driver = UtilWebdriver().houtai_driver()

    def click_button_addstudent(self):
        add_button = self.Hzb_handler.find_button_addstudent().click()

    def input_phone_number(self,phonnumber):
        phone_number = self.input_text(self.Hzb_handler.find_phone_number(),phonnumber)

    def input_homname(self,homname):
        homname = self.input_text(self.Hzb_handler.find_HomName(),homname)

    def click_qinshu(self,chanel):
        # qinshu = self.Hzb_handler.find_qishu().click()
        Chose.chose_chine(self.driver,self.Hzb_handler.find_qishu(),chanel)
    #学员姓名
    def input_studyname(self,studyname):
        studyname = self.input_text(self.Hzb_handler.find_student_name(),studyname)
    #学员性别
    def chose_study_sex(self,sex):
        Chose.chose_chine(self.driver,self.Hzb_handler.find_study_sex(),sex)
    #出生年月
    def input_chushen(self,time):
        time = self.input_text(self.Hzb_handler.find_yearmoth(),time)

    #身份证
    def input_idcard(self,idcard):
        Idc = self.input_text(self.Hzb_handler.find_idcard(),idcard)

    #标记来源
    def chose_laiyuan(self,laiyuan):
        Chose.chose_chine(self.driver,self.Hzb_handler.find_laiyuan(),laiyuan)

    def input_beizhu(self,beizhu):
        beizhu = self.input_text(self.Hzb_handler.find_beizhu(),beizhu)

    def click_submit_button(self):
        button = self.Hzb_handler.click_submit().click()

    #退出日历
    def click_out_rili(self):
        clickrili = self.Hzb_handler.click_out_rili().click()


#定义业务层
class Hzb_add():
    def __init__(self):
        self.Handle = HzbAddHandle()

    def add_user(self,phone,homname,qinshu,studyname,sex,chushen,idcard,laiyuan,beizhu):
        time.sleep(1)
        self.Handle.click_button_addstudent()
        time.sleep(3)
        self.Handle.input_phone_number(phone)
        self.Handle.input_homname(homname)
        self.Handle.click_qinshu(qinshu)
        self.Handle.input_studyname(studyname)
        self.Handle.chose_study_sex(sex)
        self.Handle.input_chushen(chushen)
        time.sleep(1)
        self.Handle.click_out_rili()
        time.sleep(2)
        self.Handle.input_idcard(idcard)
        self.Handle.chose_laiyuan(laiyuan)
        self.Handle.input_beizhu(beizhu)
        self.Handle.click_submit_button()