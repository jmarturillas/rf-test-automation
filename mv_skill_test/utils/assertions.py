import sys
import os.path
import json
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "mv_skill_test")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from PageObjectLibrary import PageObject


class Assertions(PageObject):

    def assert_element_exists(self, locator):
        self.se2lib.wait_until_page_contains_element(locator, 60)
        self.se2lib.page_should_contain_element(locator)

    def assert_page_contains_text(self, text):
        self.se2lib.wait_until_page_contains(text, 60)
        self.se2lib.page_should_contain(text)
