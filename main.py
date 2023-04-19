"""
___TO-DO___
-sqlite entegre et
"""

import sqlite3 as sl
kitaplık= sl.connect("kitaplık.db")
class kitap():
    def __init__(self,ad,yayınevi,yazar,sayfa) -> None:
        self.ad=ad
        self.yevi=yayınevi
        self.yazar=yazar
        self.sayfa=sayfa

