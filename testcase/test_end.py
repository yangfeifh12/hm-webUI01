import pytest

from common.web_util import UtilWebdriver

@pytest.mark.run(order=10)
class TestEnd:
    def test_end(self):
        UtilWebdriver.set_login_zt(True)
        UtilWebdriver.out_driver()