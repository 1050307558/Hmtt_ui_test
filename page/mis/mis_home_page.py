# 对象库层
from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle


class MisHomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 信息管理菜单栏
        self.info_manage = (By.XPATH, "//*[text()='信息管理']")
        # 内容审核菜单栏
        self.context_manage_tab = (By.XPATH, "//*[text()='内容审核']")

    # 找到信息管理菜单
    def find_info_manage_tab(self):
        return self.find_elt(self.info_manage)

    # 找到内容审核菜单
    def find_context_manage_tab(self):
        return self.find_elt(self.context_manage_tab)


# 操作层
class MisHomeHandle(BaseHandle):
    def __init__(self):
        self.hom_page = MisHomePage()

    # 内容管理菜单栏点击
    def cilck_info_manage_btn(self):
        self.hom_page.find_info_manage_tab().click()

    # 发布文章导航栏点击
    def cilck_context_manage_btn(self):
        self.hom_page.find_context_manage_tab().click()


# 业务层
class MisHomeProxy:
    def __init__(self):
        self.mis_home_handle = MisHomeHandle()

    # 跳转发布文章页面
    def to_mis_article(self):
        # 点击内容管理菜单
        self.mis_home_handle.cilck_info_manage_btn()
        # 点击发布文章菜单
        self.mis_home_handle.cilck_context_manage_btn()


########################################################################################
# 面试的时候不用以下方法回答，实际工作如果要求不严，可以使用
# 对象库层
# from selenium.webdriver.common.by import By
#
# from base.mis_base.base_page import BasePage, BaseHandle
#
#
# class MisHomePage(BasePage，BaseHandle):
#     def __init__(self):
#         super().__init__()
#         # 信息管理菜单栏
#         self.info_manage = (By.XPATH, "//*[text()='信息管理']")
#         # 内容审核菜单栏
#         self.context_manage_tab = (By.XPATH, "//*[text()='内容审核']")
#
#     # 定义实例方法----实例方法对应的事测试步骤中一些连续性动作
#     # 跳转内容审核页面
#     def find_info_manage_tab(self):
#         # 点击信息管理菜
#         self.find_elt(self.info_manage).click()
#
#     # 点击内容审核菜单
#     def find_context_manage_tab(self):
#         self.find_elt(self.context_manage_tab).click()
