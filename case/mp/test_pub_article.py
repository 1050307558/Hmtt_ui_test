# 定义测试类
import time

import pytest

import config
from page.mp.home_page import HomeProxy, HomeHandle
from page.mp.publish_articles_page import PubAriProxy
from utils import DriverUtils, is_element_exist, get_case_data


@pytest.mark.run(order = 3)
class TestPubArticle:
    # 1.打开浏览器
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mp_driver()
        # 创建首页业务层的对象
        self.home_proxy = HomeProxy()
        # 创建发布文章业务层的对象
        self.pub_ari_proxy = PubAriProxy()
        # 创建登录页面的业务层对象
        # self.login_proxy = LoginProxy()

    #
    def setup_method(self):
        self.driver.get("http://ttmp.research.itcast.cn/")

    # 定义测试方法
    @pytest.mark.parametrize(("ari_title", "ari_context", "ari_channel", "expect"),
                             get_case_data("./data/mp/test_pub_ari_atl.json"))
    def test_pub_ari(self, ari_title, ari_context, ari_channel, expect):
        # 2.组织测试数据
        config.PubArticleName= ari_title.format(time.strftime("%H%M%S"))
        # 3.执行测试步骤
        self.home_proxy.to_pub_air_tab()
        self.pub_ari_proxy.test_pub_aritcal(config.PubArticleName, ari_context, ari_channel)
        # 4.结果断言
        assert is_element_exist(self.driver, expect)
        # HomeHandle().cilck_context_tab()

    """
    不使用参数化的方法
    def test_pub_ari(self):
    # 2.组织测试数据
    ari_title = "BJ23_TESTNB_{}".format(time.strftime("%H%M%S"))
    ari_context = "我不想学测试，要秃头的"
    ari_channel = "软件测试"
    # # 执行登录
    # self.login_proxy.test_mp_login("13012345678", "246810")
    # 3.执行测试步骤
    self.home_proxy.to_pub_air_tab()
    self.pub_ari_proxy.test_pub_aritcal(ari_title, ari_context, ari_channel)
    # 4.结果断言
    assert is_element_exist(self.driver, "新增文章成功")
    不使用参数化的方法
    """

    # 5.关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
