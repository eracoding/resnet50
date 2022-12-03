import os
import re
import time

import requests
import random

from backend.settings import BASE_DIR


class SearchImage:
    REG_EX = "(src=\"//avatars[\w.?=&;,://-]*\")"
    MAIN_SEARCH = "https://yandex.ru/images/search?from=tabbar&text="

    def __init__(self, search):

        self.category = search

    def getImage(self):
        path = os.path.join(BASE_DIR.absolute(), "images", self.category)
        try:
            os.mkdir(path)
        except:
            pass
        req = requests.get(self.MAIN_SEARCH + self.category)
        text = req.text
        all_result = re.findall(self.REG_EX, text)
        for index in range(len(all_result)):
            try:
                true_url = all_result[index].replace('"', '').replace("src=", 'http:')
                c = requests.get(true_url, allow_redirects=True)
                open(os.path.join(path, "image_" + str(index) + ".png"), 'wb').write(c.content)
            except requests.exceptions.MissingSchema:
                pass
