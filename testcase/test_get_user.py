import pytest

from common.web_util import UtilWebdriver
from page.hzb_add_student import Hzb_add
from page.hzb_get_user import get_user_yewu
from page.hzb_home import Home_yewu
from page.hzb_login import Hzb_Login

@pytest.mark.run(order=3)
class TestUserGet:
    # 定义测试方法
    def setup_class(self):
        self.login = Hzb_Login()
        self.home = Home_yewu()
        self.add = Hzb_add()
        self.get = get_user_yewu()

    def teardown_class(self):
        UtilWebdriver().out_driver()

    def test_get_one_user(self):
        self.get.get_one_user("15566668888")
