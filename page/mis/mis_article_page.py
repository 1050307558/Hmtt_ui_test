# 对象库层
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle
from utils import check_channel_option, DriverUtils


class MisArticlePage(BasePage):

    def __init__(self):
        super().__init__()
        # 2.输入搜索的文章名称
        self.article_name = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 3.选择文章状态
        # 在操作层使用公用的下拉框选择方法
        # 选择查询按钮
        self.select_btn = (By.CSS_SELECTOR, ".find")
        # 4.点击通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 5.点击驳回按钮
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        # 6.弹出框选择——通过/驳回按钮
        self.reject_and_pass_btn = (By.CSS_SELECTOR, ".el-button--primary")
        # 查询时间叉号删除按钮
        self.dele_btn = (By.CSS_SELECTOR, ".el-icon-circle-close")

    # 找输入文章名称搜索框
    def find_article_name(self):
        return self.find_elt(self.article_name)

    # 找选择文章状态框
    # 操作层中调用方法
    # 找到查询按钮
    def find_select_btn(self):
        return self.find_elt(self.select_btn)

    # 找通过按钮
    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    # 找驳回按钮
    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    # 找驳回/通过按钮——弹出框——确认按钮
    def find_reject_and_pass_btn(self):
        return self.find_elt(self.reject_and_pass_btn)

    # 找到删除时间按钮
    def find_dele_btn(self):
        return self.find_elt(self.dele_btn)


# 操作层
class MisPageHandle(BaseHandle):
    def __init__(self):
        self.mis_article_page = MisArticlePage()

    # 文章标题的输入
    def input_title_name(self, title):
        self.input_text(self.mis_article_page.find_article_name(), title)

    # 文章状态的选择
    def choice_article_state(self, article_state):
        check_channel_option(DriverUtils.get_mis_driver(), "请选择", article_state)

    # 点击查询按钮
    def cilck_select_btn(self):
        self.mis_article_page.find_select_btn().click()

    # 点击通过按钮
    def click_pass_btn(self):
        self.mis_article_page.find_pass_btn().click()

    # 点击驳回按钮
    def click_reject_btn(self):
        self.mis_article_page.find_reject_btn().click()

    # 点击通过驳回按钮---弹出框确认按钮
    def click_reject_and_pass_btn(self):
        self.mis_article_page.find_reject_and_pass_btn().click()

    # 点击删除时间按钮
    def click_dele_btn(self):
        self.mis_article_page.find_dele_btn().click()


# 业务层
class MisArticleProxy:
    def __init__(self):
        self.mis_article_handle = MisPageHandle()

    # 审核通过
    def test_article_pass(self, title):
        # 1.输入文章名称
        self.mis_article_handle.input_title_name(title)
        # 2.选择状态
        self.mis_article_handle.choice_article_state("待审核")
        # 鼠标悬停到时间位置
        # mouse = ActionChains(self.driver)
        # 点击时间删除按钮
        self.mis_article_handle.click_dele_btn()
        time.sleep(2)
        # 3.点击查询
        self.mis_article_handle.cilck_select_btn()
        time.sleep(3)
        # 4.点击通过
        self.mis_article_handle.click_pass_btn()
        # 5.点击弹出框确认按钮
        self.mis_article_handle.click_reject_and_pass_btn()
        time.sleep(2)
        # 6.选择文章状态为审核通过
        self.mis_article_handle.choice_article_state("审核通过")
        time.sleep(2)
        # 7.点击查询按钮
        self.mis_article_handle.cilck_select_btn()
        time.sleep(3)

    # 审核驳回
    def test_article_reject(self):
        # 1.输入文章名称
        # 2.选择状态
        self.mis_article_handle.choice_article_state("待审核")
        # 3.点击查询
        self.mis_article_handle.cilck_select_btn()
        time.sleep(3)
        # 4.点击驳回
        self.mis_article_handle.click_reject_btn()
        # 5.点击弹出框确认按钮
        self.mis_article_handle.click_reject_and_pass_btn()
        # 6.切换审核失败界面
        self.mis_article_handle.choice_article_state("审核失败")
        # 7.点击查询按钮
        self.mis_article_handle.cilck_select_btn()
        time.sleep(3)
