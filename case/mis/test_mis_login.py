import pytest

from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


# 定义测试类
@pytest.mark.run(order = 102)
class TestLogin:
    # 定义初始化方法 # 测试之前需要打开浏览器，窗口最大化等业务操作，我们已经在utils中写好，在此直接实例化对象调用
    def setup_class(self):
        # 获取驱动对象
        self.driver = DriverUtils.get_mis_driver()
        # 创建好所需要的调用业务方法所在的类的对象
        self.mis_login_proxy = MisLoginProxy()

    # 定义方法级别的初始化，恢复原点，也就是恢复到首页页面
    def setup_method(self):
        self.driver.get("http://ttmis.research.itcast.cn")

    # 定义测试方法
    def test_mis_login(self):
        # 3.1定义测试数据
        username = "testid"
        password = "testpwd123"
        # 3.2调用业务方法形成完整业务操作
        self.mis_login_proxy.test_mis_login(username, password)
        # 3.3断言 在此断言调用的事utils文件中的is_element_exist公用方法
        assert is_element_exist(self.driver, "退出")

    # 定义销毁的方法--关闭
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
