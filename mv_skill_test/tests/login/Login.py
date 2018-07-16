import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "mv_skill_test")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from mv_skill_test.resources.Page import *


class Login(Page):
    def __init__(self):
        super(Login, self).__init__()

    def login_with(self, username='', password=''):
        self.helpers.input_data(self.config.locators['locators']['login_page']['txt_email'], username)
        self.helpers.input_data(self.config.locators['locators']['login_page']['txt_password'], password)
        self.helpers.click_button(self.config.locators['locators']['login_page']['btn_login'])

    def validate_error_in_page(self):
        self.assertions.assert_element_exists(self.config.locators['locators']['login_page']['err_login'])

    def click_forgot_password(self):
        self.helpers.click_button(self.config.locators['locators']['login_page']['lnk_forgot_pw'])

    def validate_email_text_field_in_page(self):
        self.assertions.assert_element_exists(self.config.locators['locators']['forgot_password_page']['txt_email'])

    def validate_redirect_account_home_page(self):
        self.assertions.assert_page_contains_text(self.config.data['data']['expected_data']['account_page'])
