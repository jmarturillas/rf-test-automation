"""
This is the base class for all page objects.
"""
import sys
import os.path
from robot.libraries.String import String

_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "mv_skill_test")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from mv_skill_test.resources.config import Config
from mv_skill_test.utils.helpers import Helpers
from mv_skill_test.utils.assertions import Assertions


class Page(PageObject):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.helpers = Helpers()
        self.assertions = Assertions()
        self.base_url = self.config.setup['uris']['home']
        self.login_url = self.config.setup['uris']['login']
        self.chosen_browser = self.config.setup['browser']
        # self.se2lib = BuiltIn().get_library_instance("Selenium2Library")

    def launch_browser(self, url=None, browser=None):
        self.se2lib.open_browser(url, browser)
        self.se2lib.set_window_position(0, 0)
        self.se2lib.set_window_size(1440, 900)

    def launch_app(self):
        self.launch_browser(url=self.login_url, browser=self.chosen_browser)

    def quit_browser(self):
        self.se2lib.close_browser()


if __name__ == '__main__':
    p = Page()
    print(p.config.setup)