import sys
import os.path
import json
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "mv_skill_test")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from PageObjectLibrary import PageObject


class Helpers(PageObject):

    def input_data(self, locator, data):
        self.se2lib.input_text(locator, data)

    def click_button(self, locator):
        self.se2lib.click_element(locator)

