import pytest

from common.web_util import UtilWebdriver

@pytest.mark.run(order=1)
class TestBegin:
    def test_begin(self):
        UtilWebdriver.set_login_zt(False)