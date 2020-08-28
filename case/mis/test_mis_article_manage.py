# 定义测试类
import time

import pytest

import config
from page.mis.mis_article_page import MisArticleProxy
from page.mis.mis_home_page import MisHomeProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order = 103)
class TestMisArticle:
    # 1.打开浏览器
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mis_driver()
        # 创建首页业务层的对象
        self.mis_home_proxy = MisHomeProxy()
        # 创建文章审核业务层的对象
        self.mis_article_proxy = MisArticleProxy()
        # # 创建登录页面的业务层对象
        # self.mis_login_proxy = MisLoginProxy()

    # def setup(self):
    #     time.sleep(2)
    #     self.driver.get("http://ttmis.research.itcast.cn/#/home")

    # 登录
    # @pytest.mark.run(order = 1)
    # def test_login(self):
    #     self.mis_login_proxy.test_mis_login("testid", "testpwd123")

    # 测试审核文章的测试用例
    def test_pass_article(self):
        # 2.组织测试数据
        title_name = config.PubArticleName
        # 3.执行测试步骤
        # 调用进入审核文章页面的业务方法
        self.mis_home_proxy.to_mis_article()
        # 调用审核文章的业务方法
        self.mis_article_proxy.test_article_pass(title_name)
        # 4.结果断言
        assert is_element_exist(self.driver, "驳回")

    # def test_reject_article(self):
    #     # 调用进入审核文章页面的业务方法
    #     self.mis_home_proxy.to_mis_article()
    #     # 调用驳回的业务方法
    #     self.mis_article_proxy.test_article_reject()
        # 4.结果断言
        # assert is_element_exist(self.driver, "查看")

    # 5.关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
