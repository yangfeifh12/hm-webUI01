#定义测试类
import time

import pytest

from common.web_util import UtilWebdriver
from page.hzb_add_student import Hzb_add
from page.hzb_home import Home_yewu
from page.hzb_login import Hzb_Login


@pytest.mark.run(order=2)
class TestUserAdd:
    # 定义测试方法
    def setup_class(self):
        self.login = Hzb_Login()
        self.home = Home_yewu()
        self.add = Hzb_add()

    def teardown_class(self):
        UtilWebdriver().out_driver()

    def test_user_login(self):
        self.login.login_user("admin","123")

    def test_user_addzaixian(self):
        self.home.c_home()
        self.add.add_user('15566669999','ssss','妈妈','我就是我','男','2022-03-04','433123199512055261','手动输入','哈哈哈哈哈哈哈哈哈')