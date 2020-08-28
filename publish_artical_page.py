"发布文章界面"
from selenium.webdriver.common.by import By

from base.mp_base.base_page import BasePage, BaseHandle


# 对象库层
class PubAriPage(BasePage):

    # 使用实例属性定义所有要操作的元素定位方式以及表达式
    # 使用实例方法找所有要用到的元素对象
    def __init__(self):
        super().__init__()
        # 标题
        self.ari_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # iframe
        self.ari_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 内容
        self.ari_context = (By.CSS_SELECTOR, "body")
        # 封面
        self.ari_cover = (By.XPATH, "//*[text()='自动']")
        # 频道选择框
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 频道选项
        self.channel_option = (By.XPATH, "//*[text()='android']")
        # 发表
        self.pub_btn = (By.XPATH, "//*[text()='发表']")

    # 找标题
    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    # 找iframe
    def find_ari_iframe(self):
        return self.find_elt(self.ari_iframe)

    # 找内容
    def find_ari_context(self):
        return self.find_elt(self.ari_context)

    # 找封面
    def find_ari_cover(self):
        return self.find_elt(self.ari_cover)

    # 找频道选择框
    def find_channel(self):
        return self.find_elt(self.channel)

    # 找频道选项
    def find_channel_option(self):
        return self.find_elt(self.channel_option)

    # 找发表按钮
    def find_pub_btn(self):
        return self.find_elt(self.pub_btn)


# 操作层
class PubAriHandle(BaseHandle):

    def __init__(self):
        pass


# 业务层
class PubAriProxy:
    def __init__(self):
        pass
