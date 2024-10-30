import sys

import requests

sys.path.append("/Users/fuxianglun/PycharmProjects/cicd-study/.venv/lib/python3.12/site-packages")
class Test:

    def test(self):
       r = requests.get(url="https://www.baidu.com/");
       print(r.status_code)
       assert r.status_code == 200
       print(2)
