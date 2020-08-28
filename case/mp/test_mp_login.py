import pytest

from page.mp.login_page import LoginProxy
from utils import DriverUtils, is_element_exist


# 定义测试类
@pytest.mark.run(order = 2)
class TestLogin:
    # 定义初始化方法 # 测试之前需要打开浏览器，窗口最大化等业务操作，我们已经在utils中写好，在此直接实例化对象调用
    def setup_class(self):
        # 获取驱动对象
        self.driver = DriverUtils.get_mp_driver()
        # 创建好所需要的调用业务方法所在的类的对象
        self.login_proxy = LoginProxy()

    # 定义测试方法
    def test_mp_login(self):
        # 3.1定义测试数据
        username = "13012345678"
        code = "246810"
        # 3.2调用业务方法形成完整业务操作
        # 在此调用的是login_page中的业务层LoginProxy类中的test_mp_login方法
        self.login_proxy.test_mp_login(username, code)
        # 3.3断言 在此断言调用的事utils文件中的is_element_exist公用方法
        assert is_element_exist(self.driver, "江苏传智播客")

    # 定义销毁的方法--关闭
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
