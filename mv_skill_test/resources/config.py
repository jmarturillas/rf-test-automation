import sys
import os.path
import json
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "mv_skill_test")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))


class Config(object):

    def __init__(self):
        self.setup = None
        self.data = None
        self.locators = None
        self._load_data()

    def _load_data(self):
        self.setup = Config.load_json(file_name='setup')
        self.data = Config.load_json(file_name='data')
        self.locators = Config.load_json(file_name='locators')

    @staticmethod
    def load_json(file_name=None):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'data/{0}.json'.format(file_name))
        data = json.load(open(file_path))
        return data


if __name__ == '__main__':
    c = Config()
    print(c.setup['library'])
