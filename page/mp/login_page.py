# 对象库层---自媒体
from selenium.webdriver.common.by import By

from base.mp_base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 给每个对象定义一个实例属性
        # 账号输入框
        self.username = (By.CSS_SELECTOR, "[placeholder*='手机号']")
        # 验证码
        self.verify_code = (By.CSS_SELECTOR, "[placeholder*='验证码']")
        # 登录按钮
        self.login_button = (By.CSS_SELECTOR, "[class*='el-button--primary']")

    # 找到账号输入框
    def find_username(self):
        return self.find_elt(self.username)

    # 找到验证码输入框
    def find_verify_code(self):
        return self.find_elt(self.verify_code)

    # 找到登录按钮
    def find_click_button(self):
        return self.find_elt(self.login_button)


# 操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 用户名输入
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 验证码输入
    def input_code(self, code):
        self.input_text(self.login_page.find_verify_code(), code)

    # 点击登录按钮
    def click_login_btn(self, ):
        self.login_page.find_click_button().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务方法
    def test_mp_login(self, username, code):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入验证码
        self.login_handle.input_code(code)
        # 点击登录按钮
        self.login_handle.click_login_btn()
